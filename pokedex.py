"""
This module contains the main driver method, methods to parse arguments from the command line,
and methods to handle the output.
"""
import argparse
import os
from pokedex_facade import Facade, Request
from datetime import datetime


def main(request: Request):
    print(request)
    """
    Pass the request to a Facade and handle the PokedexObjects returned.
    :param request: a Request
    """
    print("""
                                  ,'\\
    _.----.        ____         ,'  _\\   ___    ___     ____
_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.
\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |
 \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
    -------------------------------------------------------------------
    """)
    facade = Facade()

    pokedex_objects = facade.execute_request(request)
    handle_responses(pokedex_objects)


def handle_responses(pokedex_objects):
    """
    Get the timestamp and count of the requests. Pass the data to
    the print_request method.
    :param pokedex_objects: a list of PokedexObjects
    """
    now = datetime.now()
    data = f"Timestamp: {now.strftime('%d/%m/%Y %H:%M')}"

    data += f"\nNumber of requests: {len(pokedex_objects)}\n"
    no_of_request = 1

    # Count the number of PokedexObjects as the number of requests
    for pokedex_object in pokedex_objects:
        data += f"\nRequest {no_of_request}"
        data += f"\n--------------------------"
        data += f"\n{pokedex_object}"
        no_of_request += 1

    _print_request(request, data)


def _print_request(request, data):
    """
    Check whether the data should be printed to a file or console.
    If output is to the console, print it. Else, pass it to the
    print_to_file method.
    :param request: a Request
    :param data: a string
    """
    if request.output != 'print':
        print_to_file(request, data)
        print(f"Printed Pokedex objects to: {request.output}")
    else:
        print(data)
        print("Finished printing Pokedex objects.")


def check_outputfile(file_extension):
    """
    Validate the file entered by a user.
    :param path: a string
    :param file_extension: a string
    :return: True if filename is valid, False otherwise
    """
    return file_extension == ".txt"


def print_to_file(request, data):
    """
    Print the data passed in to the output file specified in the request.
    Throw an error if the output file is invalid.
    :param request: a Request
    :param data: a string
    """
    filename = request.output
    extension = os.path.splitext(filename)[1]
    if check_outputfile(extension):
        with open(request.output, mode='w', encoding="utf-8") as data_file:
            data_file.write(data)
    else:
        print("Invalid output file. Please enter a text file or 'print' as the output.")


def parse_arguments() -> Request:
    """
    Parse the arguments that were entered in the command line
    and create a Request object from them.
    :return: a Request
    """

    # Construct an ArgumentParser and specify the arguments that will be parsed
    parser = argparse.ArgumentParser()

    parser.add_argument("mode", choices=["pokemon", "ability", "move"])

    file_group = parser.add_mutually_exclusive_group()
    file_group.add_argument("--inputfile", help="The file that contains the names or ids of a pokemon, ability or move")
    file_group.add_argument("--inputdata", help='The string containing the name or id of a pokemon, ability or move')

    parser.add_argument("--expanded", action="store_true", help="If this flag is provided, certain attributes are "
                                                                "expanded with more information")

    parser.add_argument("--output", default="print", help="The output of the program. This is 'print' by "
                                                          "default, but can be set to a file name as well.")

    # Create a Request object from the parsed arguments
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
