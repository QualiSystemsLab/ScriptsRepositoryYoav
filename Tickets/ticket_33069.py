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

session.SetCustomShellAttribute(
    modelName='Obelix',
    attributeName='Autoload',
    defaultValue='1'
)