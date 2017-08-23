
import sys, os
project_path = os.path.realpath(os.path.join(__file__, '../../'))
sys.path.append(project_path)

import pytoml as toml
from root import *

def do_travel(config):
    print(config)
    ag = Agent()
    if 'policy' not in config:
        return

    for tab_name in config['policy']:
        policy = config['policy'][tab_name]
        ag.add_policy(policy['name'])

    tm = TimeMachine()
    tm.set_agent(ag)

    tm.start(config['config']['date_begin'], config['config']['date_end'])

#
def travel(argv):
    if len(argv) < 2:
        print("len(argv) < 2")
        exit()

    file = os.path.join(os.path.dirname(__file__), 'conf', sys.argv[2])
    with open(file) as f:
        config = toml.load(f)
        do_travel(config)