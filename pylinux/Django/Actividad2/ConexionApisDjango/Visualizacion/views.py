import requests
from django.shortcuts import render

def get_first_20_pokemon(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_list = response.json().get('results', [])
        pokemon_details = []
        for pokemon in pokemon_list:
            pokemon_response = requests.get(pokemon['url'])
            if pokemon_response.status_code == 200:
                details = pokemon_response.json()
                pokemon_data = {
                    'name': details['name'],
                    'types': [type_info['type']['name'] for type_info in details['types']],
                    'abilities': [ability_info['ability']['name'] for ability_info in details['abilities']]
                }
                pokemon_details.append(pokemon_data)
        return render(request, 'pokemon_table.html', {'pokemon_details': pokemon_details})
    else:
        return render(request, 'pokemon_table.html', {'error': 'Could not retrieve Pokémon data'})
