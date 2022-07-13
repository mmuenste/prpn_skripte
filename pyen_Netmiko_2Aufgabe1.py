with open('devices.csv') as fobj1:
    with open('devices_nexus.csv', 'w') as fobj2:
        for line in fobj1:
            line_list = line.strip().split(';')
            if line_list[1] == 'cisco_nxos':
                print(line_list)
                print(';'.join(line_list), file=fobj2)
            elif line_list[0] == 'hostname':
                print(';'.join(line_list), file=fobj2)

