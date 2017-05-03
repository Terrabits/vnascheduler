from os.path import expanduser
from pathlib import Path

def home_path():
	return Path(expanduser('~'))