def select_from_calendar():
    pass

def select_from_list(items, field):
    selected = False
    while not selected:
        for i, item in enumerate(items.items()):
            print(item)
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

def select_resource():
    pass

def render():
    pass

def check_within_experiment_time(current_time, experiment_start, experiment_end):
    if experiment_start > experiment_end:
        experiment_start, experiment_end = experiment_end, experiment_start
    if current_time > experiment_end or current_time < experiment_start:
        return False
