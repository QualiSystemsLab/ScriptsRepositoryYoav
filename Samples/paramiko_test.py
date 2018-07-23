import paramiko
import json
import jsonpickle
import sys

print sys.getrecursionlimit()

class JsonTransformer(object):
    def transform(self, myObject):
        return jsonpickle.encode(myObject, unpicklable=False)


hostname = '192.168.85.25'
username = 'root'
password = 'qs1234'
port = 22

t = paramiko.SSHClient()
t.load_system_host_keys()
t.set_missing_host_key_policy(paramiko.WarningPolicy())
t.connect(hostname=hostname, port=port, username=username, password=password)
t.exec_command('ls')
qq = jsonpickle.encode(t, unpicklable=False)

pass