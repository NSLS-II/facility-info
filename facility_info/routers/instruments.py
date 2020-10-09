from fastapi import APIRouter, HTTPException

instruments = {'1':{'port':'2ID', 'nickname':'SIX', 'instrument_id':1, 'emergency_contact':1, 'beamline_staff':[2,3,4], 'beamline phone numbers':[1602]},
               '2':{'port':'3ID', 'nickname':'HXN', 'instrument_id':2, 'emergency_contact':2, 'beamline_staff':[1,3,4], 'beamline_phone_numbers':[1603]}
}

router = APIRouter()

@router.get('/')
def get_all_instruments():
    print('instruments')
    to_return = []
    for instrument_id, instrument in instruments.items():
        to_return.append(instrument)
    return to_return

@router.get('/nickname/{nickname}')
def get_by_nickname(nickname: int):
    for id_string, instrument in instruments.items():
        if instrument['nickname'] == nickname:
            return instrument
    raise ValueError('Instrument nickname not found')

@router.get('/id/{instrument_id}')
def get_by_id(instrument_id: int):
    for id_string, instrument in instruments.items():
        if instrument['instrument_id'] == instrument_id:
            return instrument
    raise ValueError('Instrument_id not found')

