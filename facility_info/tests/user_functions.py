def select_from_calendar():
    pass

def select_from_list(items, field):
    selected = False
    while not selected:
        for i, item in enumerate(items.items()):
            print(f'Option {i}: {item[field]}')
        option = input('Enter an option (integer):')
        try:
            if int(option) > len(items) or int(option) < 0:
                print('Invalid option! Try again')
            else:
                selected = True
        except ValueError:
            selected = False
    return option

def select_experiment_from_proposals(items):
    selected = False
    proposal_expt_list = []
    while not selected:
        index = 1
        for proposal, experiment_dict in items.items():
            if experiment_dict:
                for value, experiment in enumerate(experiment_dict['experiments'], index):
                    print('Option: %s Proposal: %s Experiment: %s' % (value, proposal, experiment))
                    proposal_expt_list.append([proposal, experiment])
                index += len(experiment_dict['experiments'])
        option = input('Enter an option:')
        option = int(option)
        try:
            if int(option) > index or int(option) < 1:
                print('Invalid option! Try again')
            else:
                selected = True
        except ValueError:
            selected = False
    return proposal_expt_list[option-1]

def select_resource():
    pass

def render():
    pass

def check_within_experiment_time(current_time, experiment_start, experiment_end):
    if experiment_start > experiment_end:
        experiment_start, experiment_end = experiment_end, experiment_start
    if current_time > experiment_end or current_time < experiment_start:
        return False
