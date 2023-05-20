from __future__ import annotations
"""

This file demonstrates the implementations for all the individual Pokemon Classes that are all child classes of the Abstract Base Class: PokemonBase

September 2022
"""

# Required library imports for the individual pokemon clas implementation
from pokemon_base import PokemonBase
from random_gen import RandomGen

__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"

"""

All methods have a best/worst case time complexity O(1), constant time.

"""


class Charmander(PokemonBase):

    """

    This is the class that effectively facilitates the functionality and specific attributes of a Charmander Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (Charizard): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Charmander Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 9, 'Fire')
        self.name = 'Charmander'
        self.level = 1
        self.hp = 9
        self.attack_damage = 7
        self.speed = 8
        self.defence = 4
        self.evolved_version = Charizard()
        self.can_attack = True
        self.status = "free"
        self.id = 1
        self.max_speed = 8
        self.unique_id = 0

    def defend(self, damage: int) -> None:    # Damage = Damage inflicted on this pokemon
        """

        This method essentially runs the specific defence calculation for Charmander

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage > self.get_defence():
            # Lose hp equal to damage if greater than defence stat
            self.lose_hp(damage)
        else:
            # Otherwise lose half
            self.lose_hp(damage//2)

    def level_up(self):
        """

        This method effectively levels up a Charmander (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp   # Difference in hp used
            self.max_hp = 8 + (1*self.level)
            self.hp = self.max_hp - difference_hp
            self.attack_damage = 6 + (1*self.level)
            self.speed = 7+(1*self.level)
            self.max_speed = 7+(1*self.level)

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Charmander

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Charmander
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Charmander

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Charmander
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Charmander

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Charmander
        """

        return self.level

    def get_poke_name(self) -> str:
        """

        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Charmander

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Charmander
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Charmander

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Charmander
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """

        This method provides the current defence of a Charmander

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Charmander
        """

        return self.defence


class Charizard(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Charizard Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (None): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Charizard Class

        Parameters:
            None

        """

        PokemonBase.__init__(self, 15, 'Fire')
        self.name = 'Charizard'
        self.level = 3
        self.hp = 15
        self.attack_damage = 16
        self.speed = 12
        self.defence = 4
        self.evolved_version = None
        self.can_attack = True
        self.status = "free"
        self.id = 2
        self.max_speed = 12
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Charizard

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None


        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation

        """

        if damage > self.get_defence():
            self.lose_hp(2 * damage)
        else:
            self.lose_hp(damage)

    def level_up(self):
        """

        This method effectively levels up a Charizard (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 12 + (1*self.level)
            self.hp = self.max_hp - difference_hp
            self.attack_damage = 10 + (2*self.level)
            self.speed = 9+(1*self.level)
            self.max_speed = 9+(1*self.level)

    def get_hp(self) -> int:
        """
        This method provides the current hp of a Charizard

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Charizard
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Charizard

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Charizard
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Charizard

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Charizard
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Charizard

        Parameters:
            None
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Charizard

        Parameters:
            None
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Charizard

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Charizard
        """

        return self.defence


class Venusaur(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Venusaur Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (None): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Venusaur Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 21, 'Grass')
        self.name = 'Venusaur'
        self.level = 2
        self.hp = 21
        self.attack_damage = 5
        self.speed = 4
        self.defence = 10
        self.evolved_version = None
        self.can_attack = True
        self.status = "free"
        self.id = 4
        self.max_speed = 4
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Venusaur

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None


        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage > self.get_defence()+5:
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def level_up(self):
        """

        This method effectively levels up a Venasaur (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 20 + (self.level//2)
            self.hp = self.max_hp - difference_hp
            self.speed = 3+(self.level//2)
            self.max_speed = 3+(self.level//2)

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Venusaur

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Venasaur
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Venasaur

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Venasaur
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Venasaur

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Venasaur
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Venasaur

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Venasaur
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Venasaur

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Venasaur
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Venasaur

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Venasaur
        """

        return self.defence


class Bulbasaur(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Bulbasaur Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (Venasaur): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Bulbasaur Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 13, 'Grass')
        self.name = 'Bulbasaur'
        self.level = 1
        self.hp = 13
        self.attack_damage = 5
        self.speed = 7
        self.defence = 5
        self.evolved_version = Venusaur()
        self.can_attack = True
        self.status = "free"
        self.id = 3
        self.max_speed = 7
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Bulbasaur

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None


        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage > self.get_defence()+5:
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def level_up(self):
        """

        This method effectively levels up a Bulbasaur (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 12 + (1*self.level)
            self.hp = self.max_hp - difference_hp
            self.speed = 7 + (self.level//2)
            self.max_speed = 7 + (self.level//2)

    def get_hp(self):
        """

        This method provides the current hp of a Bulbasaur

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Bulbasaur
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Bulbasaur

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Bulbasaur
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Bulbasaur

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Bulbasaur
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Bulbasaur

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Bulbasaur
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Bulbasaur

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Bulbasaur
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Bulbasaur

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Bulbasaur
        """

        return self.defence


class Blastoise(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Blastoise Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (None): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Blastoise Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 21, 'Water')
        self.name = 'Blastoise'
        self.level = 3
        self.hp = 21
        self.attack_damage = 9
        self.speed = 10
        self.defence = 11
        self.evolved_version = None
        self.can_attack = True
        self.status = "free"
        self.id = 6
        self.max_speed = 10
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Blastoise

        Parameters:
            damage (int): An integer representing the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage > 2 * self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def level_up(self):
        """

        This method effectively levels up a Blastoise (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 15 + (2*self.level)
            self.hp = self.max_hp - difference_hp
            self.attack_damage = 8 + (self.level//2)
            self.defence = 8+(1*self.level)

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Blastoise

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Blastoise
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Blastoise

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Blastoise
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Blastoise

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Blastoise
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Blastoise

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Blastoise
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Blastoise

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Blastoise
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Blastoise

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Blastoise
        """

        return self.defence


class Squirtle(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Squirtle Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (Blastoise): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Squirtle Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 11, 'Water')
        self.name = 'Squirtle'
        self.level = 1
        self.hp = 11
        self.attack_damage = 4
        self.speed = 7
        self.defence = 7
        self.evolved_version = Blastoise()
        self.can_attack = True
        self.status = "free"
        self.id = 5
        self.max_speed = 7
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Squirtle

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage > 2*self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def level_up(self):
        """

        This method effectively levels up a Squirtle (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 9 + (2*self.level)
            self.hp = self.max_hp - difference_hp
            self.attack_damage = 4 + (self.level//2)
            self.defence = 6 + self.level

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Squirtle

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Squirtle
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Squirtle

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Squirtle
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Squirtle

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Squirtle
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Squirtle

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Squirtle
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Squirtle

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Squirtle
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Squirtle

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Squirtle
        """

        return self.defence


class Gengar(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Gengar Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (None): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Gengar Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 13, 'Ghost')
        self.name = 'Gengar'
        self.level = 3
        self.hp = 13
        self.attack_damage = 18
        self.speed = 12
        self.defence = 3
        self.evolved_version = None
        self.can_attack = True
        self.status = "free"
        self.id = 9
        self.max_speed = 12
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Gengar

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        self.lose_hp(damage)

    def level_up(self):
        """

        This method effectively levels up a Gengar (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 12 + (self.level // 2)
            self.hp = self.max_hp - difference_hp

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Gengar

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Gengar
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Gengar

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Gengar
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Gengar

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Gengar
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Gengar

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Gengar
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Gengar

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Gengar
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Gengar

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Gengar
        """

        return self.defence


class Haunter(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Haunter Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (Gengar): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Haunter Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 9, 'Ghost')
        self.name = 'Haunter'
        self.level = 1
        self.hp = 9
        self.attack_damage = 8
        self.speed = 6
        self.defence = 6
        self.evolved_version = Gengar()
        self.can_attack = True
        self.status = "free"
        self.id = 8
        self.max_speed = 6
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Haunter

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        self.lose_hp(damage)

    def level_up(self):
        """

        This method effectively levels up a Haunter (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 9 + (self.level // 2)
            self.hp = self.max_hp - difference_hp

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Haunter

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Haunter
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Haunter

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Haunter
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Haunter

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Haunter
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Haunter

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Haunter
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Haunter

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Haunter
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Haunter

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Haunter
        """

        return self.defence


class Gastly(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Gastly Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (Haunter): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Gastly Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 6, 'Ghost')
        self.name = 'Gastly'
        self.level = 1
        self.hp = 6
        self.attack_damage = 4
        self.speed = 2
        self.defence = 8
        self.evolved_version = Haunter()
        self.can_attack = True
        self.status = "free"
        self.id = 7
        self.max_speed = 2
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Gastly

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        self.lose_hp(damage)

    def level_up(self):
        """

        This method effectively levels up a Gastly (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.max_hp = 6 + (self.level // 2)
            self.hp = self.max_hp - difference_hp

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Gastly
        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Gastly
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Gastly

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Gastly
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Gastly

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Gastly
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Gastly

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Gastly
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Gastly

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Gastly
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of a Gastly

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Gastly
        """

        return self.defence


class Eevee(PokemonBase):
    """

    This is the class that effectively facilitates the functionality and specific attributes of a Eevee Pokemon

    Instance Attributes:
        name (str): A string giving the Pokemon's name
        level (int): An integer giving the Pokemon's level
        hp (int): An integer giving the hitpoints of the Pokemon
        attack_damage (int): An integer giving the Pokemon's attack damage
        speed (int): An integer giving the Pokemon's speed (mainly used for attack order)
        defence (int): An integer giving the Pokemon's defence
        evolved_version (None): An object representing the evolved version of the Pokemon
        status (str): A string representing the current status of the pokemon
        id (int): The ID of the Pokemon referring to its Pokedex order
        max_speed (int): An integer representing the maximum speed of a pokemon
        unique_id (int): An integer representing the unique id given to a pokemon

    """

    def __init__(self):
        """

        This is the constructor method of the Eevee Class

        Parameters:
            None
        """

        PokemonBase.__init__(self, 10, 'Normal')
        self.name = 'Eevee'
        self.level = 1
        self.hp = 10
        self.attack_damage = 7
        self.speed = 8
        self.defence = 5
        self.evolved_version = None
        self.can_attack = True
        self.status = "free"
        self.id = 10
        self.max_speed = 8
        self.unique_id = 0

    def defend(self, damage: int) -> None:
        """

        This method essentially runs the specific defence calculation for Eevee

        Parameters:
            damage (int): An integer represnting the damage inflicted on the Pokemon in question

        Returns:
            None

        Pre-Condition:
            A Pokemon has to have attacked another Pokemon

        Post-Condition:
            The Defending Pokemon loses damage according to its defence calculation
        """

        if damage >= self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(0)

    def level_up(self):
        """

        This method effectively levels up a Eevee  (meaning it increases it's level by 1 and increases its other attributes accordingly)

        Parameters:
            None

        Returns:
            None

        Pre-Condition:
            A Pokemon must have survived (not fainted) after a Battle

        Post-Condition:
            Pokemon's level attribute has to have incremented by 1 leading to an increase in relevent stats. The Pokemon can potentially evolve if their able to.
        """

        PokemonBase.level_up(self)
        if not self.should_evolve():
            difference_hp = self.max_hp - self.hp
            self.hp = self.max_hp - difference_hp
            self.attack_damage = 6 + self.level
            self.speed = 7 + self.level
            self.max_speed = 7 + self.level
            self.defence = 4 + self.level

    def get_hp(self) -> int:
        """

        This method provides the current hp of a Eevee

        Parameters:
            None

        Returns:
            self.hp (int): An integer representing the current hp of Eevee
        """

        return self.hp

    def get_status(self) -> str:
        """

        This method provides the current status of a Eevee

        Parameters:
            None

        Returns:
            self.status (str): A string representing the current status of Eevee
        """

        return self.status

    def get_level(self) -> int:
        """

        This method provides the current level of a Eevee

        Parameters:
            None

        Returns:
            self.level (int): An integer representing the current level of Eevee
        """

        return self.level

    def get_poke_name(self) -> str:
        """
        This method provides the name of the Pokemon

        Parameters:
            None

        Returns:
            self.name (str): A string representing the Pokemon's name
        """

        return self.name

    def get_speed(self) -> int:
        """

        This method provides the current speed of a Eevee

        Parameters:
            None

        Returns:
            self.speed (int): An integer representing the current speed of Eevee
        """

        return self.speed

    def get_attack_damage(self) -> int:
        """

        This method provides the current attack damage of a Eevee

        Parameters:
            None

        Returns:
            self.attack_damage (str): A string representing the current attack damage of a Eevee
        """

        return self.attack_damage

    def get_defence(self) -> int:
        """
        This method provides the current defence of an Eevee

        Parameters:
            None

        Returns:
            self.defence (str): An integer representing the current defence of Eevee
        """

        return self.defence


if __name__ == "__main__":

    # def check_evolution(pokemon:PokemonBase) -> PokemonBase:
    #    if pokemon.should_evolve():
    #        return pokemon.get_evolved_version()
    #    else:
    #        return pokemon
    c = Charmander()
    print(c)
    s = Squirtle()
    print(s)
    s.attack(c)
    print(c)
    s.attack(c)
    print(c)

    # print(c)
    # c.level_up()  # lv 2
    # c = c.check_evolution()
    # print(c)
    # c.level_up()  # lv 3
    # c = c.check_evolution()
    # print(c)
    # print(c)
    # s = Squirtle()
    # print(s)
    # s.level_up()
    # print(s)
    # s.level_up()
    # print(s)
    # s.level_up()
    # print(s)
    # s.attack(c)
    # s.attack(c)
    # print(c.status)
    # # print(c.is_fainted())
    # print(c.max_hp)
    # print(c.attack_damage)
    # print(c.speed)
    # print(c.defence)
    # print(c.burn)
    # print(c.poison)
    # print(c.paralysis)
    # print(c.sleep)
    # print(c.confusion)

    # self_win = false
#
    # if self_win == True:
