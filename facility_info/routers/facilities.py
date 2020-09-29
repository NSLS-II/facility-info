from fastapi import APIRouter, HTTPException
import datetime

router = APIRouter()

shift_data = {'202010':{'shifts': ['D'] * 104 + ['S'] * 18 + ['O'] * 35 + ['O/M'] + ['M'] * 8 + ['M/S'] + ['S', 'S', 'S'] + ['O'] * 16},
              '202011':{'shifts': ['O'] * 32 + ['I'] * 2 + ['S'] * 16 + ['O'] * 47 + ['O/M'] + ['M'] * 8 + ['M/S'] + ['S'] * 3 + ['O'] * 36 + ['I'] * 2 + ['S'] * 28}
                }

shifts = {}
for yearmonth, shift_data_dict in shift_data.items():
    year = yearmonth[:4]
    month = yearmonth[4:]
    shifts[year] = {}
    shifts[year][month] = shift_data_dict['shifts']

@router.get("/calendar/{year}/{month}")
def get_calendar(year: int, month: int):
    return shifts[str(year)][str(month).zfill(2)]

@router.get('/name')
def get_facility():
    return {'facilityid':1, 'name':'NSLS-II'}

