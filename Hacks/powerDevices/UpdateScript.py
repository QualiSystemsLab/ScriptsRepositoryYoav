import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = 'InputUpdater_user'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
# z.write("drivermetadata.xml")
# z.write("requirements.txt")
z.write("InputUpdateTPC.py")
z.write("__main__.py")
z.close()

ss = api.CloudShellAPISession('10.87.42.117', 'admin', 'admin', 'Global')
ss.UpdateScript(NameOfDriver, ZipAddress)

