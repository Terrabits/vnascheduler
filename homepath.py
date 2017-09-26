from os.path import expanduser
from pathlib import Path

def expand_home_path(path):
	return Path(expanduser(path))
