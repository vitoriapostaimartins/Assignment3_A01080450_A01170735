import asyncio
import enum

# from pokeretriever.pokedex_object import PokedexObject
# from pokeretriever.pokedex_object_factory import PokedexObjectFactory, PokemonFactory, AbilityFactory, MoveFactory
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
        pokedex_objects = request_handler.execute_request(request) # list
        return pokedex_objects





