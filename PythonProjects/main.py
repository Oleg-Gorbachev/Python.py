import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e7a24f010586020f6213e35af9e0a8e7'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Pyothon",
    "photo_id": 555
}

body_change_name = {
    "pokemon_id": "286414",
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "286414"
}

"""response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)"""

"""response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)"""

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)