from fastapi import APIRouter

router = APIRouter()

user_info_dict = {'jdoe':{'username': 'jdoe',
    'globus_email': 'jdoe@bnl.gov'}}

@router.get("/")
def get_all():
    all_info = []
    for name, info in user_info_dict.items():
        all_info.append(info)
    return all_info

@router.get("/search/{text}")
def get_by_search(text):
    results = []
    for user, info in user_info_dict.items():
        for field, value in info.items():
            if text == value:
                results.append(info)
    return results


