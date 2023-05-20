from __future__ import annotations
from audioop import alaw2lin
from os import access
from pokemon import Venusaur, Squirtle, Charizard, Gastly
from print_screen import print_game_screen
from poke_team import Action, PokeTeam, Criterion
from random_gen import RandomGen
"""

This file demonstrates the implementation of the Battle Class, a class that effectively runs a conflict/battle between two PokeTeams

September 2022
"""

__author__ = "Code by Daniel Liu, Ben Abraham, Johnny Ta, Bangze Han"

"""

All methods have a best/worst case time complexity O(1), constant time unless otherwise stated.

"""

# Some importated libraries needed to facilitate the creation/testing of the Battle Class


class Battle:
    """

    This class is an object represnting the "Battle" or conflict between two PokeTeams

    Instance Attributes:
        verbosity (int): An arbritary integer used for the print_game_screen method
    """

    def __init__(self, verbosity=0) -> None:
        """

        This is the constructor method for the Battle Class

        Parameters:
            verbosity (int): An abritary integer used for the print_game_screen method 
        """

        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """

        This is the Battle Method used for simulating a battle between two opposing PokeTeams

        Paramters:
            team1 (PokeTeam): A PokeTeam object representing one of the teams battling
            team2 (PokeTeam): A PokeTeam object representing another team that is battling

        Returns:
            integer (int): An integer that represents who won, 1 if team1 has won the battle, 2 for team2 and 0 if the battle resulted in a draw\

        Complexity analysis:
            Best case O(m * comp(==)) Where m is the number of pokemon in the smallest team
            Worst case O(n * comp(==)) Where n is the number of actions which are called
        """

        # retrieving the first Pokemon from team1's PokeTeam as per the Team battlemode's rules
        poke1 = team1.retrieve_pokemon()
        # retrieving the first Pokemon from team2's PokeTeam as per the Team battlemode's rules
        poke2 = team2.retrieve_pokemon()
        # Running a loop for as long as the Pokemon are not a NoneType (Meaning they are not fainted)
        while poke1 != None and poke2 != None:
            print_game_screen(poke1.get_poke_name(), poke2.get_poke_name(), poke1.get_hp(), poke1.max_hp, poke2.get_hp(
            ), poke2.max_hp, poke1.get_level(), poke2.get_level(), poke1.get_status(), poke2.get_status(), len(team1.team_adt), len(team2.team_adt))
            # Returns Action object -> This is team 1's pokemon action
            action1 = team1.choose_battle_option(poke1, poke2)
            # Returns Action object -> This is team 2's pokemon action
            action2 = team2.choose_battle_option(poke2, poke1)
            # If team1's action is none (either all pokemon have fainted or have tried to heal more than 3 times) team 2 wins
            if action1 == None:
                return 2
            # If team2's action is none (either all pokemon have fainted or have tried to heal more than 3 times) team 1 wins
            elif action2 == None:
                return 1

            # As per order in specification sheet, Swap Action is handled first
            # First checks if either Team has chosen Swap as their option
            if action1 == Action.SWAP or action2 == Action.SWAP:
                if action1 == Action.SWAP:  # Swap for Team 1
                    # Effectively returning current Pokemon (as per BattleMode Rules)
                    team1.return_pokemon(poke1)
                    # Effectively getting the next Pokemon (as per BattleMode Rules)
                    poke1 = team1.retrieve_pokemon()
                if action2 == Action.SWAP:  # Swap for Team 2
                    # Effectively returning current Pokemon (as per BattleMode Rules)
                    team2.return_pokemon(poke2)
                    # Effectively getting the next Pokemon (as per BattleMode Rules)
                    poke2 = team2.retrieve_pokemon()

            # As per order in specification sheet, Special Action is handled second
            # First checks whether or not either team ahs chosen special as their option
            if action1 == Action.SPECIAL or action2 == Action.SPECIAL:
                if action1 == Action.SPECIAL:  # If Team 1 has chosen special
                    # Returns current Pokemon to team adt
                    team1.return_pokemon(poke1)
                    team1.special()  # Utilizes the special method
                    poke1 = team1.retrieve_pokemon()  # Retrieves Pokemon as per battle mode rules
                if action2 == Action.SPECIAL:  # If Team 2 has chosen special
                    # Returns current Pokemon to team adt
                    team2.return_pokemon(poke2)
                    team2.special()  # Utilizes the special method
                    poke2 = team2.retrieve_pokemon()  # Retrieves Pokemon as per battle mode rules

            # As per the order in the specification sheet, The Heal Action is handled third
            if action1 == Action.HEAL or action2 == Action.HEAL:  # If either team has chosen heal as an action
                if action1 == Action.HEAL:  # If team 1 has chosen the heal action
                    poke1.heal()  # Healing team 1's current Pokemon
                if action2 == Action.HEAL:  # If team 2 has chosen the heal action
                    poke2.heal()  # Healing team 2's current Pokemon

            # As per the order in the specification sheet, The Heal Action is handled fourth
            # If either team 1 or 2 has chosen the Attack Option
            if action1 == Action.ATTACK or action2 == Action.ATTACK:
                # Boolean Variable depending on whether or not Team 1 has chosen to attack or not
                t1_attacked = False
                # Boolean Variable depending on whether or not Team 2 has chosen to attack or not
                t2_attacked = False
                if action1 == Action.ATTACK:  # If Team 1 has chosen to Attack
                    t1_attacked = True  # If Team 1 has chosen to Attack is True
                    if poke1.status == 'paralysis':  # First Checking if Paralysis status is held by Team1's Current Pokemon
                        # Setting Current Pokemon's Speed to its max speed integer divided by 2
                        poke1.speed = poke1.max_speed // 2
                if action2 == Action.ATTACK:  # If Team 2 has chosen to Attack
                    t2_attacked = True  # If the team 2 choosing to attack boolean variable is True
                    if poke2.status == 'paralysis':  # If the current Pokemon for Team 2 has a paralysis status
                        # Setting the current Pokemon's speed to it's max speed integer divided by 2
                        poke2.speed = poke2.max_speed // 2

                # Running the actual attack method
                # If Team 2 has chosen to attack and its current pokemon's speed exceeds the other team's current Pokemon
                if t2_attacked and poke2.get_speed() > poke1.get_speed():
                    # Team 2's current Pokemon attacks Team 1's current Pokemon
                    poke2.attack(poke1)
                if t1_attacked and not poke1.is_fainted():  # If Team 1 has chosen to Attack and Team 1 is not fainted
                    # Team 1's current Pokemon attacks Team 2's current Pokemon
                    poke1.attack(poke2)
                # If Team 2 has chosen to attack and Team 2's current Pokemon's speed is less than Team 1's Current Pokemon's speed and Team 2's Current Pokemon is not fainted
                if t2_attacked and poke2.get_speed() < poke1.get_speed() and not poke2.is_fainted():
                    # Team 2's current Pokemon attacks Team 1's current Pokemon
                    poke2.attack(poke1)
                if t2_attacked and poke2.get_speed() == poke1.get_speed():  # If team 2 has chosen to attack and team 2
                    # Team 2's current Pokemon attacks Team 1's current Pokemon
                    poke2.attack(poke1)

            if (not poke1.is_fainted()) and (not poke2.is_fainted()):  # This if they've both not fainted
                poke1.lose_hp(1)  # Team 1's Current Pokemon loses 1 hp
                poke2.lose_hp(1)  # Team 2's Current Pokemon loses 1 hp

            # If gastly, turn it into a haunter
            # If Team1's current Pokemon is a Gastly and it is not fainted
            if poke1.name == 'Gastly' and not poke1.is_fainted():
                poke1 = poke1.check_evolution()  # Evolving the Gastly to a Haunter
            # If Team2's current Pokemon is a Gastly and it is not fainted
            if poke2.name == 'Gastly' and not poke2.is_fainted():
                poke2 = poke2.check_evolution()  # Evolving the Gastly to a Haunter

            # If Team1's current pokemon is fainted while Team 2's current Pokemon is not fainted
            if (poke1.is_fainted()) and (not poke2.is_fainted()):
                poke2.level_up()  # Levelling up team 2's current Pokemon
                # Now check if poke2 can and should evolve, make it evolve
                poke2 = poke2.check_evolution()
                # Fainted Pokemon are returned -> Won't actually return
                # returning Team 1's current Pokemon
                team1.return_pokemon(poke1)
                if team1.is_empty():  # If Team 1's team is empty, ie all pokemon are fainted
                    poke1 = None  # Setting Team 1's current Pokemon as None
                else:
                    # Otherwise if there is still an unfainted pokemon, retrieve that Pokemon
                    poke1 = team1.retrieve_pokemon()
            # If Team2's current pokemon is fainted while Team 1's current Pokemon is not fainted
            elif (not poke1.is_fainted()) and (poke2.is_fainted()):
                poke1.level_up()  # Levelling up Team 1's current Pokemon
                # Now check if poke1 can and should evolve, make it evolve
                poke1 = poke1.check_evolution()
                # Fainted Pokemon are returned
                team2.return_pokemon(poke2)
                if team2.is_empty():  # If Team 2's entire team is fainted
                    poke2 = None  # Setting Team 2's current Pokemon to be None
                else:
                    # If not all fainted, Team 2 will retrieve its next Pokemon
                    poke2 = team2.retrieve_pokemon()
            # Otherwise if both Team 1 and Team 2's current pokemon are fainted
            elif (poke1.is_fainted()) and (poke2.is_fainted()):
                # Simply don't return either pokemon
                # If the length of the team 1's adt is equal to 0, meaning every Pokemon in the team is fainted
                if len(team1.team_adt) == 0:
                    poke1 = None  # Then Team 1's current Pokemon is set to equal None
                else:
                    # Getting the next next Pokemon if the team is not completely fainted
                    poke1 = team1.retrieve_pokemon()
                # If team 2's Team has a length of 0, ie all the Pokemon are fainted
                if len(team2.team_adt) == 0:
                    poke2 = None  # Setting Team 2's current Pokemon to equal None
                else:
                    # Otherwise if the team does have unfainted pokemon, retrieve the next pokemon as per battle mode rules
                    poke2 = team2.retrieve_pokemon()

            if poke1 == None and poke2 != None:  # If Team 1's current Pokemon is fainted and if Team 2's current Pokemon is not fainted
                # If team 2 wins, you should return the remaining pokemon on the field in team 2 back to team 2
                # Then return Team 2's current Pokemon
                team2.return_pokemon(poke2)
                return 2  # Thus, if team 2 wins, then the result integer is 2
            # If Team 1's current Pokemon is not fainted and Team 2's current Pokemon is fainted
            elif poke1 != None and poke2 == None:
                # If team 1 wins, you should return the remaining pokemon on the field in team 1 back to team 1
                team1.return_pokemon(poke1)
                return 1  # Result integer is 1 if Team 1 Wins
            elif poke1 == None and poke2 == None:  # If both Team's
                # If both teams are empty, no need to return anything as it won't actually return any pokemon
                return 0


if __name__ == '__main__':
    b = Battle()
    team1 = PokeTeam.random_team('Chen', 0, 6, ai_mode=PokeTeam.AI.RANDOM)
    team2 = PokeTeam.random_team('Chen', 1, 6, ai_mode=PokeTeam.AI.RANDOM)
    res = b.battle(team1, team2)
    print(res)
