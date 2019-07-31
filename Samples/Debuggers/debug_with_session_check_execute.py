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

dec_password = session.DecryptPassword('string')
