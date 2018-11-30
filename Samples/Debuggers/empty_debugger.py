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

resource_from_specific_model = session.FindResources(resourceModel='someResourceModel').Resources

for res in resource_from_specific_model:
    session.AutoLoad(
        resourceFullPath=res.Name
    )

my_root_connection = session.GetResourceDetails('myResourceName').Connections
port_connections = []
for child in session.GetResourceDetails('myResourceName').ChildResources:
    port_connections.append(child.Connections)



# one update
session.UpdatePhysicalConnection(
    resourceAFullPath='AResourcePort',
    resourceBFullPath='BResourcePort',
    overrideExistingConnections=True # True to Override , False to not override
)

# Bulk
connectionsList = []
connectionsList.append(api.PhysicalConnectionUpdateRequest(
    ResourceAFullName='AResourcePort',
    ResourceBFullName='BResourcePort',
    ConnectionWeight='10' # if there is routing resolution , heavier weight would be preferred. 10 is default
))
session.UpdatePhysicalConnections(
    physicalConnectionUpdateRequest=connectionsList
)