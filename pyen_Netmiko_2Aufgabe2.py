from time import time
from netmiko import ConnectHandler

device_data = []
with open("devices_nexus.csv") as dev:
    for line in dev:
        d = {}
        line_list = line.strip().split(";")
        if line_list[0] == "hostname":
            continue
        d["device_type"] = line_list[1]
        d["ip"] = line_list[2]
        d["username"] = line_list[3]
        d["password"] = line_list[4]
        device_data.append(d)

for dev in device_data:
    with ConnectHandler(**dev) as net_connect:
        host = dev['ip']
        print(host, '... connected')
        config = net_connect.send_command('show run')
        # print(config)
    filename = host.replace(""_.", ") + '_' + str(time()) + '.config'
    with open(filename, 'w') as cfg_file:
        for line in config:
            cfg_file.write(line)
