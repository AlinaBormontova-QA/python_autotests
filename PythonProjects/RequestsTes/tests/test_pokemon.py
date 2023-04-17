import requests
import pytest
 
URL = "https://pokemonbattle.me:9104/"
TOKEN='30fced6459e43646721ad846435fa888'

def test_status_code():
    response=requests.get(f'{URL}trainers', params={'trainer_id' : 3624})
    assert response.status_code == 200

def test_part_of_body():
    response=requests.get(f'{URL}trainers', params={'trainer_id' : 3624})
    assert response.json()['trainer_name'] == 'Alina'
