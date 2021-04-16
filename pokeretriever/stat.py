"""
This module contains the PokemonStat class.
"""
from pokeretriever.pokedex_object import PokedexObject


class PokemonStat(PokedexObject):
    """
    This class represent a PokemonStat Object and holds its attributes and methods.
    """
    def __init__(self, expanded, **kwargs):
        """
        Initialize a Pokemon stat object with an is_battle_only and move_damage_class attributes.

        :param expanded: a boolean
        :param kwargs: a dictionary
        """
        super().__init__(expanded, **kwargs)
        self._is_battle_only = kwargs.get("is_battle_only")
        self._move_damage_class = PokemonStat.get_move_damage_class(kwargs.get("move_damage_class"))

    @property
    def is_battle_only(self):
        """
        Get the is_battle_only attribute for this PokemonStat.
        :return: a boolean
        """
        return self._is_battle_only

    @property
    def move_damage_class(self):
        """
        Get the move_damage_class attribute for this PokemonStat.
        :return: a string
        """
        return self._move_damage_class

    @staticmethod
    def get_move_damage_class(move_damage_class):
        """
        Set the move_damage_class to the value passed in.
        :param move_damage_class: a string
        :return: a string
        """
        if move_damage_class:
            return move_damage_class.get("name")
        else:
            return "N/A"

    def __str__(self):
        """
        Return a string with the PokemonState name, id, is_battle_only
        and move_damage_class.
        :return: a string
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Is Battle Only: {self.is_battle_only} \n" \
               f"Move Damage Class: {self.move_damage_class}\n"
