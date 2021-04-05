import argparse
from facade import Facade, Request


def main(request: Request):
    facade = Facade()
    facade.execute_request(request)


def parse_arguments() -> Request:
    parser = argparse.ArgumentParser()

    # TODO figure out how to add mutually exclusive args without the --
    # mode_group = parser.add_mutually_exclusive_group()
    parser.add_argument("mode", choices=["pokemon", "ability", "move"])

    # mode_group.add_argument("pokemon", action="store_const", const="pokemon", help="The id or the name "
    #                                                                                             "of a pokemon.")
    # mode_group.add_argument("ability",  action="store_const", const="ability",  help="The id or the name "
    #                                                                                               "of an ability")
    # mode_group.add_argument("move",  action="store_const",  const="move",  help="The id or the name of a "
    #                                                                                         "pokemon move")

    file_group = parser.add_mutually_exclusive_group()
    file_group.add_argument("--inputfile", help="The file that contains the names or ids of a pokemon, ability or move")
    file_group.add_argument("--inputdata", help='The string containing the name or id of a pokemon, ability or move')
    print(f"file group {file_group}")

    parser.add_argument("--expanded", action="store_true", help="If this flag is provided, certain attributes are "
                                                                "expanded with more information")

    parser.add_argument("--output", default="print", help="The output of the program. This is 'print' by "
                                                          "default, but can be set to a file name as well.")

    try:
        args = parser.parse_args()
        print(f"args {args}")
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
