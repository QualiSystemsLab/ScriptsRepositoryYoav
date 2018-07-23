import cloudshell.api.cloudshell_api as api
username = 'admin'
password = 'admin'
server = 'qs.cisco.com'
domain = 'Global'
session = api.CloudShellAPISession(server, username, password, domain)
resource_name = ''
user_att = 'User'