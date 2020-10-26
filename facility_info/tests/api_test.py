import requests
import datetime
import json

HOSTNAME = 'localhost'
PORT = 6943

def test_all_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users')
    a = response.json()
    assert a[0]['username'] == 'jdoe'

def test_user_me():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users/me')
    a = response.json()
    print(a)
    assert a['username'] == 'it_is_me'

def test_user_by_email():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users/email/asmith@nonexistent.gov')
    a = response.json()
    assert a['username'] == 'asmith'

def test_user_by_email():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/users/orcid/', params={'orcid':'https://orcid.org/0000-0002-1694-233X'})
    a = response.json()
    assert a['username'] == 'it_is_me'

def test_user_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/user_proposals/jdoe')
    a = response.json()
    assert a['proposals']['12345']['proposal_id'] == 1

def test_get_experiments():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/proposal/12345')
    a = response.json()
    assert len(a['experiments']) == 5

def test_experiment_times():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/times/12345/1')
    a = response.json()
    assert a[0] == datetime.datetime(2020,11,1,9,0,0).isoformat('T')
    assert a[1] == datetime.datetime(2020,11,2,8,59,0).isoformat('T')

def test_begin_experiment():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiments/create/13579/1')

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/')
    a = response.json()
    assert a['proposal'] == '13579'
    assert a['experiment'] == '1'

def test_begin_experiment_again():
    response = requests.put(f'http://{HOSTNAME}:{PORT}/experiments/create/12345/1')

def test_end_experiment():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/')
    a = response.json()
    assert a['proposal_id'] == '12345'
    assert a['experiment_id'] == '1'

def test_get_users():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/users/12345')
    a = response.json()
    assert a['users'] == [1]

def test_get_proposals():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/proposals')
    a = response.json()
    assert len(a['proposals']) == 3

def test_get_proposal():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/proposals/12345')
    a = response.json()
    assert a['proposal']['full_name'] == 'gu12345'

def test_current_facility():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/name')
    a = response.json()
    assert a == 'NSLS-II'

def test_calendar_2020_oct():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/calendar/1/2020/10')
    a = response.json()
    #27th - second shift - 26*6 + 1
    assert a[157] == 'O/M'
    #31st - last shift - 31*6
    assert a[183] == 'O'

def test_calendar_2020_nov():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/calendar/1/2020/11')
    a = response.json()
    #6th - third shift - 5*6 + 2
    assert a[32] == 'I'
    #18th - 5th shift - 17*6 + 4
    assert a[106] == 'M/S'
    #30st - last shift - 29*6 + 5
    assert a[179] == 'O'

def test_authorized():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/experiments/authorized/1')
    a = response.json()
    assert a == True

def test_monthly_calendar():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/calendar/1/2020/10/')
    a = response.json()
    assert a == ['D', 'D', 'D', 'D', 'D', 'D', #1
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D', #10
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'D', #17
                 'D', 'D', 'S', 'S', 'S', 'S',
                 'S', 'S', 'S', 'S', 'S', 'S',
                 'S', 'S', 'S', 'S', 'S', 'S', #20
                 'S', 'S', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O',
                 'O', 'O/M', 'M', 'M', 'M', 'M', #27
                 'M', 'M', 'M', 'M', 'M/S', 'S',
                 'S', 'S', 'O', 'O', 'O', 'O',
                 'O', 'O', 'O', 'O', 'O', 'O', #30
                 'O', 'O', 'O', 'O', 'O', 'O']


def test_daily_calendar():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/calendar/1/2020/10/29')
    a = response.json()
    assert a == ['S', 'S', 'O', 'O', 'O', 'O']

def test_shift_calendar():
    response = requests.get(f'http://{HOSTNAME}:{PORT}/facilities/calendar/1/2020/10/29/2')
    a = response.json()
    assert a == 'S'
