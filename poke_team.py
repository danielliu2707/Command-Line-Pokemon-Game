from __future__ import annotations
"""

This file demonstrates the implementation of the PokeTeam class, effectively giving the basic properties, general capabilities and creating a pokemon team that can be used in battles.

September 2022
"""

from stack_adt import ArrayStack
from array_sorted_list import *
from random_gen import RandomGen
from pokemon_base import PokemonBase
from enum import Enum, auto
from queue_adt import CircularQueue
from pokemon import Charmander, Charizard, Venusaur, Bulbasaur, Blastoise, Squirtle, Gengar, Haunter, Gastly, Eevee


__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"

"""

All methods have a best/worst case time complexity O(1), constant time unless otherwise stated.

"""


class Action(Enum):
    """ Class for battle actions"""
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()


class Criterion(Enum):
    """ Class for criteria, can be used as a sorting key"""
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()


class PokeTeam:
    """

    This is the class represents the functionality of a PokeTeam that is created for battles

    Instance Attributes:
        team_name (str): A string giving the name of the pokemon team
        team_numbers (list): A list representation of the pokemon team
        battle_mode (int): An integer giving the battle mode that organises the strcuture of the team
        ai_type (AI): An AI Object that represents the different AI types that can be chosen
        criterion (Criterion): An integer giving the Pokemon's speed (mainly used for attack order)
        criterion_value (int): An integer that represents the pokemon attribute value
        num_heals (int): An intger that represents the number of heals that the team has used
        num_lives (None): Represents an integer that will be set in Tower 

    """

    class AI(Enum):
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:
        """ 
        Initialises the PokeTeam and instance variables

        :param team_name: Name of the team
        :param team_numbers: List representation of the team
        :battle_mode: The battle option used in battles
        :ai_type: The ai mode used in battle
        :criterion: A pokemon attribute
        :criterion_value: The pokemon attribute value
        :return: None


        Complexity analysis:
        Best case O(n) Where n is the length of team_numbers 
        Worst case O(n)

        """

        # User facing checks for the arguments:
        if isinstance(team_numbers, list):
            for item in team_numbers:
                if not isinstance(item, int):
                    raise ValueError('Please enter a list of integers')
                if (item > 6) or (item < 0):
                    raise ValueError(
                        'Integers in the list must be between 0 and 6 inclusive')
        else:
            raise ValueError('Please enter a list of integers')

        if not isinstance(battle_mode, int) or not isinstance(ai_type, PokeTeam.AI):
            raise ValueError('Please enter a valid input')
        if criterion != None:
            if not isinstance(criterion, Criterion):
                raise ValueError('Please enter a valid input')

        self.team_name = team_name
        # Team numbers is list representation of the team
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value
        # Create local variable so you only need to create stack/queue/sorted list once:
        self.create_team(battle_mode, criterion)
        self.num_heals = 0    # Number of heal actions used.
        self.num_lives = None
        # Stores poke teams that have been beaten
        self.poke_teams_beat = None

    def get_criteria_key(self, criterion: Criterion, poke: PokemonBase) -> int:
        """ Interprets criteria name and returns the appropriate attribute value from the Pokemon
        :param criterion: the string representation of the criteria
        :return: an integer containing the stat of the criteria

        Pre-Condition:
            If the PokeTeam's Battlemode is Battlemode 2

        Post-Condition:
            The Battlemode 2 ADT (linked to the PokeTeam) is sorted by the relevant criteria
        """

        criteria = criterion.name
        # Get criteria name and return corresponding attribute of the pokemon
        if criteria == 'SPD':
            return poke.get_speed()
        elif criteria == 'HP':
            return poke.get_hp()
        elif criteria == 'LV':
            return poke.get_level()
        else:
            return poke.get_defence()

    def create_team(self, battle_mode: int, criterion: Criterion = None) -> None:
        """
        Creates new random team using team_numbers which is the list
        of numbers representing how many of each base-level pokemon we initially want.

        :param battle_mode: Battle option to be used in battles
        :criterion: Attribute used as a criteria for sorting purposes
        :return: None

        Complexity analysis:
        Best case O(n * p) Where n is the length of team_numbers and p is the number of pokemon in the team
        Worst case O(n * 2p)
        """
        def create_poke(index):
            # Generates a pokemon based on the team_numbers index values
            if index == 0:
                return Charmander()
            if index == 1:
                return Bulbasaur()
            if index == 2:
                return Squirtle()
            if index == 3:
                return Gastly()
            if index == 4:
                return Eevee()
        # Generate team based on ADT
        # Battle mode 0 uses a stack
        if battle_mode == 0:
            # Create stack and store length
            my_team = ArrayStack(6)
            n = len(self.team_numbers)
            # Iterate in reverse, so when pushed last pokemon stays last as they would be pushed first
            for num_poke_index in range(n-1, -1, -1):
                if self.team_numbers[num_poke_index] != 0:
                    # Create pokemon(s) based on the number on the current index
                    for num in range(0, self.team_numbers[num_poke_index]):
                        poke_obj = create_poke(num_poke_index)
                        my_team.push(poke_obj)
            self.team_adt = my_team
        # Battle mode 1 uses a CircularQueue
        elif battle_mode == 1:
            # Create queue
            my_team = CircularQueue(6)
            # Iterate through team numbers
            for num_poke_index in range(len(self.team_numbers)):
                if self.team_numbers[num_poke_index] != 0:
                    # Create pokemon(s) based on the number on the current index
                    for num in range(0, self.team_numbers[num_poke_index]):
                        poke_obj = create_poke(num_poke_index)
                        my_team.append(poke_obj)
            self.team_adt = my_team
        # Battle mode 2 uses a SortedList
        else:
            # Create sorted array for team
            my_team = ArraySortedList(6)
            # Iterate through team numbers
            for num_poke_index in range(len(self.team_numbers)):
                poke_counter = 0  # initialise a counter for the number of the same pokemon created
                # Create another sorted list for tiebreakers
                if self.team_numbers[num_poke_index] != 0:
                    poke_specific_sorted_list = ArraySortedList(
                        self.team_numbers[num_poke_index])  # specific pokemon
                    # Create pokemon(s) based on the number on the current index
                    for _ in range(0, self.team_numbers[num_poke_index]):
                        poke_obj = create_poke(num_poke_index)
                        # Save counter as unique id, used to keep track of initial ordering
                        poke_counter += 1
                        poke_obj.unique_id = poke_counter
                        # Get sort key
                        criteria_key = self.get_criteria_key(
                            criterion, poke_obj)
                        # Add to tiebreak list
                        poke_specific_sorted_list.add(
                            ListItem(poke_obj, criteria_key * - 1+poke_obj.unique_id))
                    # Iterate again and create pokemon team
                    for _ in range(self.team_numbers[num_poke_index]):
                        # Get pokemon from tiebreak list, add to team
                        poke_specific_sorted_list[len(poke_specific_sorted_list)-1].key -= poke_specific_sorted_list[len(
                            poke_specific_sorted_list)-1].value.unique_id  # resetting values
                        item = poke_specific_sorted_list.delete_at_index(
                            len(poke_specific_sorted_list)-1)
                        my_team.add(ListItem(item.value, item.key))
                # Save team and check for tiebreaks if there are any upon creation
                self.team_adt = my_team
                self.tie_breaker_order()

    # Thus always call this class method first to create new poketeam, then do p = PokeTeam.random_team() to refer to our new PokeTeam.
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs) -> PokeTeam:
        """ 
        Generates a random team given a team size (3-6 if no team size)

        :param team_name: Name of the team
        :param battle_mode: Battle option used in battles
        :param team_size: Size of the team to be created
        :param ai_mode: AI option used in battles
        :**kwargs: Used to provide optional keyword arguments like criterion
        :returns: A PokeTeam representing the pokemon team

        """
        if not team_size:
            # Randomgen.randint is 3-6 inclusive.
            team_size = RandomGen.randint(3, 6)
        # Create sorted list,
        SortedL = ArraySortedList(6)  # assume max size given in spec pg 16
        # Add 0 and team_size to list
        # ListItem(value, key), key is the value to be sorted by
        SortedL.add(ListItem(0, 0))
        SortedL.add(ListItem(team_size, 6))
        # Generate 4 random numbers from 0 to team size
        for i in range(0, 4):
            num = RandomGen.randint(0, team_size)
            item = ListItem(num, num)
            SortedL.add(item)
        # For each adjacent value in the list, their difference specifies how many
        # Charmanders/Bulbasaurs/Squirtles/Gastlys/Eevees should be added to the team
        l = [0] * 5
        for i in range(1, len(SortedL)):
            l[i-1] = SortedL[i].value-SortedL[i-1].value
        # Create PokeTeam
        if not ai_mode:
            ai_mode = PokeTeam.AI.RANDOM
        new_team = PokeTeam(team_name, l, battle_mode, ai_mode,
                            **kwargs)
        if len(kwargs) != 0:
            # Creating sorted list (as criterion is specified)
            new_team.create_team(battle_mode, kwargs['criterion'])
        else:
            # Creating Queue/Stack (as criterion not specified)
            new_team.create_team(battle_mode)
        return new_team

    def tie_breaker_order(self):
        """ 
        Method to tiebreak pokemon ordering in battle mode 2
        This is a bubble sort as we are only comparing adjacent values

        Complexity analysis:
            Best/worst case O(n^2) where n is the length of the SortedList
            :return: None

        Pre-Condition:
            When the PokeTeam's chosen Battlemode is Battlemode 2

        Post-Condition:
            The PokeTeam's ADT is organised as per PokeDex order
        """
        for _ in range(len(self.team_adt)-1):
            for i in range(len(self.team_adt)-1):
                if self.team_adt[i].key == self.team_adt[i+1].key:
                    # If they have the same key but different id (i.e: Not same type of object -> Like one squirtle, one charmander)
                    if self.team_adt[i].value.id > self.team_adt[i+1].value.id:
                        self.team_adt.swap_items(i, i+1)
                    # If they have the same key and same id (i.e: Same type of object -> Like two charmanders) and not in correct order, change it:
                    elif self.team_adt[i].value.id == self.team_adt[i+1].value.id and self.team_adt[i].value.unique_id > self.team_adt[i+1].value.unique_id:
                        self.team_adt.swap_items(i, i+1)

    def return_pokemon(self, poke: PokemonBase) -> None:
        """ 
        Returns a pokemon back into team

            :param poke: the pokemon to return
            :return: None

        Pre-condition:
            If the team_adt is not empty

        Post-condition:
            N/A
        """

        # Firstly check if water status effect, in which case update speed again
        if poke.get_status() == 'paralysis':
            poke.speed = poke.max_speed

        # Then clear status effect
        poke.status = 'free'

        # Return based on ADT used
        if self.battle_mode == 0:
            if not poke.is_fainted():  # If the pokemon has fainted, don't return!
                self.team_adt.push(poke)
        if self.battle_mode == 1:
            if not poke.is_fainted():
                self.team_adt.append(poke)
        if self.battle_mode == 2:
            if not poke.is_fainted():
                # Inserts actual ListItem from original pokemon (poke) -> Where you implement returning of pokemon:
                # Check if sorted in ascending or descending order
                if self.team_adt[0].key < 0:
                    # Add poke to team
                    added_item = ListItem(
                        poke, -1 * self.get_criteria_key(self.criterion, poke))
                    self.team_adt.add(added_item)
                    # Check for ties
                    self.tie_breaker_order()
                # Ascending order
                else:
                    # Add poke to team
                    added_item = ListItem(
                        poke, self.get_criteria_key(self.criterion, poke))
                    self.team_adt.add(added_item)
                    # Check for ties
                    self.tie_breaker_order()

    def retrieve_pokemon(self) -> PokemonBase | None:
        """ 
        Retrieves a pokemon to go battle
            :returns: None if there is no pokemon otherwise a pokemon (PokemonBase).

         Pre-condition:
            If the team_adt is not empty

        Post-condition:
            N/A
        """
        if self.is_empty():  # If actual number elements in array is 0, return None.
            return None
        else:
            # Battle mode 0, retrieve first pokemon in the team
            if self.battle_mode == 0:
                return self.team_adt.pop()
            if self.battle_mode == 1:
                return self.team_adt.serve()
            if self.battle_mode == 2:
                # Delete and return element at first index
                return self.team_adt.delete_at_index(0).value

    def is_empty(self) -> bool:
        """ 
        Method to check if length of ADT == 0
            :return: True if empty else False
        """
        if len(self.team_adt) == 0:
            return True
        return False

    def regenerate_team(self) -> None:
        """ 
        Method to regenerate team to full health
            :return: None

        Complexity analysis: (Complexity of create_team)
        Best case O(n * p) Where n is the length of team_numbers and p is the number of pokemon in the team
        Worst case O(n * 2p)
        """
        self.create_team(self.battle_mode, self.criterion)

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """ 
        Handles actions in battle

            :param my_pokemon: Pokemon 1 in battle (on friendly side)
            :param their_pokemon: Pokemon 2 in battle (on opposing side)
            :return: An Action representing attack, swap and heal.

        Pre-condition: 
            If there is at least 1 pokemon on the field

        Post-condition:
            N/A

        """
        if self.ai_type.value == 1:  # ALWAYS ATTACK
            return Action(1)
        elif self.ai_type.value == 2:  # SWAP_ON_SUPER_EFFECTIVE
            # If their effective multiplier is larger than 1.5 attack stat, swap else attack.
            if their_pokemon.check_effective_multiplier(my_pokemon) >= 1.5:
                return Action(2)
            else:
                return Action(1)

        elif self.ai_type.value == 3:  # RANDOM -> Randomly selects an action
            # If used all heals, remove the option
            if self.num_heals == 3:
                actions = list(Action)
                actions.remove(Action.HEAL)
                # Adjust random so it doesnt account for heal option
                outcome = RandomGen.randint(0, len(actions)-1)
                number = actions[outcome]
                return Action(number)
            # Otherwise just pick random option
            else:
                number = RandomGen.randint(1, 4)
                # Increment heal count if it is picked
                if number == 3:
                    self.num_heals += 1
                return Action(number)

        else:  # USER_INPUT option
            u_input = int(input("Your Move: "))
            # Used up all heals so dedge
            if u_input == 3 and self.num_heals == 3:
                return None
            # If heal option then increment heal count
            elif u_input == 3:
                self.num_heals += 1
                return Action(u_input)
            return Action(u_input)

    def __str__(self):
        """ 
        Magic method, constructs a string representation of the team

            :return: A string representation of the pokemon team

            Complexity analysis:
            Best/worst case O(n) where n is the length of the pokemon team data structure
        """
        returned_str = f"{self.team_name} ({self.battle_mode}): ["
        if self.battle_mode == 0:
            # Make a copy of the stack, store length
            team_adt = self.team_adt
            n = len(self.team_adt)
            # Pop each item from stack, add it to string
            for index in range(n):
                if index != n - 1:
                    popped = team_adt.pop()
                    returned_str += f'{popped.__str__()}, '
                # Add ending part to string
                else:
                    popped = team_adt.pop()
                    returned_str += f'{popped.__str__()}]'
            return returned_str
        elif self.battle_mode == 1:
            # Make copy of queue, store length
            team_adt = self.team_adt
            n = len(self.team_adt)
            # Serve each item and add returned value into string
            for index in range(n):
                if index != n - 1:
                    served = team_adt.serve()
                    returned_str += f'{served.__str__()}, '
                # Add ending part to string
                else:
                    served = team_adt.serve()
                    returned_str += f'{served.__str__()}]'
            return returned_str
            # Use method in SortedList
        elif self.battle_mode == 2:
            return f"{self.team_name} ({self.battle_mode}): {self.team_adt.__str__()}"

    def special(self) -> None:
        """ 
        Method to handle special option

            :return: None
            Complexity analysis:
            Best/Worst time complexity O(n), where n is the length of the self.team_adt

        Pre-condition:
            If the team_adt is not empty

        Post-condition:
            N/A
        """
        # Swap first and last pokemon in team
        if self.battle_mode == 0:
            if len(self.team_adt) > 1:
                # This part involves retrieving all the items
                # Store middle part since we are only swapping first and last
                middle_size_adt = len(self.team_adt)-2
                top_item = self.team_adt.pop()
                temp_stack = ArrayStack(middle_size_adt)
                # Push onto temp stack until last element (this reverses the order)
                while len(self.team_adt) > 1:
                    temp_stack.push(self.team_adt.pop())
                # Get last item
                bottom_item = self.team_adt.pop()
                # Push top item first so it goes to the bottom
                self.team_adt.push(top_item)
                # Push temp stack back into team (reverse order again, making it back to original)
                for i in range(middle_size_adt):
                    item = temp_stack.pop()
                    self.team_adt.push(item)
                # Push bottom item last so it goes to top
                self.team_adt.push(bottom_item)
        # Swap first and second halves, reverse order of prev front half (so the second half after swap)
        # Second half always same or bigger than first
        elif self.battle_mode == 1:
            if len(self.team_adt) > 1:
                # Removing the first half of elements from Queue:
                # Floor divide to not include middle element (for odd lengths)
                number_poke_first_half = len(self.team_adt) // 2
                # Use stack to reverse order
                temp_stack = ArrayStack(number_poke_first_half)
                # Serve first half and push to stack
                for i in range(number_poke_first_half):
                    temp_stack.push(self.team_adt.serve())
                # Appending back first half to second half of Queue, keeping the reversed order:
                for i in range(number_poke_first_half):
                    self.team_adt.append(temp_stack.pop())
        # Swap sorting order
        else:
            # Create new SortedList and add to it in reversed order
            new_sorted_lst = ArraySortedList(len(self.team_adt))
            # Iterate through old SortedList
            for i in range(len(self.team_adt)):
                item = self.team_adt.delete_at_index(0)
                # Multiply by -1 to invert sorting key so it sorts in reverse order
                item.key = item.key * -1
                new_sorted_lst.add(item)
            # Save new list and check for tiebreaks
            self.team_adt = new_sorted_lst
            self.tie_breaker_order()
