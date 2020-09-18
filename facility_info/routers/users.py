from fastapi import APIRouter

router = APIRouter()

user_info_dict = {'jdoe':{'username': 'jdoe',
    'globus_email': 'jdoe@bnl.gov'}}

@router.get("/")
def get_all_usernames():
    all_names = []
    for name in user_info_dict.keys():
        all_names.append(name)
    return {'users':all_names}
