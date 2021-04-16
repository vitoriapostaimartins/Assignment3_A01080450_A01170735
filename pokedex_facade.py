"""
This module holds the Request class, as well as the Facade class.
"""
import asyncio

from pokeretriever.request_handler import RequestHandler
from pokeretriever.request_handler_expanded import ExpandedRequestHandler


class Request:
    """
    This class represents a Request object and is responsible for holding the attributes of a command-line-argument
    request.
    """
    def __init__(self):
        """
        Initialize a Request object and all its member variables.
        Set the member variables to None at initialization.
        """
        self._mode = None
        self._identifier = None
        self._input_file = None
        self._input_data = None
        self._expanded = None
        self._output = None

    @property
    def mode(self):
        """
        Get the mode attribute in this Request.
        :return: a String
        """
        return self._mode

    @property
    def input_file(self):
        """
        Get the input file path in this Request.
        :return: a String
        """
        return self._input_file

    @property
    def input_data(self):
        """
        Get the input data in this Request.
        :return: a String
        """
        return self._input_data

    @property
    def expanded(self):
        """
        Get the expanded attribute in this Request.
        :return: a bool
        """
        return self._expanded

    @property
    def output(self):
        """
        Get the output method in this Request.
        :return: a String
        """
        return self._output

    @mode.setter
    def mode(self, value):
        """
        Set the mode attribute in this Request.
        :param value: a String
        """
        self._mode = value

    @input_file.setter
    def input_file(self, value):
        """
        Set the input file in this Request.
        :param value: a String
        """
        self._input_file = value

    @input_data.setter
    def input_data(self, value):
        """
        Set the input data attribute in this Request.
        :param value: a String
        """
        self._input_data = value

    @expanded.setter
    def expanded(self, value):
        """
        Set the expanded flag in this Request.
        :param value: a bool
        """
        self._expanded = value

    @output.setter
    def output(self, value):
        """
        Set the output method in this Request.
        :param value: a String
        """
        self._output = value


class Facade:
    """
    This class represents an object that serves as a front-facing interface.
    Its purpose is tpo hide the complexity of the program and provide a simple interface.
    """
    @staticmethod
    def execute_request(request: Request) -> list:
        """
        Execute a Request that is made by the User using a RequestHandler.
        :param request: a Request
        :return: a list of PokedexObject object
        """

        request_handler = RequestHandler(request)
        expanded_handler = ExpandedRequestHandler(request)

        loop = asyncio.get_event_loop()

        # Process list of requests to get list of responses
        pokedex_objects = loop.run_until_complete(request_handler.process_requests())

        for pokedex_object in pokedex_objects:
            try:
                if pokedex_object.expanded:
                    loop.run_until_complete(expanded_handler.make_expanded_objects(pokedex_object))
            except AttributeError:
                continue

        return pokedex_objects
