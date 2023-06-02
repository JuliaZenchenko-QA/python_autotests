import requests
import pytest

token = '485f2b6858f2cfab7a4857cea9c14ba4'

host='https://pokemonbattle.me:9104'

trainer_info=requests.get(f'{host}/trainers', 
                          params={'trainer_id': 4608})
print(trainer_info.text)

def test_status_code():
      answer = requests.post(f'{host}/pokemons', json=
                             {
      "name": "Мой покемон",
      "photo": "https://dolnikov.ru/pokemons/albums/004.png"
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
      assert answer.json()


def test_status_code():
      answer = requests.put(f'{host}/pokemons', json=
                             {
      "pokemon_id": "12482",
      "name": "New Name",
      "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
      assert answer.json() 


def test_status_code():
      answer = requests.post(f'{host}/trainers/add_pokeball', json=
                             {
      "pokemon_id": "12482"
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
      assert answer.json() 



    
