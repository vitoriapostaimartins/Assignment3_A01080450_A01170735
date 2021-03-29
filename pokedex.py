import argparse


def main(**some_args):
    print(some_args)
    print("in main: ", some_args["inputfile"])


def parse_arguments():
    parser = argparse.ArgumentParser()

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--pokemon", action="store_true")
    mode_group.add_argument("--ability", action="store_true")
    mode_group.add_argument("--move", action="store_true")

    file_group = parser.add_mutually_exclusive_group()
    file_group.add_argument("--inputfile", metavar='text')
    file_group.add_argument("--inputdata", metavar='text')

    parser.add_argument("--expanded", help="increase output verbosity",
                        action="store_true")

    parser.add_argument("--output", metavar="text")

    args = parser.parse_args()
    if args.expanded:
        print("expanded turned on")
    if args.inputfile:
        # Get the names or ids from an input file
        print(args.inputfile)
    return vars(args)



if __name__ == '__main__':
    arguments = parse_arguments()
    main(**arguments)
