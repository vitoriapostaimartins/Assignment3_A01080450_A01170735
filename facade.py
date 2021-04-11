import asyncio
import enum

# from pokeretriever.pokedex_object import PokedexObject
# from pokeretriever.pokedex_object_factory import PokedexObjectFactory, PokemonFactory, AbilityFactory, MoveFactory
import os
import time
from datetime import datetime
from pathlib import Path

from pokeretriever.request_handler import RequestHandler


class Request:
    def __init__(self):
        self.pokemon = None
        self.ability = None
        self.move = None
        self.mode = None
        self.identifier = None
        self.input_file = None
        self.input_data = None
        self.expanded = None
        self.output = None

        def __str__(self):
            return f"Request: Pokemon: {self.pokemon}, Ability: {self.ability}" \
                   f", Move: {self.move}, Input file: {self.input_file}" \
                   f", Input Data: {self.input_data}, Expanded: {self.expanded}" \
                   f", Output: {self.output}"


class Facade:

    def execute_request(self, request: Request) -> list:
        request_handler = RequestHandler()
        pokedex_objects = request_handler.execute_request(request)

        now = datetime.now()
        data = f"Timestamp: {now.strftime('%d/%m/%Y %H:%M')}"

        data += f"\nNumber of requests: {len(pokedex_objects)}"
        no_of_request = 1
        for pokedex_object in pokedex_objects:
            data += f"\n\nRequest {no_of_request}"
            data += f"\n--------------------------"
            data += f"{pokedex_object}"
            no_of_request += 1

        self._print_request(request, data)
        return pokedex_objects

    def _print_request(self, request, data):
        if request.output != 'print':
            self._print_to_file(request, data)
        else:
            print(data)

    def _check_filename(self, filepath, file_extension, check_path):
        """
        Validate the file entered by a user.
        :param path: a string
        :param file_extension: a string
        :return: True if filename is valid, False otherwise
        """

        if not check_path or Path(filepath).exists():
            if file_extension == ".txt":
                return True
        return False

    def _print_to_file(self, request, data):
        filename = request.output
        extension = os.path.splitext(filename)[1]
        if self._check_filename(filename, extension, False):
            with open(request.output, mode='w', encoding="utf-8") as data_file:
                data_file.write(data)