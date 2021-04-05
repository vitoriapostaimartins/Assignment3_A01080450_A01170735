import asyncio

import aiohttp

from pokeretriever import pokemon


class RequestHandler:

    async def get_pokedex_object(self, input: str, request, url: str, session: aiohttp.ClientSession) -> dict:
        """
        Retrieve a Pokemon from the pokeapi.
        :param poke_name:
        :param poke_id:
        :param url:
        :param session:
        :return:
        """


        target_url = url.format(request.mode, input)
        print(target_url)

        response = await session.request(method="GET", url=target_url)

        print("Response from aiohttp: \\n", response)

        json_dict = await response.json()
        return json_dict

    async def process_request(self, pokedex_object, input: str):
        """
        Process a single request
        :param pokemon:
        :param ability:
        :param move:
        :return:
        """
        url = "https://pokeapi.co/api/v2/{}/{}/"
        async with aiohttp.ClientSession() as session:
            print("Getting pokemon")

            # make get request here
            response = await self.get_pokedex_object(input, pokedex_object, url, session)
            print(response)
            return response

    async def process_requests(self, request):
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
        input =[]
        with open(request.input_file, mode='r') as data_file:
             data = data_file.readlines()

        for i in data:
            input.append(i.rstrip("\n"))
        return input
