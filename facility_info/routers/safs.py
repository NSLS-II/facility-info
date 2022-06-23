from fastapi import APIRouter

from .saf_data import safs

router = APIRouter()

@router.get("/")
def get_all():
    all_info = []
    for name, info in safs.items():
        all_info.append(info)
    return all_info

@router.get("/{saf_id}")
def get_by_search(saf_id: int):
    for safs_saf_id, info in safs.items():
        if int(safs_saf_id) == saf_id:
            return info

@router.get('/experiment/{experiment_id}')
def get_by_experiment(experiment_id: int):
    for saf_id, info in safs.items():
        if info['experiment_id'] == experiment_id:
            return info
