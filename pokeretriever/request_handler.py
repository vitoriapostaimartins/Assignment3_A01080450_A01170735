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
        print(target_url)

        response = await session.request(method="GET", url=target_url)

        print("Response from aiohttp: \\n", response)

        json_dict = await response.json()

        # Get factory for mode passed in
        factory = RequestHandler.get_pokedex_factory(request.mode)
        # pokedex_object = factory.create_pokedex_object(request.expanded, **json_dict)
        # return pokedex_object

        return RequestHandler._make_pokedex_object(request, factory, **json_dict)

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
            print(target_url)

            response = await session.request(method="GET", url=target_url)

            print("Response from aiohttp: \\n", response)

            json_dict = await response.json()

            # Get factory for mode passed in
            factory = RequestHandler.get_pokedex_factory(mode)
            return RequestHandler._make_pokedex_object(mode, factory, **json_dict)

    @staticmethod
    def _make_pokedex_object(request, factory, **kwargs):
        pokedex_object = factory.create_pokedex_object(request.expanded, **kwargs)
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
        pokedex_objects = []

        # Process list of requests to get list of responses
        responses = loop.run_until_complete(RequestHandler.process_requests(request))
        for r in responses:
            print("responses: ", r)

        return responses

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

            print(url)

            # process each request
            async_coroutines = [RequestHandler.get_pokedex_object(input, request, url, session)
                                for input in inputs]

            responses = await asyncio.gather(*async_coroutines)

            for response in responses:
                print(response)
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


