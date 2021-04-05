from pokeretriever.pokedex_object import PokedexObject


class PokemonStat(PokedexObject):
    def __init__(self, expanded, **kwargs):
        super().__init__(expanded, **kwargs)
        self._is_battle_only = kwargs.get("is_battle_only")



