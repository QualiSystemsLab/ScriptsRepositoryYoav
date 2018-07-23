import cloudshell.api.cloudshell_api as api_7
import os
import re

class entry():
    def __init__(self):
        self.datetime = ''
        self.type_om = ''
        self.data = ''
        self.filename = ''

username = 'admin'
password = 'admin'
server_7 = 'qs.cisco.com'
N_domain = 'Global'

resid = 'e11459e3-71f2-451f-8f72-9156e341ed04'

session_7 = api_7.CloudShellAPISession(server_7, username, password, N_domain)
res_domain = session_7.GetReservationDetails(resid).ReservationDescription.DomainName
short_path = r'\\qexec7-ssp-sjc.cisco.com\c$\ProgramData\QualiSystems\venv'
short_dir_folders = os.listdir(short_path)
log_entries = []
for sdf in short_dir_folders:
    path = short_path + '\\' + sdf + '\\Lib\\site-packages\\cloudshell\\Logs\\' + resid
    try:
        dir_files = os.listdir(path)
        for dir_file in dir_files:
            full_path = path + '\\' + dir_file
            f = open(full_path, 'r')
            abc = f.read()
            lines = abc.split('\n')
            for line in lines:
                new_entry = entry()
                new_entry.filename = full_path
                new_entry.datetime = line.split('[')[0]
                new_entry.type_om = line.split('[')[1].split(']')[0]
                new_entry.data = line.split(']:')[1].split(' - ')[1]
                log_entries.append(new_entry)
            f.close()
    except:
        pass
pass
session_7.ExecuteResourceConnectedCommand()