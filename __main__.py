#!/usr/bin/env python

from   homepath import home_path
from   pathlib  import Path
from   save     import create_save_action
import schedule
from   rohdeschwarz.instruments.vna import Vna
from   ruamel   import yaml

settings = {}
with open('settings.yaml', 'r') as f:
    settings = yaml.safe_load(f.read())

# Connect to VNA
vna = Vna()
vna.open_tcp(settings['vna address'])
vna.timeout_ms = 10*60*1000 # 10 mins

# Create lamdba function.
# Function will be called on interval
path = Path(settings['path'])
action = create_save_action(vna, path)

# run
interval = settings['interval (mins)']
duration = settings['duration (hrs)']
schedule.run(interval, duration, action)
