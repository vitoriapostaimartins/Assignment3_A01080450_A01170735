import asyncio
import enum

import aiohttp

from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokedex_object_factory import MoveFactory, AbilityFactory, PokemonFactory, PokedexObjectFactory


class PokedexModes(enum.Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class RequestHandler:

    async def get_pokedex_object(self, input: str, request, url: str, session: aiohttp.ClientSession) -> PokedexObject:
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
        factory = self.get_pokedex_factory(request)
        pokedex_object = factory.create_pokedex_object(request.expanded, **json_dict)
        return pokedex_object


    # async def get_pokedex_object(self, url: str) -> dict:
    #     """
    #     Retrieve a Pokemon from the pokeapi.
    #     :param poke_name:
    #     :param poke_id:
    #     :param url:
    #     :param session:
    #     :return:
    #     """
    #     async with aiohttp.ClientSession() as session:
    #         target_url = url
    #         print(target_url)
    #
    #         response = await session.request(method="GET", url=target_url)
    #
    #         print("Response from aiohttp: \\n", response)
    #
    #         json_dict = await response.json()
    #         return json_dict

    def get_pokedex_factory(self, request) -> PokedexObjectFactory:
        pokedex_factories = {
            PokedexModes.POKEMON.value: PokemonFactory(),
            PokedexModes.ABILITY.value: AbilityFactory(),
            PokedexModes.MOVE.value: MoveFactory()
        }
        return pokedex_factories[request.mode]

    def execute_request(self, request) -> list:
        loop = asyncio.get_event_loop()
        pokedex_objects = []

        # Process list of requests to get list of responses
        responses = loop.run_until_complete(self.process_requests(request))
        for r in responses:
            print("responses: ", r)

        return responses

    async def process_requests(self, request):
        """

        :param request:
        :return:
        """
        inputs = []
        if request.input_data:
            inputs.append(request.input_data)
        else:
            inputs = self.get_input_list(request)

        url = "https://pokeapi.co/api/v2/{}/{}/"
        async with aiohttp.ClientSession() as session:
            print("Getting pokemon")

            print(url)

            # process each request
            async_coroutines = [self.get_pokedex_object(input, request, url, session)
                                for input in inputs]

            responses = await asyncio.gather(*async_coroutines)

            for response in responses:
                print(response)
            return responses

    def get_input_list(self, request) -> list:
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
