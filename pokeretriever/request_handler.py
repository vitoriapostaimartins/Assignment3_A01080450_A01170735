"""
This module holds the RequestHandler class and all of its functionalities, as well as a custom exception class,
BadRequestError, and an Enum, PokedexModes. It also contains helper static methods.
"""

import asyncio
import enum
import os
import aiohttp
from pathlib import Path
from pokeretriever.pokedex_object_factory import PokedexObjectFactory, MoveFactory, AbilityFactory, PokemonFactory, \
    StatFactory


class PokedexTypes(enum.Enum):
    """
    Enum class that holds the types of Pokedex objects.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"


class BadRequestError(Exception):
    """
    Custom class that has the purpose of being thrown when there is a problem in the request being made.
    """

    def __init__(self):
        """
        Initialize a new BadRequestError instance and pass in a message with details of this error to the parent class,
        Exception.
        """
        super().__init__("An error occurred. Skipping this request.\n")


class RequestHandler:
    """
    Class that is responsible for making the requests to a specific API. In this program, we use the pokemon api.
    """

    @staticmethod
    async def get_pokedex_object(input: str, request, url: str, session: aiohttp.ClientSession):
        """
        Get the Pokedex object from the API via a GET request.
        :param input: name or id (a String or an int)
        :param request: a Request
        :param url: a String
        :param session: a ClientSession
        :return: a PokedexObject
        """

        target_url = url.format(request.mode, input)

        response = await session.request(method="GET", url=target_url)

        if response.status == 404:
            raise BadRequestError()

        json_dict = await response.json()

        # Get factory for mode passed in
        factory = RequestHandler.get_pokedex_factory(request.mode)

        return RequestHandler.make_pokedex_object(request.expanded, factory, **json_dict)

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

            # if response.status == '404':

            json_dict = await response.json()

            # Get factory for mode passed in
            factory = RequestHandler.get_pokedex_factory(type_of_pokedex)
            return RequestHandler.make_pokedex_object(True, factory, **json_dict)

    @staticmethod
    def make_pokedex_object(expanded, factory, **kwargs):
        """
        Make and return a new PokedexObject and personalize it according to the expanded flag, the factory of the
        PokedexObject and the dictionary that contains the attributes, kwargs.
        :param expanded: a bool
        :param factory: a PokedexFactory
        :param kwargs: a dict
        :return: a PokedexObject
        """
        pokedex_object = factory.create_pokedex_object(expanded, **kwargs)
        return pokedex_object

    @staticmethod
    def get_pokedex_factory(pokedex_type) -> PokedexObjectFactory:
        """
        Get a PokedexObject factory according to the type of object that we wish to get an instance of.
        :param pokedex_type: a PokedexTypes Enum item
        :return: a PokedexObjectFactory
        """
        pokedex_factories = {
            PokedexTypes.POKEMON.value: PokemonFactory(),
            PokedexTypes.ABILITY.value: AbilityFactory(),
            PokedexTypes.MOVE.value: MoveFactory(),
            PokedexTypes.STAT.value: StatFactory()
        }
        return pokedex_factories[pokedex_type]

    @staticmethod
    def execute_request(request) -> list:
        """
        Execute the given request and return the resulting PokedexObjects and errors if there are any.
        :param request: a Request
        :return: a list of PokedexObject objects and Errors (if there are any)
        """
        loop = asyncio.get_event_loop()

        # Process list of requests to get list of responses
        pokedex_objects = loop.run_until_complete(RequestHandler.process_requests(request))

        for pokedex_object in pokedex_objects:
            try:
                if pokedex_object.expanded:
                    loop.run_until_complete(RequestHandler.make_expanded_objects(pokedex_object))
            except AttributeError:
                continue

        return pokedex_objects

    @staticmethod
    async def make_expanded_objects(pokedex_object):
        """
        Make expanded objects for an object that has the expanded flag.
        Get the details from the objects that are expandable.
        :param pokedex_object: a PokedexObject
        """

        # query for abilities
        abilities = await RequestHandler.make_abilities(pokedex_object)

        # query for moves
        moves = await RequestHandler.make_moves(pokedex_object)

        # query for stats
        stats = await RequestHandler.make_stats(pokedex_object)

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
        async_coroutines = [RequestHandler.get_expanded_object(ability.get("url"), PokedexTypes.ABILITY.value) for
                            ability in pokedex_object.abilities]
        abilities = await asyncio.gather(*async_coroutines)
        return abilities

    @staticmethod
    async def make_moves(pokedex_object):
        """
        Make and return a list of moves and the details that are required when the object is expanded.
        :param pokedex_object: a PokedexObject
        :return: a list of dicts
        """
        async_coroutines = [RequestHandler.get_expanded_object(move.get("url"), PokedexTypes.MOVE.value) for move in
                            pokedex_object.moves]
        moves = await asyncio.gather(*async_coroutines)
        return moves

    @staticmethod
    async def make_stats(pokedex_object):
        """
        Make and return a list of stats and the details that are required when the object is expanded.
        :param pokedex_object: a PokedexObject
        :return: a list of dicts
        """
        async_coroutines = [RequestHandler.get_expanded_object(stat.get("url"), PokedexTypes.STAT.value) for stat in
                            pokedex_object.stats]
        stats = await asyncio.gather(*async_coroutines)
        return stats

    @staticmethod
    async def process_requests(request):
        """
        Read the request input and start the chain to process the request.
        Quit the program if no input data or file is found.
        :param request:
        :return:
        """
        inputs = []
        if request.input_data:
            inputs.append(request.input_data)
        elif request.input_file:
            inputs = RequestHandler.get_input_list(request)
        else:
            print("No input data or input file found. Please try again.")
            quit()

        url = "https://pokeapi.co/api/v2/{}/{}/"
        async with aiohttp.ClientSession() as session:
            print("Getting pokedex object...\n")

            # process each request
            async_coroutines = [RequestHandler.get_pokedex_object(input, request, url, session)
                                for input in inputs]

            responses = await asyncio.gather(*async_coroutines, return_exceptions=True)
            return responses

    @staticmethod
    def get_input_list(request) -> list:
        """
        Get lines of input from an input file as a list.
        :param request: a Request
        :return: a list
        """
        input = []
        filename = request.input_file
        extension = os.path.splitext(filename)[1]
        if RequestHandler.check_inputfile(filename, extension):
            with open(request.input_file, mode='r') as data_file:
                data = data_file.readlines()
            for i in data:
                input.append(i.rstrip("\n"))
        else:
            print("Invalid file. Please enter a existing text file.")
            quit()
        return input


    @staticmethod
    def check_inputfile(filepath, file_extension):
        """
        Check the if the filepath exists and if the provided file is a text file.
        :param filepath: a String
        :param file_extension: a String
        :return: True if the file is valid, False if it is not
        """
        if Path(filepath).exists():
            if file_extension == ".txt":
                return True
        return False
