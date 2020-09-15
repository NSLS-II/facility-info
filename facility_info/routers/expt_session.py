from fastapi import APIRouter, HTTPException
import datetime

proposal = None
visit = None

router = APIRouter()

proposals = {'12345':{'users':['jdoe']}, '45678':{'users':['jdoe']}, '78901':{'users':['jdoe']}}
visits = {'12345':{'1':{'start_time':datetime.datetime(2020,11,1,9,0,0), 'end_time':datetime.datetime(2020,11,2,8,59,0)},
                   '2':{'start_time':datetime.datetime(2020,11,2,9,0,0), 'end_time':datetime.datetime(2020,11,3,8,59,0)},
                   '3':{'start_time':datetime.datetime(2020,11,3,9,0,0), 'end_time':datetime.datetime(2020,11,4,8,59,0)},
                   '4':{'start_time':datetime.datetime(2020,11,4,9,0,0), 'end_time':datetime.datetime(2020,11,5,8,59,0)},
                   '5':{'start_time':datetime.datetime(2020,11,5,9,0,0), 'end_time':datetime.datetime(2020,11,6,8,59,0)}}}
                   #TODO fill this out for other visits, including 45678, 78901, 13579
user_proposals = {'jdoe':['12345','45678','78901']} #this should be derived from proposals but hard-coded for now

@router.get("/")
def test():
    return {'test':'worked'}

@router.get("/user_proposals/{username}")
def get_user_proposals(username):
    return {'proposals':user_proposals.get(username, None)}

@router.get("/visits_for_proposal/{proposal}")
def get_visits_for_proposal(proposal: int):
    visits_for_proposal = set()
    for visit_str, times in visits[str(proposal)].items():
        visits_for_proposal.add(int(visit_str))
    print(visits_for_proposal)
    return {'visits': list(visits_for_proposal)}

@router.get("/times/{current_proposal}/{current_visit}")
def get_visit_times(current_proposal, current_visit):
    return visits.get(current_proposal, None).get(current_visit, None)

#there can only be one visit running at a time per beamline
@router.put("/visit/{current_proposal}/{current_visit}")
def set_visit(current_proposal, current_visit):
    global proposal, visit
    if current_proposal != proposal or current_visit != visit: #might want a message that visit is changing
        proposal = current_proposal
        visit = current_visit

@router.get("/visit") 
def get_visit():
    global proposal, visit
    return {'proposal': proposal, 'visit': visit}

@router.get('/users/{proposal}')
def get_users(proposal):
    return {'users': proposals[proposal]['users']}
