import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = ''
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
z.write("drivermetadata.xml")
z.write("requirements.txt")
z.write(".py")
# z.write("drivercontext.py")
z.close()


ss = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')
ss.UpdateDriver(NameOfDriver, ZipAddress)


