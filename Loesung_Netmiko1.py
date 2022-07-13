from time import time
from netmiko import ConnectHandler
from credentials import username, password, ip, username2, password2, ip2

N9KV1 = {'device_type': 'cisco_nxos',
         'ip': ip,
         'username': username,
         'password': password}

N9KV2 = {'device_type': 'cisco_nxos',
         'ip': ip2,
         'username': username2,
         'password': password2}

DEVS = [N9KV1, N9KV2]

for dev in DEVS:
    net_connect = ConnectHandler(**dev)
    host = dev['ip']
    print(host, '... connected')
    config = net_connect.send_command('show run')
    # print(config)
    filename = host.replace(".", "_") + '_' + str(time()) + '.config'
    cfg_file = open(filename, 'w')
    for line in config:
        cfg_file.write(line)
    cfg_file.close()
    net_connect.disconnect()
