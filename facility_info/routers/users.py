from fastapi import APIRouter

router = APIRouter()

user_info_dict = {'jdoe':{'username': 'jdoe',
    'globus_email': 'jdoe@bnl.gov'}}

@router.get("/")
def get_all():
    all_names = []
    for name in user_info_dict.keys():
        all_names.append(name)
    return {'users':all_names}

@router.get("/search/{text}")
def get_by_search(text):
    results = []
    for user, info in user_info_dict.items():
        for field, value in info.items():
            if text == value:
                results.append(info)
    return results


