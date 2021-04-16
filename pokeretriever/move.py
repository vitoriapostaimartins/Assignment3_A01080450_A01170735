"""
This module holds the PokemonMove class and all of its functionalities.
"""
from pokeretriever.pokedex_object import PokedexObject


class PokemonMove(PokedexObject):
    """
    This class represent a PokemonMove Object and holds its attributes and methods.
    """

    def __init__(self, expanded, **kwargs):
        """
        Initialize a PokemonMove object with an expanded flag and other attributes that compose the generation,
        accuracy, pp, power, type, damage class and effect short.
        :param expanded: a bool
        :param kwargs: a dict
        """
        super().__init__(expanded, **kwargs)
        self._generation = kwargs.get("generation").get("name")
        self._accuracy = kwargs.get("accuracy")
        self._pp = kwargs.get("pp")
        self._power = kwargs.get("power")
        self._type = kwargs.get("type").get("name")
        self._damage_class = kwargs.get("damage_class").get("name")
        self._effect_short = super().get_effect("short_effect", **kwargs)

    def __str__(self):
        """
        Get a string that represents this PokemonMove object.
        :return: a String
        """
        return f"Name: {self.name} \n" \
               f"ID: {self.id} \n"\
               f"Generation: {self._generation} \n" \
               f"Accuracy: {self._accuracy} \n" \
               f"PP: {self._pp} \n" \
               f"Power: {self._power} \n" \
               f"Type: {self._type} \n" \
               f"Damage Class: {self._damage_class} \n" \
               f"Effect Short: {self._effect_short}\n"
