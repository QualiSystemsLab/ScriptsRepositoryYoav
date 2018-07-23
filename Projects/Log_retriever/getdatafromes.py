__author__ = 'yoav.e'

# import win_unc
import os
import shutil



def go_through_folder(j, unc_path, loc_path, resid):
    curr_path = unc_path + '\\' + j + '\\'
    print curr_path
    for ROOT, DIR, FILES in os.walk(curr_path):
        if ROOT.__contains__(resid):
            new_loc_dir = loc_path + '\\' + j
            os.mkdir(new_loc_dir)
            for f in FILES:
                file_path = ROOT + '\\' + f
                shutil.copy(file_path, new_loc_dir)
            break

def copy_file_to_server():
    pass

resid = 'ab03e40b-15bc-41ea-a79b-5ecd2a7715cb'
# unc_path = r'\\qexec7-ssp-sjc.cisco.com\c$\programdata\qualisystems\venv'
# server_path = r'\\qs.cisco.com\c$\programdata\qualisystems\venv'
unc_path = r'c:\programdata\qualisystems\venv'
loc_path = r'C:\temp\autlog'
# creds = win_unc.UncCredentials('quali.gen@cisco.com', 'Password3')
# authz_unc = win_unc.UncDirectory(unc_path, creds)
# conn = win_unc.UncDirectoryConnection(authz_unc)
# conn.connect()
jj = os.listdir(unc_path)
for j in jj:
    go_through_folder(j, unc_path, loc_path, resid)
# conn.disconnect()
pass