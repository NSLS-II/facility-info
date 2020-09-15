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

def test_user_visits():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/expt_session/user_proposals/jdoe')
    a = response.json()
    assert a['proposals'][0] == '12345'

def test_visit_times():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/expt_session/times/12345/1')
    a = response.json()
    assert a['start_time'] == datetime.datetime(2020,11,1,9,0,0).isoformat('T')
    assert a['end_time'] == datetime.datetime(2020,11,2,8,59,0).isoformat('T')

def test_begin_session():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/expt_session/visit/13579/1')

def test_end_session():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/expt_session/visit')
    a = response.json()
    assert a['proposal'] == '13579'
    assert a['visit'] == '1'

def test_begin_session_again():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/expt_session/visit/12345/1')

def test_end_session():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/expt_session/visit')
    a = response.json()
    assert a['proposal'] == '12345'
    assert a['visit'] == '1'

def test_get_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/expt_session/users/12345')
    a = response.json()
    print(a)
    assert a['users'] == ['jdoe']
