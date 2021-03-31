import abc

from pokeretriever.ability import PokemonAbility
from pokeretriever.move import PokemonMove
from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokemon import Pokemon
from pokeretriever.stat import PokemonStat


class PokedexObjectFactory(abc.ABC):

    @abc.abstractmethod
    def create_pokedex_object(self, **kwargs) -> PokedexObject:
        pass


class AbilityFactory(PokedexObjectFactory):

    def create_pokedex_object(self, **kwargs) -> PokedexObject:
        return PokemonAbility(**kwargs)


class PokemonFactory(PokedexObjectFactory):

    def create_pokedex_object(self, **kwargs) -> PokedexObject:
        return Pokemon(**kwargs)


class MoveFactory(PokedexObjectFactory):
    def create_pokedex_object(self, **kwargs) -> PokedexObject:
        return PokemonMove(**kwargs)


class StatFactory(PokedexObjectFactory):
    def create_pokedex_object(self, **kwargs) -> PokedexObject:
        return PokemonStat(**kwargs)
