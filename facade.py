import asyncio
import enum

import pokeretriever
from pokeretriever import request_handler
from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokedex_object_factory import PokedexObjectFactory, PokemonFactory, AbilityFactory, MoveFactory
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

    def execute_request(self, request: Request) -> PokedexObject:
        request_handler = RequestHandler()

        loop = asyncio.get_event_loop()

        response = loop.run_until_complete(request_handler.process_request(request))
        factory = self._get_pokedex_factory(request)
        print("factory: ", factory)
        pokedex_object = factory.create_pokedex_object(**response)
        print("\nPrinting Pokedex Object")
        print(pokedex_object)

    def _get_pokedex_factory(self, request) -> PokedexObjectFactory:
        pokedex_factories = {
            PokedexModes.POKEMON.value: PokemonFactory(),
            PokedexModes.ABILITY.value: AbilityFactory(),
            PokedexModes.MOVE.value: MoveFactory()
        }
        return pokedex_factories[request.mode]


class PokedexModes(enum.Enum):
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
