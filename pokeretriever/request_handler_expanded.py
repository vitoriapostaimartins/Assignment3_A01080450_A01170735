"""
Holds the ExpandedRequestHandler class, which is responsible for handling and managing objects from expanded requests.
"""

import asyncio
import aiohttp
from pokeretriever import request_handler
from pokeretriever.pokedex_object_factory import get_pokedex_factory, PokedexTypes
from pokeretriever.request_handler import RequestHandler


class ExpandedRequestHandler():
    """
    This class has helpful static methods that make and retrieve the expandable objects from a expanded request.
    """
    def __init__(self, request):
        self._request = request

    @staticmethod
    async def get_expanded_object(url: str, type_of_pokedex) -> dict:
        """
        Retrieve an expanded PokedexObject from the given url.
        :param url: a String
        :param type_of_pokedex: a PokemonTypes Enum item
        :return: a PokedexObject
        """
        async with aiohttp.ClientSession() as session:
            target_url = url

            response = await session.request(method="GET", url=target_url)

            if response.status == 404:
                raise request_handler.BadRequestError()

            json_dict = await response.json()

            # Get factory for type of pokedex object
            factory = get_pokedex_factory(type_of_pokedex)

            return RequestHandler.make_pokedex_object(True, factory, **json_dict)

    @staticmethod
    async def make_expanded_objects(pokedex_object):
        """
        Make expanded objects for an object that has the expanded flag.
        Get the details from the objects that are expandable.
        :param pokedex_object: a PokedexObject
        """

        # query for abilities
        abilities = await ExpandedRequestHandler.make_abilities(pokedex_object)

        # query for moves
        moves = await ExpandedRequestHandler.make_moves(pokedex_object)

        # query for stats
        stats = await ExpandedRequestHandler.make_stats(pokedex_object)

        # set data for expanded attributes
        pokedex_object.abilities = abilities
        pokedex_object.moves = moves
        pokedex_object.stats = stats

    @staticmethod
    async def make_abilities(pokedex_object):
        """
        Make and return a list of abilities and the details that are required when the object is expanded.
        :param pokedex_object: a PokedexObject
        :return: a list of dicts
        """
        async_coroutines = [ExpandedRequestHandler.get_expanded_object(ability.get("url"), PokedexTypes.ABILITY.value)
                            for ability in pokedex_object.abilities]
        abilities = await asyncio.gather(*async_coroutines)
        return abilities

    @staticmethod
    async def make_moves(pokedex_object):
        """
        Make and return a list of moves and the details that are required when the object is expanded.
        :param pokedex_object: a PokedexObject
        :return: a list of dicts
        """
        async_coroutines = [ExpandedRequestHandler.get_expanded_object(move.get("url"), PokedexTypes.MOVE.value) for
                            move in pokedex_object.moves]
        moves = await asyncio.gather(*async_coroutines)
        return moves

    @staticmethod
    async def make_stats(pokedex_object):
        """
        Make and return a list of stats and the details that are required when the object is expanded.
        :param pokedex_object: a PokedexObject
        :return: a list of dicts
        """
        async_coroutines = [ExpandedRequestHandler.get_expanded_object(stat.get("url"), PokedexTypes.STAT.value) for
                            stat in pokedex_object.stats]
        stats = await asyncio.gather(*async_coroutines)
        return stats
