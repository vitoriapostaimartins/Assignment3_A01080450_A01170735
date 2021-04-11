import abc


class PokedexObject(abc.ABC):

    def __init__(self, expanded, **kwargs):
        self._name = kwargs.get("name")
        self._id = kwargs.get("id")
        self._expanded = expanded

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def expanded(self):
        return self._expanded

    def get_effect(self, effect_string, **kwargs) -> str:
        effect_entries = kwargs.get("effect_entries")
        english_entry = None
        for entry in effect_entries:
            if entry.get("language").get("name") == "en":
                english_entry = entry
        if english_entry is not None:
            return english_entry.get(effect_string)
        # TODO throw error?

    def get_pokemon_names(self, **kwargs):
        pokemon_list = kwargs.get("pokemon")

        pokemon_names = []

        for pokemon in pokemon_list:
            pokemon_names.append(pokemon.get("pokemon").get("name"))

        return pokemon_names

    def get_stats(self, **kwargs):
        """
        Gets the name and base value for a Pokemon stat.
        :param kwargs:
        :return:
        """
        stat_list = kwargs.get("stats")

        stats = []

        for stat in stat_list:
            name = stat.get("stat").get("name")
            base_value = stat.get("base_stat")
            url = stat.get("stat").get("url")
            if not self._expanded:
                stats.append({"name": name, "base value": base_value})
            else:
                stats.append({"name": name, "base value": base_value, "url": url})
        return stats

    def get_abilities(self, **kwargs):
        ability_list = kwargs.get("abilities")

        abilities = []
        for ability in ability_list:
            name = ability.get("ability").get("name")
            url = ability.get("ability").get("url")

            if not self._expanded:
                abilities.append({"name": name})
            else:
                abilities.append({"name": name, "url": url})

        return abilities

    def get_moves(self, **kwargs):
        moves_list = kwargs.get("moves")

        moves = []

        for move in moves_list:
            name = move.get("move").get("name")
            url = move.get("move").get("url")
            level_learnt = move.get("version_group_details")[0].get("level_learned_at")
            if not self._expanded:
                moves.append({"name": name, "level_learnt": level_learnt})
            else:
                moves.append({"name": name, "level_learnt": level_learnt, "url": url})

        return moves

    def _get_move_object(self, url):
        pass

    def get_types(self, **kwargs):
        types_list = kwargs.get("types")
        type_names = []
        for type in types_list:
            type_names.append(type.get("type").get("name"))

        return type_names
