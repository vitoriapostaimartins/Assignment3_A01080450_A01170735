"""
This module holds the PokemonAbility class and all of its functionalities.
"""

from pokeretriever.pokedex_object import PokedexObject


class PokemonAbility(PokedexObject):
    """
    This class represent a PokemonAbility Object and holds its attributes and methods.
    """

    def __init__(self, expanded, **kwargs):
        """
        Initialize a PokemonAbility object with an expanded flag and other attributes that compose effects and the
        pokemon.
        :param expanded: a bool
        :param kwargs: a dict
        """
        super().__init__(expanded, **kwargs)
        self._generation = kwargs.get("generation").get("name")
        self._effect = super().get_effect("effect", **kwargs)
        self._effect_short = super().get_effect("short_effect", **kwargs)
        self._pokemon = super().get_pokemon_names(**kwargs)

    @property
    def pokemon(self):
        """
        Get the pokemon in this object.
        :return: list of Strings
        """
        return self._pokemon

    def __str__(self):
        """
        Get a string that represents this PokemonAbility object.
        :return: a String
        """

        pokemon_str = ", ".join(self.pokemon)

        return f"Name: {self.name}\n" \
               f"ID: {self.id} \n" \
               f"Generation: {self._generation} \n" \
               f"Effect: {self._effect} \n" \
               f"Effect Short: {self._effect_short} \n" \
               f"Pokemon: {pokemon_str}\n"
