from fastapi import APIRouter, HTTPException

resources = {'1':{'instrument_id':1, 'resource_id':1, 'name':'eq1'},
             '2':{'instrument_id':2, 'resource_id':2, 'name':'eq2'}
}

router = APIRouter()

@router.get('/')
def get_all_resources():
    to_return = []
    for resource_id, resource in resources.items():
        to_return.append(resource)
    return to_return

@router.get('/instrument/{instrument_id}')
def get_by_instrument_id(instrument_id: int):
    in_resources = []
    for id_string, resource in resources.items():
        if resource['instrument_id'] == instrument_id:
            in_resources.append(resource)
    return in_resources

@router.get('/id/{resource_id}')
def get_by_id(resource_id: int):
    in_resources = []
    for id_string, resource in resource.items():
        if resource['resource_id'] == resource_id:
            in_resources.append(resource)
    return in_resources
