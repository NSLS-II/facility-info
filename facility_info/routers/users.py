from typing import Optional

from fastapi import APIRouter, Query

router = APIRouter()

from .user_data import user_info_dict

def get_by_field(items, field, field_value):
    for user, info in items:
        print(field, info[field], field_value)
        if info[field] == field_value:
            return info

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
def get_by_username(username : str):
    return get_by_field(user_info_dict.items(), 'username', username)

@router.get("/email/{email}")
def get_by_email(email : str):
    return get_by_field(user_info_dict.items(), 'email', email)

@router.get("/orcid/")
def get_by_orcid(orcid : str):
    return get_by_field(user_info_dict.items(), 'orcid', orcid)
