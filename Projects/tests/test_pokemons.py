import requests
import pytest

token = '485f2b6858f2cfab7a4857cea9c14ba4'

host = 'https://pokemonbattle.me:9104'

def test_status_code():
      answer_body=requests.get(f'{host}/trainers', params={'trainer_id' : 4608})  
      assert answer_body.status_code == 200

def test_part_of_answer():
      answer_body=requests.get(f'{host}/trainers', params={'trainer_id' : 4608})
      assert answer_body.json()['trainer_name']== 'Tina'     

@pytest.mark.parametrize('key,value', [('trainer_name', 'Tina'),
                                        ('city', 'Benedorm'),
                                          ('get_history_battle', '0'),
                                            ('level', '1')])

def test_parts_of_answer(key, value):
      answer=requests.get(f'{host}/trainers', params={'trainer_id' : 4608})
      assert answer.json()[key]== value    
 