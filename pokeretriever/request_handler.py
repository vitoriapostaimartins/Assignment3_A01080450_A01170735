"""
This module holds the RequestHandler class and all of its functionalities, as well as a custom exception class,
BadRequestError, and an Enum, PokedexModes. It also contains helper static methods.
"""

import asyncio
import os
from pathlib import Path

import aiohttp

from pokeretriever.pokedex_object_factory import get_pokedex_factory


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

    def __init__(self, request):
        """
        Instantiate a RequestHandler with a request.
        :param request: a Request
        """
        self._request = request

    @property
    def request(self):
        return self._request

    async def _get_pokedex_object(self, input: str, url: str, session: aiohttp.ClientSession):
        """
        Get the Pokedex object from the API via a GET request.
        :param input: name or id (a String or an int)
        :param url: a String
        :param session: a ClientSession
        :return: a PokedexObject
        """

        target_url = url.format(self.request.mode, input)

        response = await session.request(method="GET", url=target_url)

        if response.status == 404:
            raise BadRequestError()

        json_dict = await response.json()

        # Get factory for mode passed in
        factory = get_pokedex_factory(self.request.mode)

        return RequestHandler.make_pokedex_object(self.request.expanded, factory, **json_dict)

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

    async def process_requests(self):
        """
        Read the request input and start the chain to process the request.
        Quit the program if no input data or file is found.
        :return:
        """
        inputs = []
        if self.request.input_data:
            inputs.append(self.request.input_data)
        elif self.request.input_file:
            inputs = self._get_input_list()
        else:
            print("No input data or input file found. Please try again.")
            quit()

        url = "https://pokeapi.co/api/v2/{}/{}/"
        async with aiohttp.ClientSession() as session:
            print("Getting pokedex object...\n")

            # process each request
            async_coroutines = [self._get_pokedex_object(input, url, session)
                                for input in inputs]

            responses = await asyncio.gather(*async_coroutines, return_exceptions=True)
            return responses

    def _get_input_list(self) -> list:
        """
        Get lines of input from an input file as a list.
        :return: a list
        """
        input = []
        filename = self.request.input_file
        extension = os.path.splitext(filename)[1]
        if RequestHandler.check_inputfile(filename, extension):
            with open(self.request.input_file, mode='r') as data_file:
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

