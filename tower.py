from __future__ import annotations
from random_gen import RandomGen
from queue_adt import CircularQueue
from battle import Battle
from poke_team import PokeTeam, Criterion
"""

This is the file that demonstrates the implementation of the BattleTower

September 2022

"""

__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"

"""

All methods have a best/worst case time complexity O(1), constant time unless otherwise stated.

"""


# Various imported libraries


class BattleTower:
    """

    This is the implementation of the BattleTower Class, where an instantiation of it contains the protagonist team and the random teams (with lives) they must face in order to win the tower

    Instance Attributes:
        tower (none)/(CircularQueue): Initially set to none, but each instantiation (via it's generate teams method) changes it to a CircularQueue
        battle (battle) : A Battle object that is used to create the individual battles within the Tower
    """

    def __init__(self, battle: Battle | None = None) -> None:
        """

        This is the constructor method of the BattleTower Class 

        Paramaters:
            battle (Battle): A Battle object used to create individual battles within the Tower game format
        """

        self.tower = None
        self.battle = battle

    def set_my_team(self, team: PokeTeam) -> None:
        """

        This method effectively allows for the protagonist PokeTeam to be set

        Parameters:
            team (PokeTeam): A PokeTeam Object that represents the team that is going to battle through the tower

        Returns:
            None
        """

        self.my_team = team

    def generate_teams(self, n: int) -> None:
        """

        This method effectively allows for the generation of an n number of random teams (with a random amount of lives) to fight against in the tournament

        Parameters:
            n (int): An integer representing the amount of randomly generated teams needed to be made

        Returns:
            None

        Complexity analysis:
            Best Case: O(n) where the n is the number of teams that will be created
            Worst Case: O(n)
        """

        if n >= 1:  # Makes it user facing as it validates for the number of randomly generated teams
            tower = CircularQueue(n)
            for num_gen in range(n):  # Iterating through number of teams to be created
                # Randomly chosing a Battle Mode (0 or 1)
                battle_mode = RandomGen.randint(0, 1)
                rand_team = PokeTeam.random_team(
                    f'Team {num_gen}', battle_mode)  # Instantiating a random PokeTeam Object
                rand_team.num_lives = RandomGen.randint(2, 10)
                # Adding the randomly generated team to the Tower (CircularQueue Object)
                tower.append(rand_team)
            self.tower = tower
        else:
            # If n is 0 or a negative amount of randomly generated Poke Teams, A ValueError is raised
            raise ValueError('Tower must contain atleast 1 PokeTeam')

    def __iter__(self):
        """

        This is the iterator magic method, making the referenced object (self) iterable

        Paramaters:
            None

        Returns:
            Self (but in this case it is a self that points towards the BattleTowerIterator Class)
        """

        if self.my_team is not None:  # tower can be none for the condition that the my_team wins
            self = BattleTowerIterator(
                self.tower, self.my_team, self.battle)  # Getting Self to point to the BattleTowerIterator Object
            return self
        # Cannot iterate through the tower if all teams in the tower are taken out, my_team has won
        raise ValueError('No my_team found')


class BattleTowerIterator:
    """

    This Class effectively facilitates the iteration through the BattleTower Class, allowing each round of Battles to take place until either the protagonist team wins or all the random teams all have 0 lives left

    Instance Attribute:
        battle_tower (CircularQueue): A circular Queue object that essentially just represents the tower of randomly generated teams to fight through
        my_team (PokeTeam): A PokeTeam object used to represent the team that is fighting through the battle
        battle (Battle): 

    """

    def __init__(self, tower: CircularQueue, my_team: PokeTeam, battle: Battle):
        # setting the battle_tower instance attribute to equal tower which is a variable representing a CircularQueue object
        self.battle_tower = tower
        # setting the poke_team instance attribute to equal the my_team PokeTeam object
        self.my_poke_team = my_team
        # setting the battle_poke instance attribute to equal the battle Battle Object
        self.battle_poke = battle

    def __next__(self):
        """

        This is the next magic method which essentially represents each individual battle of each round throughout the tower

        Paramaters:
            None

        Return:
            (res, player_team, tower_team, team2.num_lives) (tuple): Effectively gives the result of the current battle in the current round of the battle
        """

        # '''Check if it's O(B) -> Serve, Append -> O(1) but    I think regenerate_team is not, neither is __str__.
        # __str__ shouldn't be too bad to fix but I think regenerate_team, we somehow
        # need to make a copy of the original team and not regenerate it every time. Otherwise, should all be O(B)'''
        if len(self.battle_tower) != 0:  # First checking if the self.battle_tower does not equal 0, meaning if the tower is not empy
            self.my_poke_team.regenerate_team()  # regenerating the protagonist team
            team2 = self.battle_tower.serve()  # getting the next random team to be fought
            # regenerating the next team as they may have already been fought in the last round
            team2.regenerate_team()
            # resetting the amount of heals the team has to 0, as they may have used heals the previous round
            team2.num_heals = 0
            # resseting the protagnoist team's num heals to 0 as well as this is a new battle
            self.my_poke_team.num_heals = 0
            # My Pokemon team is team 1, opposition is team 2:
            # running a battle between the protagonist team and the other team and setting the res to equal an integer relating to who won the battle
            res = self.battle_poke.battle(self.my_poke_team, team2)
            # If the opposing team wins
            player_team = self.my_poke_team
            if res == 2:  # If the random team in the tower won
                self.battle_tower.clear()
                tower_team = team2
                return (res, player_team, tower_team, team2.num_lives)
            # If your team wins/draws the battle
            else:
                team2.num_lives -= 1  # reduces the lives of the fought against tower random team
                # Only if team2 has more lives, put it back in the end of the CircularQueue:
                if not team2.num_lives <= 0:
                    self.battle_tower.append(team2)
                tower_team = team2
                return (res, player_team, tower_team, team2.num_lives)
        else:
            raise StopIteration  # End the iterator by raising a StopIteration Exception

    def __iter__(self):
        """

        This is the iterator magic method, making the referenced object (self) iterable

        Parameters:
            None

        Returns:
            None
        """

        return self

    def avoid_duplicates(self):
        """

        This method effectively works to eliminate teams that are still alive and have multiple Pokemon of the same type

        Parameters:
            None

        Returns:
            None

        Complexity:
            Best case: O(1) Only one pokemon team left
            Worst case: O(N*P) where N is the remaining number of Trainers in the Tower and P is maximum number of Pokemon on a team
        """
        # The following iterates through the length of the tower, retrieving a team from the tower
        # And only if no duplicates, append it to battle_tower
        for _ in range(len(self.battle_tower)):
            poke_team = self.battle_tower.serve()
            if max(poke_team.team_numbers) <= 1:
                self.battle_tower.append(poke_team)
