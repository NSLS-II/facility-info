import requests
import datetime
import json

HOSTNAME = 'localhost'
PORT = 6942

def test_all_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users')
    a = response.json()
    assert a[0]['username'] == 'jdoe'

def test_user_by_email():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users/search/jdoe@abc.com')
    a = response.json()
    assert a[0]['username'] == 'jdoe'

def test_user_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/user_proposals/jdoe')
    a = response.json()
    assert a['proposals']['12345']['proposal_id'] == 1

def test_get_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/experiments_in_proposal/12345')
    a = response.json()
    assert len(a['experiments']) == 5

def test_experiment_times():
    query = {'proposal_number': 12345, 'experiment_number': 1}
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/times', params=query)
    a = response.json()
    assert a['start_time'] == datetime.datetime(2020,11,1,9,0,0).isoformat('T')
    assert a['end_time'] == datetime.datetime(2020,11,2,8,59,0).isoformat('T')

def test_begin_experiment():
    query = {'proposal_number': 13579, 'experiment_number': 1}
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiments/create', params=query)

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/current')
    a = response.json()
    assert a['proposal'] == '13579'
    assert a['experiment'] == '1'

def test_begin_experiment_again():
    query = {'proposal_number': 12345, 'experiment_number': 1}
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiments/create', params=query)

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/current')
    a = response.json()
    assert a['proposal'] == '12345'
    assert a['experiment'] == '1'

def test_get_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/users/12345')
    a = response.json()
    assert a['users'] == ['jdoe']

def test_get_proposals():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/proposals')
    a = response.json()
    assert len(a['proposals']) == 3

def test_get_proposal():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/proposals/12345')
    a = response.json()
    assert a['proposal']['full_name'] == 'gu12345'
