from __future__ import annotations
from stack_adt import ArrayStack
from linked_list import LinkedList
from battle import Battle
from poke_team import PokeTeam
"""

This file demonstrates the implementation of the Tournament class

September 2022

"""
__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"


"""

All methods have a best/worst case time complexity O(1), constant time unless otherwise stated.

"""

# Various imports needed to facilitate the Tournament class implementation


class Tournament:
    """
    This is the class representing the Tournament object, essentially referring to the tournament in which Pokemon trainers compete in alongside their respective Pokemon 
    where the tournament is completed when one player remains.

    Instance Attributes:
        battle_poke (Battle): A Battle instance that is used to create the individual battles in each tournament
        battle_mode (None): A battle mode that needs to be specified in order to determine how the pokemon team will be organised/modified/maintained.
        tournament_adt (None): A tournament abstract data type to hold the remaining players within the tournament.
    """

    def __init__(self, battle: Battle | None = None) -> None:
        """
        This is the constructor for the Tournament class

        Parameters:
            battle (Battle): A Battle instance that is passed on to create the individual battles within a tournament
        Returns:
            None
        Complexity analysis:
            Best case O(1) when user passes in a Battle object
            Worst case O(B) where B is the complexity of Battle when user doesn't pass in any arguments
        """

        # Create Battle instance if it doesn't exist
        self.battle_poke = battle
        if not battle:
            self.battle_poke = Battle()
        self.battle_mode = None
        self.tournament_adt = None

    def set_battle_mode(self, battle_mode: int) -> None:
        """
        This sets the battle mode for all randomly generated teams

        Parameters:
            battle_mode (int): An integer representing the battle mode used by all the randomly generated teams in the tournament

        Returns:
            None
        """

        self.battle_mode = battle_mode

    def is_valid_tournament(self, tournament_str: str) -> bool:
        """
        This is a method that checks that the tournament string that is passed through is a valid string i.e each player has an opponent to fight against

        Parameters:
            tournament_str (string): A string that represents the input of the structure of the tournament's battles, can be both in valid or invalid formats

        Returns:
            True or False (bool): A boolean value that is True when the tournament string is valid, and False when the tournamnet string is invalid

        Complexity analysis:
            Best case O(n * comp(==)) where n is the length of the tournament_str
            Worst case O(n * comp(==)) where n is the length of the tournament_str
        """

        array_stack = ArrayStack(len(tournament_str))
        # Push first letter
        # We assume that the first character is a letter and push player onto the stack (represented by 1)
        array_stack.push(1)
        had_first_letter = True
        for i in range(len(tournament_str)):
            # When the length of the stack is less than 1 there will be no winner so it is not valid
            if len(array_stack) < 1:
                return False
            if tournament_str[i] == '+':  # A plus represents that there should be a winner
                array_stack.pop()  # We pop 1 person because 1 of them should lose
            # If the tournament string is a letter or _
            # if the character is a letter and has not had a first letter, it is a new player.
            elif tournament_str[i] != '+' and tournament_str[i] != ' ' and not had_first_letter:
                array_stack.push(1)  # push new player onto stack
                # set as true to represent the first letter of that player as being accounted for
                had_first_letter = True
            # if the character is a space then the next character can be a new player or a plus
            elif tournament_str[i] == ' ':
                had_first_letter = False  # Therefore, set had_first_letter to false
        # if the loop iterates through the whole string and has more than 1 length, it is valid.
        return True

    def start_tournament(self, tournament_str: str) -> None:
        """

        This is the method which begins the Tournament by generating teams based on the tournament string input and inputting the teams and their respective match-ups into LinkedList

        Parameters:
            tournament_str (string): A string that represents the players in the tournament and the respective battles that they will be fighting in

        Returns:
            None

        Complexity analysis:
            Best case O(n * comp(==) + m * comp(==)) where n is the length of the tournament_str and m is the cost of splitting a string
            Worst case O(n * comp(==) + m * comp(==)) where n is the length of the tournament_str and m is the cost of splitting a string
        """

        if self.is_valid_tournament(tournament_str):
            # setting the tournament_adt instance attribute to equal a LinkedList ADT object
            self.tournament_adt = LinkedList()
            counter = 0
            # Iterating through a list that is created by splitting the tournamenet string input by its " "
            for player_name in tournament_str.split():
                if player_name != '+':  # If player_name is not an "+"
                    team = PokeTeam.random_team(player_name, self.battle_mode)
                    # Inserting the counter variable as a node and the team as its value
                    self.tournament_adt.insert(counter, team)
                    counter += 1
                # If the player_name == '+'
                else:
                    # Inserting the counter variable as a node but this time the value is a + sign
                    self.tournament_adt.insert(counter, '+')
                    counter += 1
        else:
            raise ValueError("Tournament string is not valid")

    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        """

        This is the method which advances the tournament by simulating one fight in the order given by the tournament_str input

        Parameters:
            None

        Returns:
            tuple(player1, player2, res) (tuple): A tuple containing the two Poketeams that fought in a battle and the integer result for battle

        Complexity:
            Best case O(B+P) where B is the cost of battling, P is the num of poke in party
            Worst case O(B+P) where B is the cost of battling, P is the num of poke in party
        """

        try:
            # Finds the first '+' available in the LinkedList
            index_first_plus = self.tournament_adt.index('+')
        except ValueError:
            # If it can't find a +
            return None
        else:  # If it does find a +
            # LinkedList structure => [player1, player2, '+'] etc
            # Finds first player to do the battling
            player1 = self.tournament_adt[index_first_plus-2]
            # Finds the respective opponent for player1, that is player2
            player2 = self.tournament_adt[index_first_plus-1]
            player1.regenerate_team()
            player2.regenerate_team()
            # Uses the battle method to get a result from Player1 and Player2 Battling
            res = self.battle_poke.battle(
                player1, player2)  # Both players battle
            # If player 2 wins, insert player 2 into the original position of player 1. Also store player 1's team_numbers as player_2 defeated it.
            if res == 2:
                self.tournament_adt[index_first_plus - 2] = player2
                if player2.poke_teams_beat is None:
                    player2.poke_teams_beat = player1.team_numbers
                    player1.poke_teams_beat = [0, 0, 0, 0, 0]
                else:
                    player2.poke_teams_beat = [
                        player2.poke_teams_beat + player1.team_numbers for _ in range(5)]
            # If player 1 wins or draws, no need to insert player 1 as its already in its correct position but store player2 team_numbers as player_1 defeated it.
            else:
                if player1.poke_teams_beat is None:
                    player1.poke_teams_beat = player2.team_numbers
                    player2.poke_teams_beat = [0, 0, 0, 0, 0]
                else:
                    player1.poke_teams_beat = [
                        player1.poke_teams_beat + player2.team_numbers for _ in range(5)]

            # Either way, delete 2 things in linked list after first player (losing player and +).
            # Deletes the first item
            self.tournament_adt.delete_at_index(index_first_plus-1)
            # Deletes the +
            self.tournament_adt.delete_at_index(index_first_plus-1)
            return (player1, player2, res)

    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        """

        This is a method that effectively gives list for each round of PokeTeam Matchups

        Parameters:
            None

        Returns:
            LinkedList[tuple[PokeTeam, PokeTeam]] (LinkedList): A Linked List object that represents all the matchups of a respective tournament round

        Complexity:
            Best case O(M) where M is the total number of matches 
            Worst case O(M) where M is the total number of matches 
        """

        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            # Inserts at index 0 so the very first matchup will be at the end of the LinkedList.
            l.insert(0, (res[0], res[1]))
        return l

    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        """

        This method returns a LinkedList representing each battle between two poke_teams and a list of lst_strings
        representing the poke types not present in either poke_teams battling but present in a team they defeated

        Parameters:
            None

        Returns:
            LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]

        Complexity:
            Worst case O(M * P) where M is the total number of matches and P is the number of poke in team
            Worst case O(M * P) where M is the total number of matches and P is the number of poke in team
        """

        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break

            poke_team_1 = res[0]
            poke_team_2 = res[1]

            poke_team_lst_1 = poke_team_1.team_numbers
            poke_team_lst_2 = poke_team_2.team_numbers

            lst_strings = []
            for i in range(5):
                # Checks whether any of the two teams don't have a particular pokemon type
                if poke_team_lst_1[i] == 0 and poke_team_lst_2[i] == 0:
                    # Check whether the other teams that have been beat had that particular pokemon type
                    if poke_team_1.poke_teams_beat[i] != 0 or poke_team_2.poke_teams_beat[i] != 0:
                        if i == 0:
                            lst_strings.append('FIRE')
                        elif i == 1:
                            lst_strings.append('GRASS')
                        elif i == 2:
                            lst_strings.append('WATER')
                        elif i == 3:
                            lst_strings.append('GHOST')
                        else:
                            lst_strings.append("NORMAL")

            l.insert(0, (poke_team_1, poke_team_2, lst_strings))
        return l
