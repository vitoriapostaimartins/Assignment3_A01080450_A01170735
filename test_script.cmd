ECHO write to screen
python pokedex.py --inputfile input_ability.txt ability
python pokedex.py --inputdata 2 move
python pokedex.py --inputdata 2 pokemon
python pokedex.py --inputfile input_move.txt move

ECHO write to file
python pokedex.py --inputfile input_move.txt --output output_move_test.txt move
python pokedex.py --inputfile input_ability.txt --output output_ability_test.txt ability
python pokedex.py --inputfile input_pokemon.txt --output output_test.txt pokemon

ECHO write to file expanded
python pokedex.py --inputfile input_pokemon.txt --output output_pokemon_expand_test.txt pokemon --expanded

ECHO error
python pokedex.py --inputfile input_error.txt --output output_error_test.txt move
