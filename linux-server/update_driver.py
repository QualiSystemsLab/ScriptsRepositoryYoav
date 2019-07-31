import zipfile
import cloudshell.api.cloudshell_api as cs_api
import os

credentials = {
    "user": "admin",
    "password": "admin",
    "domain": "Global",
    "server": "localhost"
}
# ***************Add Custom Script Name if Desired***********************

# script_name will default to name of the directory, can be changed here
custom_script_name = 'linux-server'

# ************************************************************************

default_directory_name = os.path.basename(os.getcwd())
driver_name = custom_script_name or default_directory_name
zip_address = driver_name + '.zip'


def zip_files():
    z = zipfile.ZipFile(zip_address, "w")
    files_to_exclude = [zip_address, "venv", ".idea"]
    all_files = [f for f in os.listdir('.')
                 if f not in files_to_exclude
                 and not f.endswith('.pyc')]

    for script_file in all_files:
        z.write(script_file)

    z.close()

    if zip_address in os.listdir('.'):
        print("[+] ZIPPED UP: '{zip_address}'".format(zip_address=zip_address))
    else:
        print("[-] ZIP FILE DOES NOT EXIST")


def establish_cs_session():
    try:
        ses = cs_api.CloudShellAPISession(host=credentials["server"],
                                          username=credentials["user"],
                                          password=credentials["password"],
                                          domain=credentials["domain"])
    except Exception as e:
        print("[-] THERE WAS AN ERROR ESTABLISHING CLOUDSHELL API SESSION" + "\n" + str(e))
        exit(1)
    else:
        return ses


def update_script(cs_ses):
    try:
        cs_ses.UpdateDriver(driver_name, zip_address)
    except Exception as e:
        print("[-] THERE WAS AN ERROR UPDATING SCRIPT\n" + str(e) + "\nPLEASE LOAD SCRIPT MANUALLY THE FIRST TIME")
        exit(1)
    else:
        print("[+] SUCCESFULLY UPDATED IN PORTAL: '{script}'".format(script=driver_name))


def load_to_cs():
    zip_files()
    cs_ses = establish_cs_session()
    update_script(cs_ses)


load_to_cs()



