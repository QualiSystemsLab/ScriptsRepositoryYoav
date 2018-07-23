import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = 'CalculateOrchTimes'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
# z.write("drivermetadata.xml")
z.write("requirements.txt")
z.write("html_table_builder.py")
z.write("calculate.py")
z.write("login_sbox_api_activityFeed.py")
z.write("__main__.py")
z.close()

ss = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')
ss.UpdateScript(NameOfDriver, ZipAddress)