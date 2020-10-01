import requests

HOST='localhost'
PORT=6942

def get_response_or_exception(response):
    print(response.json())
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
    response = requests.get(get_base_url('proposals','byuser',str(userid)))
    return get_response_or_exception(response)

def get_experiments_for_proposal(proposalid):
    response = requests.get(get_base_url('experiments','byproposal',str(proposalid)))
    return get_response_or_exception(response)

def get_facility_schedule(year, month):
    response = requests.get(get_base_url('facility','schedule',str(year), two_digit_month(month)))
    return get_response_or_exception(response)

def get_resource_calendar(resourceid, year, month):
    response = requests.get(get_base_url('resource',resourceid, str(year), two_digit_month(month)))
    return get_response_or_exception(response)

def set_experiment(resourceid, proposalid, experiment):
    response = requests.put(get_base_url('resource', resourceid, proposalid, experiment))

def get_experiment_times(proposalid, experiment):
    response = requests.get(get_base_url('experiments', proposalid, experiment))
    return get_response_or_exception(response)

def get_experiment(resourceid):
    response = requests.get(get_base_url('experiments'))
    return get_response_or_exception(response)

def get_environments(resource):
    response = requests.get(get_base_url('environment'))
    return get_response_or_exception(response)


