from fastapi import APIRouter

router = APIRouter()

#TODO consolidate with proposals dictionary in experiments
proposals = {'12345':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu12345'},
             '45678':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu45678'},
             '78901':{'users':['jdoe'], 'prefix':'gu', 'full_name':'gu78901'}}

@router.get('/')
def get_all_proposals():
    return {'proposals': proposals}

@router.get('{proposal_number}')
def get_proposal_number(proposal_number):
    return {'proposal': proposals[proposal_number]}
