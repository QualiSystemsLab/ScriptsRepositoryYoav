import cloudshell.api.cloudshell_api as api
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
qq = session.FindResources(resourceModel='Resource Constants Model').Resources
qq_details = session.GetResourceDetails(qq[0].Name)
project_names = [x.Name.split('/')[-1] for x in qq_details.ChildResources]
session
pass