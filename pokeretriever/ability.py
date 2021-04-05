from pokeretriever.pokedex_object import PokedexObject


class PokemonAbility(PokedexObject):

    def __init__(self, expanded, **kwargs):
        super().__init__(expanded, **kwargs)
        self._generation = kwargs.get("generation").get("name")
        self._effect = super().get_effect("effect", **kwargs)
        self._effect_short = super().get_effect("short_effect", **kwargs)
        self._pokemon = super().get_pokemon_names(**kwargs)


    def __str__(self):
        return f"Generation: {self._generation} \n" \
               f"Effect: {self._effect} \n" \
               f"Effect Short: {self._effect_short} \n" \
               f"Pokemon: {self._pokemon}"
