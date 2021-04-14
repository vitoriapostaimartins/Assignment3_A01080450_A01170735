import argparse
import os
from pathlib import Path

from facade import Facade, Request
from datetime import datetime


def main(request: Request):
    facade = Facade()

    pokedex_objects = facade.execute_request(request)
    handle_responses(pokedex_objects)


def handle_responses(pokedex_objects):
    now = datetime.now()
    data = f"Timestamp: {now.strftime('%d/%m/%Y %H:%M')}"

    data += f"\nNumber of requests: {len(pokedex_objects)}"
    no_of_request = 1
    for pokedex_object in pokedex_objects:
        data += f"\n\nRequest {no_of_request}"
        data += f"\n--------------------------"
        data += f"\n{pokedex_object}"
        no_of_request += 1

    _print_request(request, data)


def _print_request(request, data):
    if request.output != 'print':
        _print_to_file(request, data)
    else:
        print(data)


def _check_outputfile(file_extension):
    """
    Validate the file entered by a user.
    :param path: a string
    :param file_extension: a string
    :return: True if filename is valid, False otherwise
    """

    return file_extension == ".txt"


def _print_to_file(request, data):
    filename = request.output
    extension = os.path.splitext(filename)[1]
    if _check_outputfile(extension):
        with open(request.output, mode='w', encoding="utf-8") as data_file:
            data_file.write(data)
    else:
        print("Invalid output file. Please enter a text file or 'print' as the output.")


def parse_arguments() -> Request:
    parser = argparse.ArgumentParser()

    parser.add_argument("mode", choices=["pokemon", "ability", "move"])

    file_group = parser.add_mutually_exclusive_group()
    file_group.add_argument("--inputfile", help="The file that contains the names or ids of a pokemon, ability or move")
    file_group.add_argument("--inputdata", help='The string containing the name or id of a pokemon, ability or move')

    parser.add_argument("--expanded", action="store_true", help="If this flag is provided, certain attributes are "
                                                                "expanded with more information")

    parser.add_argument("--output", default="print", help="The output of the program. This is 'print' by "
                                                          "default, but can be set to a file name as well.")

    try:
        args = parser.parse_args()
        request = Request()
        request.mode = args.mode
        request.input_file = args.inputfile
        request.input_data = args.inputdata
        request.expanded = args.expanded
        request.output = args.output
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


if __name__ == '__main__':
    request = parse_arguments()
    main(request)
