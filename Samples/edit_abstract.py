from quali_utils.quali_packaging import PackageEditor
import requests
PE = PackageEditor()
def upload_file_to_CloudShell(filepath):
    r = requests.put('http://localhost:9000/Api/Auth/Login', {"username": "admin", "password": "admin", "domain": "Global"})
    authcode = "Basic " + r._content[1:-1]
    fileobj = open(filepath, 'rb')
    r = requests.post('http://localhost:9000/API/Package/ImportPackage',
                      headers={"Authorization": authcode},
                      files={"file": fileobj})

def get_cs_api_session():
    import cloudshell.api.cloudshell_api as api
    username = 'admin'
    password = 'admin'
    server = 'localhost'
    domain = 'Global'

    session = api.CloudShellAPISession(
        username=username,
        password=password,
        domain=domain,
        host=server
    )
    return session

def add_poss_values_to_abstract(filepath, blueprint_name):
    PE.load(filepath)
    PE.add_attribute_to_abstract(
        topology_name=blueprint_name,
        abstract_path='Samsung STB',
        attribute_name='SetTopBoxSamsung.ServerName',
        possible_values=['Obelix_Server_3', 'Obelix_Server_1'],
        default_value='Obelix_Server_3',
        required=True,
        publish=True
    )

filepath = r"C:\temp\set-top-boxes-specific Manufacturer\set-top-boxes-specific Manufacturer.zip"
blueprint_name = 'set-top-boxes-specific Manufacturer1'
session = get_cs_api_session()
session.DeleteTopology(blueprint_name)
add_poss_values_to_abstract(filepath, blueprint_name)
upload_file_to_CloudShell(filepath)
pass