from pokeretriever.pokedex_object import PokedexObject


class PokemonMove(PokedexObject):

    def __init__(self, expanded, **kwargs):
        super().__init__(expanded, **kwargs)
        self._generation = kwargs.get("generation").get("name")
        self._accuracy = kwargs.get("accuracy")
        self._pp = kwargs.get("pp")
        self._power = kwargs.get("power")
        self._type = kwargs.get("type").get("name")
        self._damage_class = kwargs.get("damage_class").get("name")
        self._effect_short = super().get_effect("short_effect", **kwargs)


    def __str__(self):
        return f"\nName: {self._name} \n" \
               f"Generation: {self._generation} \n" \
               f"Accuracy: {self._accuracy} \n" \
               f"pp: {self._pp} \n" \
               f"Power: {self._power} \n" \
               f"Type: {self._type} \n" \
               f"Damage Class: {self._damage_class} \n" \
               f"Effect Short: {self._effect_short} \n"
