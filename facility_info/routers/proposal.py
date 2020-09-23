from fastapi import APIRouter

router = APIRouter()

from .proposal_data import proposals

@router.get('/{proposal_number}')
def get_proposal_number(proposal_number: int):
    return {'proposal': proposals[str(proposal_number)]}
