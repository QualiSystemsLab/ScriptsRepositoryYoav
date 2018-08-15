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

session.AddResourcesToDomain(
    domainName='',
    resourcesNames=['res1, res2'],
    includeDecendants=True
)
pass