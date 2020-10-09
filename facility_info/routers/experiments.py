from fastapi import APIRouter, HTTPException
import datetime

proposal = None
experiment = None

router = APIRouter()

from .proposal_data import proposals

from .experiment_data import experiments, user_proposals

@router.get("/user_proposals/{username}")
def get_user_proposals(username):
    return {'proposals':user_proposals.get(username, None)}

@router.get("/proposal/{proposal}")
def get_experiments_for_proposal(proposal: int):
    experiments_for_proposal = set()
    if str(proposal) in experiments:
        for experiment_str, times in experiments[str(proposal)].items():
            experiments_for_proposal.add(int(experiment_str))
        return {'experiments': list(experiments_for_proposal)}

@router.get("/times/{proposal_number}/{experiment_number}")
def get_experiment_times(proposal_number, experiment_number):
    expt_info = experiments[proposal_number][experiment_number]
    return expt_info['start_time'], expt_info['end_time']

#there can only be one experiment running at a time per beamline
@router.put("/create/{proposal_number}/{experiment_number}") #for testing! will be different in production
def set_experiment(proposal_number, experiment_number):
    global proposal, experiment
    if proposal_number != proposal or experiment_number != experiment: #might want a message that experiment is changing
        proposal = proposal_number
        experiment = experiment_number
    return experiment_number

@router.get('/{experiment_id}')
def get_experiment(experiment_id: int):
    experiment_list = []
    for proposal, experiment_num_and_info in experiments.items():
        for expt_num, expt_info in experiment_num_and_info.items():
            if expt_info['experiment_id'] == experiment_id:
                return expt_info
    return ValueError(f'Experiment_id {experiment_id} not found')

@router.get("/")
def get_experiment():
    global proposal, experiment
    return {'proposal_id': proposal, 'experiment_id': experiment}

@router.get('/users/{proposal}')
def get_users(proposal):
    return {'users': proposals[proposal]['users']}

@router.get('/authorized/{user_id}')
def get_is_authorized(user_id: int):
    if user_id in experiments[proposal][experiment]['users']:
        return True
    return False
