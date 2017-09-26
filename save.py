from   datetime           import datetime
from   distutils.dir_util import mkpath
import re

def make_path_safe(s):
    return re.sub('[/\\\\:\\*\\?"<>|]', '~', s)

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
        time_path = path / timestamp
        for i in vna.channels:
            channel  = vna.channel(i)
            filename = 'ch{1}'.format(timestamp, i)
            print('  Saving {0}'.format(filename))
            filename = str(time_path / filename)
            ports    = get_ports(vna, channel)
            channel.save_measurement_locally(filename, ports)
        for t in vna.traces:
            trace = vna.trace(t)
            if trace.markers:
                filename = make_path_safe(trace.name)
                filename = '{0}_markers.csv'.format(filename)
                filename = time_path / filename
                with open(str(filename), 'w') as f:
                    for m in trace.markers:
                        marker = trace.marker(m)
                        marker.name
                        marker.x
                        marker.y
        for d in vna.diagrams:
            # Save screenshot
            pass
    return action
