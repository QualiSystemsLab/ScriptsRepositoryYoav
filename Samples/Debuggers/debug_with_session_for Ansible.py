import cloudshell.api.cloudshell_api as api
import cloudshell.cm.ansible.ansible_shell as ansible
import json

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'
new_server = 'localhost'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

resid = '49cfa1b9-c2f9-4189-8af6-c617bb6f63f2'
service_Name = 'AnsibleServer'
attrs = session.GetReservationDetails(resid).ReservationDescription.Services[0].Attributes
passwrd = session.DecryptPassword([attr.Value for attr in attrs if attr.Name == 'Password'][0]).Value
username = [attr.Value for attr in attrs if attr.Name == 'User'][0]
TimeoutMinutes = [attr.Value for attr in attrs if attr.Name == 'Timeout Minutes'][0]
playbook_url = [attr.Value for attr in attrs if attr.Name == 'URL'][0]

Inputs_Json = '''
{
    "additionalArgs": "",
    "timeoutMinutes": "10",
    "repositoryDetails" : {
        "url": "",
        "username": "",
        "password": ""
    },
    "hostsDetails": [
    {
        "ip": "192.168.85.24",
        "username": "",
        "password": "",
        "accessKey": "",
        "connectionMethod": "ssh",
        "connectionSecured": "true",
        "groups": [],
        "parameters": [
        {
            "name": "a",
            "value": "SomeValue"
        }]
    }]
}
'''
JsonDetails = json.loads(Inputs_Json)
JsonDetails['hostsDetails'][0]['username'] = username
JsonDetails['hostsDetails'][0]['password'] = passwrd
JsonDetails['timeoutMinutes'] = TimeoutMinutes
JsonDetails['repositoryDetails']['url'] = playbook_url
pass

command_inputs = [
    api.InputNameValue(
        Name='ansible_configuration_json',
        Value=json.dumps(JsonDetails)
    )
]

session.ExecuteCommand(
    reservationId=resid,
    targetName=service_Name,
    targetType='Service',
    commandName='execute_playbook',
    commandInputs=command_inputs
)
pass