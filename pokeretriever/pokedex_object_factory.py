import abc

from pokeretriever.ability import PokemonAbility
from pokeretriever.move import PokemonMove
from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokemon import Pokemon
from pokeretriever.stat import PokemonStat


class PokedexObjectFactory(abc.ABC):

    @abc.abstractmethod
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        pass


class AbilityFactory(PokedexObjectFactory):

    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        return PokemonAbility(expanded, **kwargs)


class PokemonFactory(PokedexObjectFactory):

    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        return Pokemon(expanded, **kwargs)


class MoveFactory(PokedexObjectFactory):
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        return PokemonMove(expanded, **kwargs)


class StatFactory(PokedexObjectFactory):
    def create_pokedex_object(self, expanded, **kwargs) -> PokedexObject:
        return PokemonStat(expanded, **kwargs)
