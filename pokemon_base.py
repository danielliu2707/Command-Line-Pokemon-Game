from __future__ import annotations
"""

This file demonstrates the implementation of the PokemonBase class, effectively giving the basic properties and general capabilities shared between all Pokemon

September 2022
"""


from abc import ABC, abstractmethod
from random_gen import RandomGen


__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"


"""

All methods have a best/worst case time complexity O(1), constant time.

"""


class PokemonBase(ABC):
    """

    This is the implementation of the abstract PokemonBase Class, effectively providing the basic functionality and attributes shared by all Pokemon

    This class inherits from the Python ABC module to get the functionality to become a Base Class

    Class Attributes:
        EFFECTIVE_MULTIPLIER_LST (PythonList): A list of lists that gives the effective multiplier combinations between all Pokemon Types

    Instance Attributes:
        max_hp (int): An integer giving the maximum health of a pokemon (aka hitpoints (hp))
        poke_type (str): A string giving the type of pokemon that the pokemon in question is (Fire or Water etc)
    """

    EFFECTIVE_MULTIPLIER_LST = [[1, 2, 0.5, 1, 1],
                                [0.5, 1, 2, 1, 1],
                                [2, 0.5, 1, 1, 1],
                                [1.25, 1.25, 1.25, 2, 0],
                                [1.25, 1.25, 1.25, 0, 1]]

    POKEMON_TYPES = ['fire', 'water', 'grass', 'normal', 'ghost']

    def __init__(self, hp: int, poke_type: str) -> None:
        """

        This is the constructor method for the PokemonBase Class

        Parameters:
            hp (int): An integer giving the hitpoints of a pokemon
            poke_type (str): A string giving the type of the pokemon

        Pre-condition:
            - HP should be an integer and greater than 0
            - Poke_type should be a string and be one of the pokemon types

        """
        if not isinstance(hp, int):
            raise TypeError("Incorrect value for hp")
        if not isinstance(poke_type, str):
            raise TypeError("Incorrect type for poke_type")
        if hp <= 0:
            raise ValueError("Hp must be greater than 0")
        if poke_type.lower() not in PokemonBase.POKEMON_TYPES:
            raise ValueError("Incorrect pokemon type")
        self.max_hp = hp
        self.poke_type = poke_type

    def is_fainted(self) -> bool:
        """

        This method effectively checks if a pokemon is fainted or not, which is done by checking if the Pokemon's hitpoints are lower than or equal to 0

        Parameters:
            None

        Returns:
            True or False (bln): A boolean value that is True if the Pokemon is fainted, and False if the Pokemon is not fainted
        """

        if self.hp <= 0:
            return True
        return False

    def level_up(self) -> None:
        """

        This method effectively increments a pokemon's level up by 1

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
        A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        self.level += 1

    def heal(self) -> None:
        """

        This method effectively heals a pokemon back up to its max hp by setting its current hp to its max hp

        Parameters:
            None

        Returns:
            None
        """

        self.hp = self.max_hp
        self.status = "free"

    @abstractmethod
    def get_hp(self) -> int:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return an integer representing the current hp of the Pokemon
        """

        pass

    @abstractmethod
    def get_status(self) -> str:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            String (int): The child class's method will return a string representing the current status of the Pokemon (eg. Burnt)
        """

        pass

    @abstractmethod
    def get_speed(self) -> int:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return an integer representing the current speed of the Pokemon
        """

        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return an integer representing the current attack damage of the Pokemon
        """

        pass

    @abstractmethod
    def get_defence(self) -> int:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return an integer representing the current defence of the Pokemon
        """

        pass

    def lose_hp(self, lost_hp: int) -> None:
        """

        This method effectively reduces the Pokemon's hp by a specified amount given by the paramater lost_hp

        Parameters:
            lost_hp (int): An integer representing the amount of hp that the Pokemon is going to lose

        Returns:
            None

        Pre-Condition:
            The Pokemon in question must either be attacked, under the affect of a status, or have lasted on round of attacks in a battle and lost 1 hp as a result

        Post-Condition:
            self.hp has to be lower than it was by an amount equaling lost_hp before lose_hp was called
        """

        self.hp -= lost_hp

    @abstractmethod
    def defend(self, damage: int) -> None:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation

        """

        pass

    def attack(self, other: PokemonBase) -> None:
        """

        This method effectively facilitates one Pokemon's attack onto another Pokemon

        Parameters:
            other (PokemonBase): An instantiation of the PokemonBase Class representing another Pokemon

        Returns:
            None

        Pre-Condition:
            If the pokemon in question is capable of attacking (not asleep or lucky when confused)

        Post-Condition:
            Defending Pokemon's hp is lower by the Attacking Pokemon's effective attack ran through the defending Pokemon's defend method
        """

        self.can_attack = True
        # Step 1: Status effects on attack damage / redirecting attacks
        self.status_effect_for_attack()
        if self.can_attack:
            # self.can_attack means if it can attack 'successfully'
            # If it can attack, it'll attack 'successfully', regardless of whether it loses damage
            if self.status == "burn":
                # If a fire status effect, impose a * 0.5 attack damage.
                other.defend(
                    int(self.check_effective_multiplier(other) * self.get_attack_damage() * 0.5))
            else:
                other.defend(
                    int(self.check_effective_multiplier(other) * self.get_attack_damage()))

            # If it successfully attacks (i.e: even does damage of 0), it'll lose hp
            self.status_effect_hp()

        if self.can_attack and RandomGen.random_chance(0.2):
            # Must check can_attack to see if it attacked 'successfully', only then can it implement a status effect on another pokemon
            self.set_status(other)

    def check_effective_multiplier(self, other):
        """

        This method checks the effective multiplier that a Pokemon has when attacking another Pokemon

        Parameters:
            other (Pokemon): A Pokemon Object representing the Pokemon that is being attacked

        Returns:
            PokemonBase.EFFECTIVE_MULTIPLIER_LST[attack_index][defend_index] (int): An integer representing the effective multiplier that the attacking Pokemon has on the defending Pokemon
        """

        def calc_index(type_poke):
            """

            This nested method essentially gives an integer representing the index as per the structure of the EFFECTIVE_MULTIPLIER_LST class variable, basically an index giving the type of the attacking pokemon

            Parameters:
                type_poke (str): A string representing the type of the Pokemon

            Returns:
                integer (int): An integer representing the index of the Attacking Pokemon as per the structure of the EFFECTIVE_MULTIPLIER_LST
            """

            if type_poke == 'fire':
                return 0
            if type_poke == 'grass':
                return 1
            if type_poke == 'water':
                return 2
            if type_poke == 'ghost':
                return 3
            if type_poke == 'normal':
                return 4

        attack_index = calc_index(self.poke_type.lower())
        defend_index = calc_index(other.poke_type.lower())

        return PokemonBase.EFFECTIVE_MULTIPLIER_LST[attack_index][defend_index]

    def set_status(self, other_poke: PokemonBase):
        """

        This method effectively sets the status of the defending Pokemon based on the type of the attacking Pokemon

        Paramters:
            other_poke (Pokemon): A PokemonBade object that represents the defending Pokemon

        Returns:
            None

        Pre-Condition:
            The attacking Pokemon has to have already attacked the defending Pokemon and has to have got won the 20% chance of inflicting a status effect on the defending Pokemon

        Post-Condition:
            The defending Pokemon will have a status set to it that is based on the type of the attacking Pokemon
        """

        # Other pokemon might get the status of attacker pokemons status
        if self.poke_type.lower() == 'fire':
            other_poke.status = 'burn'
        elif self.poke_type.lower() == 'grass':
            other_poke.status = 'poison'
        elif self.poke_type.lower() == 'water':
            other_poke.status = 'paralysis'
        elif self.poke_type.lower() == 'ghost':
            other_poke.status = 'sleep'
        else:
            other_poke.status = 'confuse'

    def status_effect_for_attack(self):
        """

        A method which essentially checks the two status's that effect a Pokemon's capacity to attack another Pokemon (Confusion and Sleep) and switches of Attack Capability accordingly

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            The Attack Method has to have been called for a Pokemon attacking another Pokemon

        Post-Condition:
            Depending on the attacking Pokemon's status, the can_attack boolean is modified accordingly
        """

        if self.status == "sleep":
            self.can_attack = False  # if the pokemon is asleep, it cannot attack
        elif self.status == "confuse":
            # if the 50% chance is satisfied, then damage itself when it is confused
            if RandomGen.random_chance(0.5):
                self.defend(int(self.check_effective_multiplier(
                    self) * self.get_attack_damage()))
                self.can_attack = False  # it cannot attack because it attacks itself
            else:
                self.can_attack = True  # otherwise it can attack the opponent pokemon

    def status_effect_hp(self):
        """

        This method effectively checks for and runs the two status effects that result in a direct hp loss, that being burn and poison

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            The Attack method has to have been called for a Pokemon attacking another Pokemon

        Post-Condition:
            If the Attacking Pokemon has a relevant status effect, then it loses hp accordingly to the status effect
        """

        # damage calculation for the status effects that causes the pokemon to lose hp
        if self.status == "burn":
            self.lose_hp(1)
        if self.status == "poison":
            self.lose_hp(3)

    @abstractmethod
    def get_level(self) -> int:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return an integer representing the current level of the Pokemon
        """

        pass

    @abstractmethod
    def get_poke_name(self) -> str:
        """

        This method is an abstract method that will be concretely implemented in its child class, the Pokemon Class

        Parameters:
            None

        Returns:
            Integer (int): The child class's method will return a string representing the name of the Pokemon
        """

        pass

    def __str__(self) -> str:
        """

        This is the string method of the PokemonBase Class, effectively giving the string representation of the class when a print function is called to print an instantiation of the PokemonBase Class, or one of its child classes

        Returns:
            String (str): A string representing the string representation of the class
        """

        return f"LV. {self.level} {self.name}: {self.hp} HP"

    def should_evolve(self) -> bool:
        """

        This method effectively checks whether a Pokemon has met the level-based requirements and is ready to evolve into its evolved formats

        Parameters:
            None

        Returns:
            True or False (bln): A boolean value that is True if the Pokemon should evolve, and False if the Pokemon should not evolve

        Pre-Condition:
            If a Pokemon levels up after a battle

        Post-Condition:
            N/A
        """

        try:
            if self.level == self.evolved_version.level:  # Base level of new initialized evolved object
                return True  # returns True if the level is at the sufficient level for evolution
            return False
        except AttributeError:
            return False

    def can_evolve(self) -> bool:
        """

        This method effectively checks whether a Pokemon has an evolved form to actually evolve to

        Parameters:
            None

        Returns:
            True or False (bln): True if the Pokemon has an evolved version, False if the Pokemon does not have an evolved version

        Pre-Condition:
            Can only be run after a Pokemon levels up after a battle

        Post-Condition:
            N/A
        """

        # If there is an evolved version then we check if the pokemon is not fainted
        if self.evolved_version != None:
            if not self.is_fainted():
                return True  # if it isn't fainted, then it can evolve
            else:
                return False
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        """

        This method effectively gives the evolved version PokemonBase object that is the evolved version of the Pokemon in question

        Parameters:
            None

        Returns:
            evolved_poke (PokemonBase): A PokemonBase Object represnting the evolved version of the Pokemon

        Pre-Condition:
            If should_evolve has return True

        Post-Condition:
            N/A
        """

        if self.can_evolve():
            difference_hp = self.max_hp - self.hp
            evolved_poke = self.evolved_version  # Retrieve evolved version
            # Computes the hp for the evolved pokemon
            evolved_poke.hp = evolved_poke.max_hp - difference_hp
            evolved_poke.status = self.status  # Set status to old poke
            return evolved_poke

    def check_evolution(self) -> PokemonBase:
        """

        This method efectively gives the evolved version of the Pokemon in question

        Parameters:
            None

        Returns:
            evoloution (PokemonBase): A PokemonBase Object that represents the evolved version Pokemon of the Pokemon in question


        Pre-Condition:
            Can only be run after a Pokemon levels up after a battle

        Post-Condition:
            N/A
        """

        if self.should_evolve():
            evolution = self.get_evolved_version()  # Obtain the evolved version
            # Set unique ID to that of its evolved version
            evolution.unique_id = self.unique_id
            return evolution  # Return evolved pokemon
        else:
            return self  # If the pokemon cannot evolve then return its own object
