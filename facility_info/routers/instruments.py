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

@router.get('/{nickname}')
def get_by_nickname(nickname):
    for instrument in instruments:
        if instrument['nickname'] == nickname:
            return instrument
    raise ValueError('Instrument nickname not found')
