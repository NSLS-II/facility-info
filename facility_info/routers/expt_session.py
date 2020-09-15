from fastapi import APIRouter, HTTPException
import datetime

visit = None

router = APIRouter()

proposals = {'12345':{'users':['jdoe']}, '45678':{'users':['jdoe']}, '78901':{'users':['jdoe']}}
user_proposals = {'jdoe':['12345','45678','78901']} #this should be derived from visits but hard-coded for now

@router.get("/")
def test():
    return {'test':'worked'}

@router.get("/user_proposals/{username}")
def get_user_proposals(username):
    return {'proposals':user_proposals.get(username, None)}

@router.get("/times/{current_visit}")
def get_visit_times(current_visit):
    visit_times = {'12345':{'start_time':datetime.datetime(2020,11,1,9,0,0),
                    'end_time':datetime.datetime(2020,11,2,8,59,0)}}
    return visit_times.get(current_visit,None)

#there can only be one visit running at a time per beamline
@router.put("/visit/{current_visit}")
def set_visit(current_visit):
    global visit
    if current_visit != visit: #might want a message that visit is changing
        visit = current_visit

@router.get("/visit") 
def get_visit():
    global visit
    return {'visit': visit}

@router.get('/users/{visit}')
def get_users(visit):
    return {'users': visits[visit]['users']}
