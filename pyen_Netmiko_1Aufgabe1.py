from netmiko import ConnectHandler

ipaddress = '192.168.181.21'
user = 'admin'
passw = 'cisco'
device = 'cisco_nxos'

net_connect = ConnectHandler(ip=ipaddress,
                             username=user, password=passw, device_type=device)

cmd = net_connect.send_command('show version')
print(cmd)

net_connect.disconnect()
