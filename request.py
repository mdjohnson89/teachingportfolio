import requests

number = input('What number is the pokemon you\'re looking for?')
r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}/')

pokemon_info_all = r.json()

print(pokemon_info_all['forms'][0]['name'])

print(pokemon_info_all.get('forms')[0].get('name'))