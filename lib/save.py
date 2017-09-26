from __future__           import print_function
import csv
from   datetime           import datetime
from   distutils.dir_util import mkpath
import re

def print_saving(filename):
    filename = filename[:17]
    line = 'Saving {0}...'.format(filename)
    print('  {0: <30}'.format(filename), end='')

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
        print(now.strftime('%m/%d/%Y at %H:%M:%S'))
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        mkpath(str(path / timestamp))
        time_path = path / timestamp
        vna.manual_sweep = True
        for i in vna.channels:
            channel  = vna.channel(i)
            filename = 'ch{1}'.format(timestamp, i)
            print_saving(filename)
            filename = str(time_path / filename)
            ports    = get_ports(vna, channel)
            channel.save_measurement_locally(filename, ports)
            print('DONE')
        for t in vna.traces:
            trace = vna.trace(t)
            markers = trace.markers
            if markers:
                filename = make_path_safe(trace.name)
                filename = '{0}_markers.csv'.format(filename)
                print_saving(filename)
                filename = time_path / filename
                with open(str(filename), 'w') as f:
                    csvwriter = csv.writer(f)
                    headers = ['Name']
                    headers.append('x ({0})'.format(trace.x_units()))
                    headers.append('y ({0})'.format(trace.y_units()))
                    csvwriter.writerow(headers)
                    for m in markers:
                        marker = trace.marker(m)
                        line = [marker.name, marker.x, marker.y]
                        csvwriter.writerow(line)
                print('DONE')
        for d in vna.diagrams:
            diagram = vna.diagram(d)
            filename = diagram.title
            if not filename:
                filename = 'Diagram{0}'.format(d)
            print_saving(filename)
            filename = make_path_safe(filename)
            filename = time_path / filename
            diagram.save_screenshot_locally(str(filename))
            print('DONE')
        print('  Current measurement interval complete!')
    return action
