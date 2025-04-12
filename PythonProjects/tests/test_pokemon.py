import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e7a24f010586020f6213e35af9e0a8e7'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '29015'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
 
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'handler'

