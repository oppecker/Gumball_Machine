import json
from Gumball import Gumball_Machine

def run_test(machine, test):
    print(f'Test Steps: {test}')
    levers = {
        'R':machine.red_lever,
        'Y':machine.yellow_lever,
        'C':machine.return_change_lever,
    }
    for step in test:
        print(f'Step: {step}')
        if step in levers:
            print(levers[step]())
        else:
            machine.input_currency(step)

if __name__ == '__main__':
    with open('tests.json') as json_file:
        tests = json.load(json_file)
        for title, test in tests.items():
            print(f'\n**** {title} ****')
            run_test(Gumball_Machine(), test)
