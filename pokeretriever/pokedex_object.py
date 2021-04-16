"""
This module holds the PokemonObject class and all of its functionalities.
"""
import abc


class PokedexObject(abc.ABC):
    """
    This class represent a PokedexObject and holds its attributes and methods.
    """

    def __init__(self, expanded, **kwargs):
        """
        Initialize a PokedexObject object with an expanded flag and other attributes that compose the name and the
        id.
        :param expanded: a bool
        :param kwargs: a dict
        """
        # self.error = None
        self._name = kwargs.get("name")
        self._id = kwargs.get("id")
        self._expanded = expanded

    @property
    def name(self):
        """
        Get the name in this object.
        :return: a String
        :rtype:
        """
        return self._name

    @property
    def id(self):
        """
        Get the id in this object.
        :return: an int
        :rtype:
        """
        return self._id

    @property
    def expanded(self):
        """
        Get the expanded flag in this object.
        :return: a bool
        """
        return self._expanded

    @staticmethod
    def get_effect(effect_string, **kwargs) -> str:
        """
        Get the effect from the type of effect and a dictionary to initialize the effect in this object.
        :param effect_string: a String
        :param kwargs: a dict
        :return: a String
        """
        effect_entries = kwargs.get("effect_entries")
        english_entry = None
        for entry in effect_entries:
            if entry.get("language").get("name") == "en":
                english_entry = entry
        if english_entry is not None:
            return english_entry.get(effect_string)

    @staticmethod
    def get_pokemon_names(**kwargs):
        """
        Get pokemon names from a dictionary.
        :param kwargs: a dict
        :return: a list of Strings
        """
        pokemon_list = kwargs.get("pokemon")

        pokemon_names = []

        for pokemon in pokemon_list:
            pokemon_names.append(pokemon.get("pokemon").get("name"))

        return pokemon_names

    @staticmethod
    def get_types(**kwargs):
        """
        Get the types attribute from a dictionary.
        :param kwargs: a dict
        :return: a list Strings.
        """
        types_list = kwargs.get("types")
        type_names = []
        for request_type in types_list:
            type_names.append(request_type.get("type").get("name"))

        return type_names

    def get_stats(self, **kwargs):
        """
        Gets the name and base value for a Pokemon stat.
        :param kwargs: a dict
        :return: a list of dictionaries if this object is expanded, a list of tuples if it is not
        """
        stat_list = kwargs.get("stats")

        stats = []

        for stat in stat_list:
            name = stat.get("stat").get("name")
            base_value = stat.get("base_stat")
            url = stat.get("stat").get("url")
            if not self._expanded:
                stats.append((f"{name}", base_value))
            else:
                stats.append({"name": name, "base value": base_value, "url": url})
        return stats

    def get_abilities(self, **kwargs):
        """
        Get abilities from a dictionary.
        :param kwargs: a dict
        :return: a list of dictionaries if this object is expanded, a list of tuples if it is not.
        """
        ability_list = kwargs.get("abilities")

        abilities = []
        for ability in ability_list:
            name = ability.get("ability").get("name")
            url = ability.get("ability").get("url")

            if not self._expanded:
                abilities.append(f"{name}")
            else:
                abilities.append({"name": name, "url": url})

        return abilities

    def get_moves(self, **kwargs):
        """
        Get moves from a dictionary.
        :param kwargs: a dict
        :return: a list of dictionaries if this object is expanded, a list of tuples if this object is not expanded.
        """
        moves_list = kwargs.get("moves")

        moves = []

        for move in moves_list:
            name = move.get("move").get("name")
            url = move.get("move").get("url")
            level_learnt = move.get("version_group_details")[0].get("level_learned_at")
            if not self._expanded:
                moves.append((f"name: {name}", f"level_learnt: {level_learnt}"))
            else:
                moves.append({"name": name, "level_learnt": level_learnt, "url": url})

        return moves
