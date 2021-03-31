from pokeretriever.pokedex_object import PokedexObject


class PokemonStat(PokedexObject):
    def __init__(self, **kwargs):
        self._is_battle_only = kwargs.get("is_battle_only")
        super().__init__(**kwargs)


