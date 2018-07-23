import zipfile
# import cloudshell.api.cloudshell_api as api
import qualipy.api.cloudshell_api as api


NameOfDriver = 'AdminOptions_CreateConnection'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
# z.write("drivermetadata.xml")
# z.write("requirements.txt")
# z.write("CreateResource.py")
z.write("CreateConnection.py")
z.write("get_cs_session.py")
z.write("__main__.py")
z.close()

ss = api.CloudShellAPISession('q1.cisco.com', 'admin', 'admin', 'Global')
# ss.UpdateScript(NameOfDriver, ZipAddress)

