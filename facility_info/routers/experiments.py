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

@router.get("/experiments_in_proposal/{proposal}")
def get_experiments_for_proposal(proposal: int):
    experiments_for_proposal = set()
    for experiment_str, times in experiments[str(proposal)].items():
        experiments_for_proposal.add(int(experiment_str))
    return {'experiments': list(experiments_for_proposal)}

@router.get("/times")
def get_experiment_times(proposal_number, experiment_number):
    return experiments[proposal_number][experiment_number]

#there can only be one experiment running at a time per beamline
@router.put("/create")
def set_experiment(proposal_number, experiment_number):
    global proposal, experiment
    if proposal_number != proposal or experiment_number != experiment: #might want a message that experiment is changing
        proposal = proposal_number
        experiment = experiment_number

@router.get("/current")
def get_experiment():
    global proposal, experiment
    return {'proposal': proposal, 'experiment': experiment}

@router.get('/users/{proposal}')
def get_users(proposal):
    return {'users': proposals[proposal]['users']}
