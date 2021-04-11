# Assignment 3 Checklist

##
- [x] Jeff's notes:
    - [x] mutually exclusive choices
    - [x] pick the first version in the list and store the level_learned_at from there

## Implementation Requirements
### Console Output
- [ ] format this to look better

### Parseing Arguments
- [x] input file
- [x] output file

### API Queries
- [x] Query for Pokemon Data
    - create a Pokemon object
    - only one that is expandable
- [x] Query for PokemonAbility Data
    - create a PokemonAbility object
- [x] Query for PokemonMove Data
    - create a PokemonMove object

### Expanded Arguments
- [x] query API for expanded

### Printing a Report
- [x] file
- [x] console
- [ ] format is nicely
- [x] append information from subqueries if expanded
- [ ] create a tuple out of key-value pairs
    - e.g. `Move name: move_value`
- [ ] output error if there is one

### Facade and Packages
- [x] group the following code in a `pokeretriever` package
    - create aiohttp session and execute requests
    - parse JSON and instantiate appropriate object
    - Pokemon, Ability, Move and Stat Classes
- [x] facade provides interface to `pokeretriever` package