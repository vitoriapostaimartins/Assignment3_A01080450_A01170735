from pokeretriever.pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    def __init__(self, **kwargs):
        self._expanded = True
        self._height = kwargs.get("height")
        self._weight = kwargs.get("weight")
        self._stats = super().get_stats(**kwargs)
        self._types = super().get_types(self._expanded, **kwargs)
        self._abilities = super().get_abilities(**kwargs)
        self._moves = super().get_moves(**kwargs)
        super().__init__(**kwargs)

    def __str__(self):
        return f"Height: {self._height} decimetres\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Stats: {self._stats}\n" \
               f"Types: {self._types}\n" \
               f"Abilities: {self._abilities} \n" \
               f"Moves: {self._moves}"
