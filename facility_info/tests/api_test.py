import requests
import datetime
import json

HOSTNAME = 'localhost'
PORT = 6942

def test_user_info():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/user_info/jdoe')
    a = response.json()
    assert a['username'] == 'jdoe'
    assert a['globus_email'] == 'jdoe@bnl.gov'

def test_all_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/user_info')
    a = response.json()
    assert a['users'] == ['jdoe']

def test_user_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/user_proposals/jdoe')
    a = response.json()
    assert a['proposals'][0] == '12345'

def test_get_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/experiments_for_proposal/12345')
    a = response.json()
    assert len(a['experiments']) == 5

def test_experiment_times():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/times/12345/1')
    a = response.json()
    assert a['start_time'] == datetime.datetime(2020,11,1,9,0,0).isoformat('T')
    assert a['end_time'] == datetime.datetime(2020,11,2,8,59,0).isoformat('T')

def test_begin_experiment():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiment/experiment/13579/1')

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/experiment')
    a = response.json()
    assert a['proposal'] == '13579'
    assert a['experiment'] == '1'

def test_begin_experiment_again():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiment/experiment/12345/1')

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/experiment')
    a = response.json()
    assert a['proposal'] == '12345'
    assert a['experiment'] == '1'

def test_get_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiment/users/12345')
    a = response.json()
    print(a)
    assert a['users'] == ['jdoe']
