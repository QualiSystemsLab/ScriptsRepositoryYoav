import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = 'ActivateConsole'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
# z.write("drivermetadata.xml")
# z.write("requirements.txt")
z.write("activateConsole.py")
z.write("__main__.py")
z.close()

ss = api.CloudShellAPISession('qs.cisco.com', 'admin', 'admin', 'Global')
ss.UpdateScript(NameOfDriver, ZipAddress)

