#!/usr/bin/env python

from   homepath import home_path
from   save     import create_save_action
import schedule
from   rohdeschwarz.instruments.vna import Vna

from pathlib import Path

# Settings:
interval_min    = 60
duration_hr     = 24 * 7
path            = Path('/your/path/here')
vna_address     = '127.0.0.1'

# Connect to VNA
vna = Vna()
vna.open_tcp(vna_address)
vna.timeout_ms = 10*60*1000 # 10 mins

# Create lamdba function.
# Function will be called on interval
action = create_save_action(vna, path)

# run
schedule.run(interval_min, duration_hr, action)
