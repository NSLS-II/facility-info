import datetime

experiments = {'12345':{'1':{'proposal_id':1, 'proposal_number':1, 'start_time':datetime.datetime(2020,11,1,9,0,0), 'end_time':datetime.datetime(2020,11,2,8,59,0), 'users':[1, 2, 3], 'beamline_id':2, 'experiment_id':1},
                   '2':{'proposal_id':1, 'proposal_number':2, 'start_time':datetime.datetime(2020,11,2,9,0,0), 'end_time':datetime.datetime(2020,11,3,8,59,0), 'users':[1], 'beamline_id':1, 'experiment_id':2},
                   '3':{'proposal_id':1, 'proposal_number':3, 'start_time':datetime.datetime(2020,11,3,9,0,0), 'end_time':datetime.datetime(2020,11,4,8,59,0), 'users':[1, 2], 'beamline_id':2, 'experiment_id':3},
                   '4':{'proposal_id':1, 'proposal_number':4, 'start_time':datetime.datetime(2020,11,4,9,0,0), 'end_time':datetime.datetime(2020,11,5,8,59,0), 'users':[1,3], 'beamline_id':1, 'experiment_id':4},
                   '5':{'proposal_id':1, 'proposal_number':5, 'start_time':datetime.datetime(2020,11,5,9,0,0), 'end_time':datetime.datetime(2020,11,6,8,59,0), 'users':[1], 'beamline_id':2, 'experiment_id':5}}}
                   #TODO fill this out for other experiments, including 45678, 78901, 13579
user_proposals = {'jdoe':{'12345':{'proposal_id':1},
                          '45678':{'proposal_id':2},
                          '78901':{'proposal_id':3}}} #this should be derived from proposals but hard-coded for now

safs = {'1':{'materials':[], 'safety_level':1, 'users':[1]},
       '2':{'materials':[], 'safety_level':2, 'users':[2]}}

