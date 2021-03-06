import sched
import time
from   lib.save import create_save_action

def run(interval_min, duration_hr, action):
	interval_s = interval_min * 60
	duration_s = duration_hr  * 60 * 60
	sheduler   = sched.scheduler(time.time, time.sleep)
	for i in range(0, duration_s, interval_s):
		sheduler.enter(i, 1, action, ())
	sheduler.run()
