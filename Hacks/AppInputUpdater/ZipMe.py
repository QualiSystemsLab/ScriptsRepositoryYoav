import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = 'InputUpdater'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
z.write("drivermetadata.xml")
z.write("requirements.txt")
z.write("inputUpdater.py")
# z.write("drivercontext.py")
z.close()

ss = api.CloudShellAPISession('10.87.42.117', 'admin', 'admin', 'Global')
ss.UpdateDriver(NameOfDriver, ZipAddress)


