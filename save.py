from datetime           import datetime
from distutils.dir_util import mkpath

def get_ports(vna, channel):
    result = []
    for t_name in channel.traces:
        t = vna.trace(t_name)
        ports = t.test_ports()
        for i in ports:
            if not i in result:
                result.append(i)
    return sorted(result)

def create_save_action(vna, path):
	mkpath(str(path))
	def action():
		now = datetime.now()
		print(now)
		timestamp = now.strftime('%Y%m%d_%H%M%S')
        mkpath(str(path / timestamp))
        path      = path / timestamp
		for i in vna.channels:
			channel  = vna.channel(i)
			filename = 'ch{1}'.format(timestamp, i)
			print('  Saving {0}'.format(filename))
			filename = str(path / filename)
			ports    = get_ports(vna, channel)
			channel.save_measurement_locally(filename, ports)
        for t in vna.traces:
            trace = vna.trace(t)
            for m in trace.markers:
                marker = trace.marker(m)
                marker.name
                marker.x
                marker.y
            pass
        for d in vna.diagrams:
            # Save screenshot
            pass
	return action
