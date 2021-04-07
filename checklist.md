# Assignment 3 Checklist

##
- [ ] Jeff's notes:
    - [ ] mutually exclusive choices
    - [ ] pick the first version in the list and store the leve_learned_at from there

## Implementation Requirements
### Console Output
- [ ] format this to look better

### Parseing Arguments
- [x] input file
- [ ] output file

### API Queries
- [x] Query for Pokemon Data
    - create a Pokemon object
    - only one that is expandable
- [x] Query for PokemonAbility Data
    - create a PokemonAbility object
- [x] Query for PokemonMove Data
    - create a PokemonMove object

### Expanded Arguments
- [ ] query API for expanded

### Printing a Report
- [ ] file
- [ ] console
- [ ] format is nicely
- [ ] append information from subqueries if expanded
- [ ] create a tuple out of key-value pairs
    - e.g. `Move name: move_value`
- [ ] output error if there is one

### Facade and Packages
- [x] group the following code in a `pokeretriever` package
    - create aiohttp session and execute requests
    - parse JSON and instantiate appropriate object
    - Pokemon, Ability, Move and Stat Classes
- [] facade provides interface to `pokeretriever` package