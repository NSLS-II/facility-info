from fastapi import APIRouter

router = APIRouter()

from .proposal_data import proposals

@router.get('/')
def get_all_proposals():
    return {'proposals': proposals}

@router.get('/{proposal_number}')
def get_proposal_number(proposal_number: int):
    return {'proposal': proposals[str(proposal_number)]}

@router.get('/user/{user_id}')
def get_by_user_id(user_id: int):
    user_id_str = str(user_id)
    all_proposals = []
    for proposal, proposal_info in proposals.items():
        if user_id in proposal_info['users']:
            all_proposals.append(proposal_info['proposal_number'])
    return {'proposals': all_proposals}
