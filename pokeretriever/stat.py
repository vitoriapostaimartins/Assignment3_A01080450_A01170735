from pokeretriever.pokedex_object import PokedexObject


class PokemonStat(PokedexObject):
    def __init__(self, expanded, **kwargs):
        super().__init__(expanded, **kwargs)
        self._is_battle_only = kwargs.get("is_battle_only")
        self._move_damage_class = PokemonStat.get_move_damage_class(kwargs.get("move_damage_class"))

    @property
    def is_battle_only(self):
        return self._is_battle_only

    @property
    def move_damage_class(self):
        return self._move_damage_class

    @staticmethod
    def get_move_damage_class(move_damage_class):
        if move_damage_class:
            return move_damage_class.get("name")
        else:
            return "N/A"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Is Battle Only: {self.is_battle_only} \n" \
               f"Move Damage Class: {self.move_damage_class}\n"


