from fastapi import APIRouter

router = APIRouter()

from .proposal_data import proposals

@router.get('/')
def get_all_proposals():
    return {'proposals': proposals}
