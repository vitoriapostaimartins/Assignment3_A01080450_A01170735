import asyncio
import enum

import aiohttp

from pokeretriever.pokedex_object_factory import PokedexObjectFactory, MoveFactory, AbilityFactory, PokemonFactory, \
    StatFactory


class PokedexModes(enum.Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"


class RequestHandler:

    @staticmethod
    async def get_pokedex_object(input: str, request, url: str, session: aiohttp.ClientSession):
        """
        :param input: name or id
        :param request: a Request
        :param url:
        :param session:
        :return:
        """

        target_url = url.format(request.mode, input)

        response = await session.request(method="GET", url=target_url)

        json_dict = await response.json()

        # Get factory for mode passed in
        factory = RequestHandler.get_pokedex_factory(request.mode)
        # pokedex_object = factory.create_pokedex_object(request.expanded, **json_dict)
        # return pokedex_object

        return RequestHandler._make_pokedex_object(request.expanded, factory, **json_dict)

    @staticmethod
    async def get_expanded_object(url: str, mode) -> dict:
        """
        Retrieve a Pokemon from the pokeapi.
        :param poke_name:
        :param poke_id:
        :param url:
        :param session:
        :return:
        """
        async with aiohttp.ClientSession() as session:
            target_url = url

            response = await session.request(method="GET", url=target_url)

            json_dict = await response.json()

            # Get factory for mode passed in
            factory = RequestHandler.get_pokedex_factory(mode)
            return RequestHandler._make_pokedex_object(True, factory, **json_dict)

    @staticmethod
    def _make_pokedex_object(expanded, factory, **kwargs):
        pokedex_object = factory.create_pokedex_object(expanded, **kwargs)
        return pokedex_object

    @staticmethod
    def get_pokedex_factory(mode) -> PokedexObjectFactory:
        pokedex_factories = {
            PokedexModes.POKEMON.value: PokemonFactory(),
            PokedexModes.ABILITY.value: AbilityFactory(),
            PokedexModes.MOVE.value: MoveFactory(),
            PokedexModes.STAT.value: StatFactory()
        }
        return pokedex_factories[mode]

    @staticmethod
    def execute_request(request) -> list:
        loop = asyncio.get_event_loop()

        # Process list of requests to get list of responses
        pokedex_objects = loop.run_until_complete(RequestHandler.process_requests(request))

        for pokedex_object in pokedex_objects:
            if pokedex_object.expanded:
                loop.run_until_complete(RequestHandler.make_expanded_objects(pokedex_object))

        return pokedex_objects

    @staticmethod
    async def make_expanded_objects(pokedex_object):
        # abilities
        abilities = await RequestHandler.make_abilities(pokedex_object)

        # moves
        moves = await RequestHandler.make_moves(pokedex_object)

        # stats
        stats = await RequestHandler.make_stats(pokedex_object)

        pokedex_object.abilities = abilities
        pokedex_object.moves = moves
        pokedex_object.stats = stats
        print(str)

    @staticmethod
    async def make_abilities(pokedex_object):
        async_coroutines = [RequestHandler.get_expanded_object(ability.get("url"), PokedexModes.ABILITY.value) for ability in pokedex_object.abilities]
        abilities = await asyncio.gather(*async_coroutines)
        return abilities


    @staticmethod
    async def make_moves(pokedex_object):
        async_coroutines = [RequestHandler.get_expanded_object(move.get("url"), PokedexModes.MOVE.value) for move in pokedex_object.moves]
        moves = await asyncio.gather(*async_coroutines)
        return moves

    @staticmethod
    async def make_stats(pokedex_object):
        async_coroutines = [RequestHandler.get_expanded_object(stat.get("url"), PokedexModes.STAT.value) for stat in pokedex_object.stats]
        stats = await asyncio.gather(*async_coroutines)
        return stats

    @staticmethod
    async def process_requests(request):
        """

        :param request:
        :return:
        """
        inputs = []
        if request.input_data:
            inputs.append(request.input_data)
        else:
            inputs = RequestHandler.get_input_list(request)

        url = "https://pokeapi.co/api/v2/{}/{}/"
        async with aiohttp.ClientSession() as session:
            print("Getting pokemon")

            # process each request
            async_coroutines = [RequestHandler.get_pokedex_object(input, request, url, session)
                                for input in inputs]

            responses = await asyncio.gather(*async_coroutines)

            # for response in responses:
            #     print(response)
            return responses

    @staticmethod
    def get_input_list(request) -> list:
        """
        Get lines of input from an input file as a list.
        :param request:
        :return:
        """
        input = []
        with open(request.input_file, mode='r') as data_file:
            data = data_file.readlines()

        for i in data:
            input.append(i.rstrip("\n"))
        return input


