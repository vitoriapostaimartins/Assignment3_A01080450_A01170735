from pokeretriever.pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    def __init__(self, expanded, **kwargs):
        super().__init__(expanded, **kwargs)
        self._height = kwargs.get("height")
        self._weight = kwargs.get("weight")
        self._stats = super().get_stats(**kwargs)
        self._types = super().get_types(**kwargs)
        self._abilities = super().get_abilities(**kwargs)
        self._moves = super().get_moves(**kwargs)


    def __str__(self):
        return f"Name: {self._name}\n"\
               f"Id: {self._id} \n" \
               f"Height: {self._height} decimetres\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Stats: {self._stats}\n" \
               f"Types: {self._types}\n" \
               f"Abilities: {self._abilities} \n" \
               f"Moves: {self._moves}"
