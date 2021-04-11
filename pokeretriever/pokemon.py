import asyncio

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

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, abilities):
        self._abilities = abilities

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, moves):
        self._moves = moves

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, stats):
        self._stats = stats

    def __str__(self):
        abilities_str = "\n".join([str(ability) for ability in self.abilities])
        moves_str = " \n".join([str(move) for move in self.moves])
        stats_str = "\n".join([str(stat) for stat in self.stats])
        types = ", ".join(self._types)

        return f"\nName: {self._name}\n" \
               f"Id: {self._id} \n" \
               f"Height: {self._height} decimetres\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Types: {types}\n" \
               f"Stats: {stats_str}\n" \
               f"Abilities: {abilities_str} \n" \
               f"Moves: {moves_str}"
