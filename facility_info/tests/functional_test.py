# a mock-up of the expected workflow for a user attempting to collect data using a remote client

# instructions:
#    start API service with uvicorn --port 6942 facility_api.main:app
#    set up environment - pip install -r requirements.txt
#    python functional_test.py

import datetime
import py_api
from user_functions import select_from_calendar, select_from_list, select_resource, check_within_experiment_time , select_experiment_from_proposals#select_plan, render, send_globus_link

username = 'jdoe'
use_calendar = False
user_info = py_api.get_user_info(username)
#for now assume there is only one user that matches the username substring
user_info = user_info[0]
user_proposals = py_api.get_user_proposals(user_info['userid'])['proposals']
print(f'user {username} has proposals {user_proposals}')
user_proposals_experiments = {}
for proposal in user_proposals:
    user_experiments = py_api.get_experiments_for_proposal(proposal)
    if user_experiments:
        user_proposals_experiments[str(proposal)] = user_experiments
print(f'This user has experiments in the following user proposals: {user_proposals_experiments}')
if use_calendar:
    current_proposal, current_experiment = select_from_calendar(datetime.datetime.now().date(), py_api.get_facility_schedule(), py_api.get_resource_calendar(), user_proposals_experiments)
else:
    current_proposal, current_experiment = select_experiment_from_proposals(user_proposals_experiments)
print('setting current proposal and experiment to', current_proposal, current_experiment)
expt_id = py_api.set_experiment(current_proposal, current_experiment)
#beamline = py_api.get_beamline_from_experiment(current_proposal, current_experiment)
#maybe for this test, use a time within the experiment
print('Are we within the experiment time?', check_within_experiment_time(datetime.datetime.now(), py_api.get_experiment_times(current_proposal, current_experiment))) #heartbeat in applications? possibly with warnings if within x amount of time of finishing?
#expt_id = py_api.get_current_experiment() #TODO understand why this doesn't work
experiment = py_api.get_experiment(expt_id)
beamline_id = experiment['beamline_id']
beamline_info = py_api.get_beamline_info(beamline_id)
resources = py_api.get_resources(beamline_id)
if len(resources) > 1:
    selected_resource = select_resource(resources)
else:
    selected_resource = resources[0]
print('beamline:', beamline_info['nickname'], 'resources:', selected_resource['name'])
#plans = bluesky_plans.get_plans_for_resource(selected_resource) #is the resource what determines the plans?
#selected_plan = select_plan(plans)
#render(plan.rw_elements)
#send_globus_link(current_experiment, user_info.globus_email)
