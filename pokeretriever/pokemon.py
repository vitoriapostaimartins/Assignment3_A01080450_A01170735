"""
This module holds the Pokemon class and all of its functionalities.
"""
from pokeretriever.pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    """
    This class represent a Pokemon Object and holds its attributes and methods.
    """
    def __init__(self, expanded, **kwargs):
        """
        Initialize a Pokemon object with an expanded flag and other attributes that compose the height, weight, stats,
        types, abilities and moves.
        pokemon.
        :param expanded: a bool
        :param kwargs: a dict
        """
        super().__init__(expanded, **kwargs)
        self._height = kwargs.get("height")
        self._weight = kwargs.get("weight")
        self._stats = super().get_stats(**kwargs)
        self._types = super().get_types(**kwargs)
        self._abilities = super().get_abilities(**kwargs)
        self._moves = super().get_moves(**kwargs)

    @property
    def abilities(self):
        """
        Get the abilities list in this object.
        :return: a list
        """
        return self._abilities

    @abilities.setter
    def abilities(self, abilities):
        """
        Set the abilities list in this object.
        :param abilities: a list
        """
        self._abilities = abilities

    @property
    def moves(self):
        """
        Get the moves list in this object.
        :return: a list
        """
        return self._moves

    @moves.setter
    def moves(self, moves):
        """
        Set the moves list in this object.
        :param moves: a list
        """
        self._moves = moves

    @property
    def stats(self):
        """
        Get the stats list in this object.
        :return: a list
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Set the stats list in this object.
        :param stats: a list
        """
        self._stats = stats

    def __str__(self):
        """
        Get a string that represents this Pokemon object.
        :return: a String
        """
        abilities_str = "\n".join([str(ability) for ability in self.abilities])
        moves_str = "\n".join([str(move) for move in self.moves])
        stats_str = "\n".join([str(stat) for stat in self.stats])
        types = ", ".join(self._types)

        return f"\nName: {self._name}\n" \
               f"Id: {self._id} \n" \
               f"Height: {self._height} decimetres\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Types: {types}\n\n" \
               f"Stats:\n------\n{stats_str}\n\n" \
               f"Abilities:\n------\n{abilities_str} \n\n" \
               f"Moves:\n------\n{moves_str}"
