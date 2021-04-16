
Assignment 3
=====================

## How it works
The program will take in arguments to query for an item in Professor Oak's Pokedex.

To do this you can:
    - Enter your arguments in the command line
    - Specify your arguments in the run configuration for `pokedex.py`

### Formatting the arguments
As outlined in the Assignment 3 instructions document, the format of the arguments should
look like the following:
```
python3 pokedex.py {"pokemon" | "ability" | "move"} {--inputfile "filename.txt" | --inputdata "name or id"
[--expanded] [--output "f"]
```
If we are setting our args in `pokedex.py`'s run configurations, we can omit `python3 pokedex.py` from the config.

## Features
### Requirements as outlined in the assignment:
- 

### Error Handling
- handles:
    - Requests to an API endpoint that doesn't exist
        - e.g. entering a Pokemon name when we are querying for move/ability

#### Custom Exceptions
- **BadRequestError**
    - handles request to an invalid API endpoint
    

## References
Pokemon ASCII Art from: https://www.asciiart.eu/video-games/pokemon