import requests

URL = "https://pokemonbattle.me:9104/"
TOKEN='30fced6459e43646721ad846435fa888'


response=requests.put(f'{URL}pokemons', headers={'trainer_token' : TOKEN}, json={
    "pokemon_id": "9300",
    "name": "Naz",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response.text)

response_add_pokeball=requests.post(f'{URL}trainers/add_pokeball', headers={'trainer_token' : TOKEN}, json={
    "pokemon_id": "9300"
})
print(response_add_pokeball.text)
