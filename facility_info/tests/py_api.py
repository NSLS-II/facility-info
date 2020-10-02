import requests
import json

HOST='localhost'
PORT=6942

def get_response_or_exception(response):
    if isinstance(response.json(), dict) and list(response.json().keys())[0]== 'detail':
        raise Exception('Failed API call')
    return response.json()

def two_digit_month(month):
    return str(int(month)).zfill(2)

def get_base_url(*args):
    return f'http://{HOST}:{PORT}/' + '/'.join(args)

def get_user_info(username):
    response = requests.get(get_base_url('users',username))
    return get_response_or_exception(response)

def get_user_proposals(userid):
    response = requests.get(get_base_url('proposals', 'user', str(userid)))
    return get_response_or_exception(response)

def get_experiments_for_proposal(proposalid):
    response = requests.get(get_base_url('experiments','proposal',str(proposalid)))
    try:
        return get_response_or_exception(response)
    except json.decoder.JSONDecodeError: #proposal defined but no experiments (yet?)
        return []

def get_facility_schedule(year, month):
    response = requests.get(get_base_url('facility','schedule',str(year), two_digit_month(month)))
    return get_response_or_exception(response)

def get_resource_calendar(resourceid, year, month):
    response = requests.get(get_base_url('resource',resourceid, str(year), two_digit_month(month)))
    return get_response_or_exception(response)

def set_experiment(proposalid, experiment):
    response = requests.put(get_base_url('experiments', 'create', str(proposalid), str(experiment)))
    return get_response_or_exception(response)

def get_experiment_times(proposalid, experiment):
    response = requests.get(get_base_url('experiments', 'times', str(proposalid), str(experiment)))
    return get_response_or_exception(response)

def get_current_experiment():
    response = requests.get(get_base_url('experiments', 'current'))
    print(response.json())
    return get_response_or_exception(response)

def get_experiment(experiment_id):
    response = requests.get(get_base_url('experiments', str(experiment_id)))
    return get_response_or_exception(response)

def get_resources(beamline_id):
    response = requests.get(get_base_url('resources', str(beamline_id)))
    return get_response_or_exception(response)
