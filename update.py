import re
from urllib import request
from suffix import (gtld_suffix, nation_suffix, special_suffix)
__host_url = 'https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts'
try:
    response = request.urlopen(__host_url)
    page = response.read().decode('utf-8')
    lines = page.split('\n')
    names = set()
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            continue
        if line == '\n' or line == '':
            continue
        hosts = re.split('[\s\t]', line)
        name = hosts[1]
        keys = name.split('.')
        fulllist = ['*']
        if keys[len(keys) - 1] == 'localhost':
            continue
        if keys[len(keys) - 1] in nation_suffix and keys[len(keys) - 2] in gtld_suffix and keys[len(keys) - 2] not in special_suffix:
            fulllist.append(keys[len(keys) - 3])
            fulllist.append(keys[len(keys) - 2])
            fulllist.append(keys[len(keys) - 1])
        else:
            fulllist.append(keys[len(keys) - 2])
            fulllist.append(keys[len(keys) - 1])
        names.add('.'.join(fulllist))
    namearr = list(names)
    namearr.sort()
    print('[SwitchyOmega Conditions]')
    print('@with result')
    print('')
    for name in namearr:
        print(name+' +SS')
    print('')
    print('* +direct')
except IOError as e:
    print('Visit Github Failed')
