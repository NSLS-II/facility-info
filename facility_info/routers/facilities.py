from fastapi import APIRouter, HTTPException
import datetime

router = APIRouter()

facility_dict = {'NSLS-II':{'facility_id':1, 'name':'NSLS-II'}}

shift_data = {'1':{'202010':{'shifts': ['D'] * 104 + ['S'] * 18 + ['O'] * 35 + ['O/M'] + ['M'] * 8 + ['M/S'] + ['S', 'S', 'S'] + ['O'] * 16},
              '202011':{'shifts': ['O'] * 32 + ['I'] * 2 + ['S'] * 16 + ['O'] * 47 + ['O/M'] + ['M'] * 8 + ['M/S'] + ['S'] * 3 + ['O'] * 36 + ['I'] * 2 + ['S'] * 28}
                }}

shifts = {}
for facility, shift_dict in shift_data.items():
    for yearmonth, shift_data_dict in shift_dict.items():
        year = yearmonth[:4]
        month = yearmonth[4:]
        for short_name, item in facility_dict.items():
            if item['facility_id'] == int(facility):
                facility_name = item['name']
        shifts[facility_name] = {}
        shifts[facility_name][year] = {}
        shifts[facility_name][year][month] = shift_data_dict['shifts']

@router.get("/calendar/{facility}/{year}/{month}")
def get_calendar(year: int, month: int):
    return shifts[facility_dict[int(facility)]][str(year)][str(month).zfill(2)]

@router.get('/name')
def get_facility():
    return facility_dict.keys()[0]

@router.get('/facility/{facilityID}/schedule')
def get_facility_schedule(facilityID):
    return shifts[facility_dict[int(facility)]]
