from pokeretriever.pokedex_object import PokedexObject


class PokemonMove(PokedexObject):
    def __init__(self, **kwargs):
        self._generation = kwargs.get("generation").get("name")
        self._accuracy = kwargs.get("accuracy")
        self._pp = kwargs.get("pp")
        self._power = kwargs.get("power")
        self._type = kwargs.get("type")
        self._damage_class = kwargs.get("damage_class")
        self._effect_short = super().get_effect("short_effect", **kwargs)
        super().__init__(**kwargs)

    def __str__(self):
        return f"Name: {self._name}, " \
               f"Generation: {self._generation}, " \
               f"Accuracy: {self._accuracy}, " \
               f"pp: {self._pp}, " \
               f"Power: {self._power}, " \
               f"Type: {self._type}, " \
               f"Damage Class: {self._damage_class}, " \
               f"Effect Short: {self._effect_short}"
