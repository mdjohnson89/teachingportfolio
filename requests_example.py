import requests
name = input('What pokemon do you want? : ')
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')

pokemon_info = response.json()

name = pokemon_info.get('name')
weight = pokemon_info.get('weight')

print(name, weight)

