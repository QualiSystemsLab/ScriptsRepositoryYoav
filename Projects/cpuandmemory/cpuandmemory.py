import subprocess
from datetime import datetime
import os
import time


filename = 'performance'
# servers = [
#     "172.16.1.104",
#     "172.16.1.105",
#     "172.16.1.108",
#     "10.30.21.248",
#     "10.13.1.241",
#     "10.13.1.242",
#     "10.13.1.243",
#     "10.13.1.244",
#     "10.13.1.245",
#     "10.13.1.246",
#     "10.13.1.247",
#     "10.30.1.248"
# ]

commands = [
    'wmic cpu get loadpercentage /format:value',
    'wmic os get freephysicalmemory /format:value',
    'wmic os get freevirtualmemory /format:value'
]
results = []
for command in commands:
    short_command = command.split('get ')[1].split(' /')[0]
    if os.path.isfile('{0}-{1}.txt'.format(filename, short_command)):
        os.rename('{0}-{1}.txt'.format(filename, short_command), '{0}-{2}-{1}.txt'.format(filename.split('.')[0], datetime.now().strftime('%d%m%Y_%H%M%S'),short_command))

i = 0
while True:
    for command in commands:
        short_command = command.split('get ')[1].split(' /')[0]
        dt = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        ping_result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().strip('\r\n')
        with open("{}".format('{0}-{1}.txt'.format(filename, short_command)), "a") as file:
            file.write('timestamp: {1} operation {0} result : {2} \r\n'.format(short_command, dt, ping_result))
    time.sleep(1)

