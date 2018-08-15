import subprocess
from datetime import datetime
import os
import time


filename = 'ping'
servers = [
    "172.16.1.104",
    "172.16.1.105",
    "172.16.1.108",
    "10.30.21.248",
    "10.13.1.241",
    "10.13.1.242",
    "10.13.1.243",
    "10.13.1.244",
    "10.13.1.245",
    "10.13.1.246",
    "10.13.1.247",
    "10.30.1.248"
]
results = []
for ip in servers:
    if os.path.isfile('{0}-{1}.txt'.format(filename, ip)):
        os.rename('{0}-{1}.txt'.format(filename, ip), '{0}-{2}-{1}.txt'.format(filename.split('.')[0], datetime.now().strftime('%d%m%Y_%H%M%S'),ip))

i = 0
while True:
    for ip in servers:
        dt = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        ping_result = subprocess.Popen("ping {} -n 1".format(ip), shell=True, stdout=subprocess.PIPE).stdout.read().split('data:')[1].split('Ping')[0].replace('\r\n', '')
        with open("{}".format('{0}-{1}.txt'.format(filename, ip)), "a") as file:
            file.write('timestamp: {1} ping to {0} result : {2} \r\n'.format(ip, dt, ping_result))
    time.sleep(1)
