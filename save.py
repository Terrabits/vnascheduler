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
		timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
		for i in vna.channels:
			channel = vna.channel(i)
			filename = '{0}_ch{1}'.format(timestamp, i)
			filename = str(path / filename)
			ports    = get_ports(vna, channel)
			channel.save_measurement_locally(filename, ports)
	return action
