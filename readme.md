
Assignment 3
=====================

## How it works
The program will take in arguments to query for an item in Professor Oak's Pokedex.

To do this you can:
    - Enter your arguments in the command line
    - Specify your arguments in the run configuration for `pokedex.py`
    - Run a `.cmd` file, with multiple arguments specified.

### Formatting the arguments
As outlined in the Assignment 3 instructions document, the format of the arguments should
look like the following:
```
python pokedex.py {"pokemon" | "ability" | "move"} {--inputfile "filename.txt" | --inputdata "name or id"
[--expanded] [--output "f"]
```
If we are setting our args in `pokedex.py`'s run configurations, we can omit `python pokedex.py` from the config.

## Features
### Requirements as outlined in the assignment:
- Take input from console and parse arguments to make a Request
  - Take multiple inputs from a text file
- Call the pokeapi to get data for pokemon, ability, move, stats
    - Create corresponding PokedexObject for pokemon, ability, move data retrieved
    - Query for additional data if an `--expanded` flag is passed in
- Formatted report, printed to the console, or a text file
- Implement the Facade pattern in order to hide the complexity of making API calls and Pokedex objects.

### Error Handling
- handles:
    - Requests to an API endpoint that doesn't exist
        - e.g. entering a Pokemon name when we are querying for move/ability
    - Empty, missing, and invalid inputs for arguments that expect a value
    - Invalid/non-existent input file
    - Invalid extensions for output file
    
#### Custom Exceptions
- **BadRequestError**
    - handles request to an invalid API endpoint
    

## References
Pokemon ASCII Art from: https://www.asciiart.eu/video-games/pokemon