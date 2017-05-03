from   homepath import home_path
import schedule
from   rohdeschwarz.instruments.vna import Vna

# Settings:
interval_min    = 60
duration_hr     = 24 * 7
path            = home_path() / 'Documents' / 'VnaScheduler'
vna_address     = '127.0.0.1'

# Connect to VNA
vna = Vna()
vna.open_tcp(vna_address)

# run
schedule.run(interval_min, duration_hr, vna, path)