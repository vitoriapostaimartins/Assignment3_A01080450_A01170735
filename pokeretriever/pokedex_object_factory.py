"""
This module holds the factories that make PokedexObjects.
"""
import abc
import enum

from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.ability import PokemonAbility
from pokeretriever.move import PokemonMove
from pokeretriever.pokemon import Pokemon
from pokeretriever.stat import PokemonStat


class PokedexObjectFactory(abc.ABC):
    """
    This class represents a PokedexObjectFactory and it is responsible for holding functionalities to yield new
    instances of PokedexObject objects.
    """

    @abc.abstractmethod
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        """
        Create and return a new PokedexObject instance based on the expanded and kwargs arguments that are passed in.
        :param expanded: a bool
        :param kwargs: a dict
        :return: a PokedexObject
        """
        pass


class AbilityFactory(PokedexObjectFactory):
    """
    This class represents a AbilityFactory and it is responsible for holding functionalities to yield new
    instances of PokemonAbility objects.
    """
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        """
        Create and return a new PokemonAbility instance based on the expanded and kwargs arguments that are passed in.
        :param expanded: a bool
        :param kwargs: a dict
        :return: a PokemonAbility
        """
        return PokemonAbility(expanded, **kwargs)


class PokemonFactory(PokedexObjectFactory):
    """
    This class represents a PokemonFactory and it is responsible for holding functionalities to yield new
    instances of Pokemon objects.
    """
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        """
        Create and return a new Pokemon instance based on the expanded and kwargs arguments that are passed in.
        :param expanded: a bool
        :param kwargs: a dict
        :return: a Pokemon
        """
        return Pokemon(expanded, **kwargs)


class MoveFactory(PokedexObjectFactory):
    """
    This class represents a MoveFactory and it is responsible for holding functionalities to yield new
    instances of PokemonMove objects.
    """
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        """
        Create and return a new PokemonMove instance based on the expanded and kwargs arguments that are passed in.
        :param expanded: a bool
        :param kwargs: a dict
        :return: a PokemonMove
        """
        return PokemonMove(expanded, **kwargs)


class StatFactory(PokedexObjectFactory):
    """
    This class represents a StatFactory and it is responsible for holding functionalities to yield new
    instances of PokemonStat objects.
    """
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        """
        Create and return a new PokemonStat instance based on the expanded and kwargs arguments that are passed in.
        :param expanded: a bool
        :param kwargs: a dict
        :return: a PokemonStat
        """
        return PokemonStat(expanded, **kwargs)


class PokedexTypes(enum.Enum):
    """
    Enum class that holds the types of Pokedex objects.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"


def get_pokedex_factory(pokedex_type) -> PokedexObjectFactory:
    """
    Get a PokedexObject factory according to the type of object that we wish to get an instance of.
    :param pokedex_type: a PokedexTypes Enum item
    :return: a PokedexObjectFactory
    """
    pokedex_factories = {
        PokedexTypes.POKEMON.value: PokemonFactory(),
        PokedexTypes.ABILITY.value: AbilityFactory(),
        PokedexTypes.MOVE.value: MoveFactory(),
        PokedexTypes.STAT.value: StatFactory()
    }
    return pokedex_factories[pokedex_type]
