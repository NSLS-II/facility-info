from fastapi import APIRouter

router = APIRouter()

from .user_data import user_info_dict

@router.get("/")
def get_all():
    all_info = []
    for name, info in user_info_dict.items():
        all_info.append(info)
    return all_info

@router.get("/me")
def get():
    return user_info_dict['me']

@router.get("/username/{username}")
def get_by_username(username):
    for user, info in user_info_dict.items():
        if info['username'] == username:
            return info

@router.get("/{text}")
def get_by_search(text):
    results = []
    for user, info in user_info_dict.items():
        for field, value in info.items():
            if text == value:
                results.append(info)
    return results


