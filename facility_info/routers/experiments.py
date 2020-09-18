from fastapi import APIRouter, HTTPException
import datetime

proposal = None
experiment = None

router = APIRouter()

#TODO consolidate with proposals dictionary in proposal
proposals = {'12345':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu12345'},
             '45678':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu45678'},
             '78901':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu78901'}}
experiments = {'12345':{'1':{'start_time':datetime.datetime(2020,11,1,9,0,0), 'end_time':datetime.datetime(2020,11,2,8,59,0)},
                   '2':{'start_time':datetime.datetime(2020,11,2,9,0,0), 'end_time':datetime.datetime(2020,11,3,8,59,0)},
                   '3':{'start_time':datetime.datetime(2020,11,3,9,0,0), 'end_time':datetime.datetime(2020,11,4,8,59,0)},
                   '4':{'start_time':datetime.datetime(2020,11,4,9,0,0), 'end_time':datetime.datetime(2020,11,5,8,59,0)},
                   '5':{'start_time':datetime.datetime(2020,11,5,9,0,0), 'end_time':datetime.datetime(2020,11,6,8,59,0)}}}
                   #TODO fill this out for other experiments, including 45678, 78901, 13579
user_proposals = {'jdoe':['12345','45678','78901']} #this should be derived from proposals but hard-coded for now

@router.get("/")
def test():
    return {'test':'worked'}

@router.get("/user_proposals/{username}")
def get_user_proposals(username):
    return {'proposals':user_proposals.get(username, None)}

@router.get("/experiments_in_proposal/{proposal}")
def get_experiments_for_proposal(proposal: int):
    experiments_for_proposal = set()
    for experiment_str, times in experiments[str(proposal)].items():
        experiments_for_proposal.add(int(experiment_str))
    print(experiments_for_proposal)
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
