import aiohttp

from pokeretriever import pokemon


class RequestHandler:

    async def get_pokedex_object(self, request: str, url: str, session: aiohttp.ClientSession) -> dict:
        """
        Retrieve a Pokemon from the pokeapi.
        :param poke_name:
        :param poke_id:
        :param url:
        :param session:
        :return:
        """

        target_url = url.format(request.mode, request.input_data)
        print(target_url)

        response = await session.request(method="GET", url=target_url)

        print("Response from aiohttp: \\n", response)

        json_dict = await response.json()
        return json_dict

    async def process_request(self, pokedex_object):
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
            response = await self.get_pokedex_object(pokedex_object, url, session)
            print(response)
            return response

