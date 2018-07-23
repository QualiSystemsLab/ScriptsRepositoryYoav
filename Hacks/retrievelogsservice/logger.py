__author__ = 'yoav.e'
import cloudshell.api.cloudshell_api as api
import zipfile
import win_unc
import os
import shutil
username = 'admin'
password = 'admin'
server = 'qs.cisco.com'
domain = 'Global'
session = api.CloudShellAPISession(server, username, password, domain)
# resid = 'e2bda8c3-ad76-40d0-8d8a-56f2a5ec78c7'
# res_domain = session.GetReservationDetails(resid).ReservationDescription.DomainName
unc_path = r'\\10.87.42.119\c$\Temp'
# creds = win_unc.UncCredentials('quali.gen@cisco.com', 'Password3')
# authz_unc = win_unc.UncDirectory(unc_path, creds)
# conn = win_unc.UncDirectoryConnection(authz_unc)
# conn.connect()
curr_path = r'C:\temp\autlog\\'
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
zipf = zipfile.ZipFile(curr_path + r'\Python.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(curr_path, zipf)
zipf.close()

# file_path = r"C:\temp\autlog.zip"
# shutil.copy(file_path, unc_path)
# conn.disconnect()
pass
