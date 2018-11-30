import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help

session = api.CloudShellAPISession(
    host='localhost',
    username='admin',
    password='admin',
    domain='Global'
)
# session = script_help.get_api_session()


# all_resources = session.FindResources(resourceFamily='CS_ComputeServer')
# session.CreateResource(
#     resourceFamily='aa'
# )
#
#
# for resource in all_resources.Resources:
#     session.AutoLoad(resourceFullPath=resource.Name)

res_details = session.GetResourceDetails('Dut2')
phys_connections = []
for i, child in enumerate(res_details.ChildResources):
    print child.Name
    print child.Connections[0].FullPath
    phys_connections.append(
        api.PhysicalConnectionUpdateRequest(ResourceAFullName=child.Name,
            ResourceBFullName='L1_Mock/Blade 1/Port 00{}'.format(str(i+5)),
                                            ConnectionWeight='10'
        )
    )

session.UpdatePhysicalConnections(
    phys_connections
)

# session.UpdatePhysicalConnection(
#     resourceAFullPath=child.Name,
#     resourceBFullPath='L1_Mock/Blade 1/Port 017'
# )

# new_connection = child.Connections[0].FullPath
# new_connection_port = int(new_connection.split(' ')[-1]) + 1
# new_connection_revised = ' '.join([new_connection.split(' ')[0:-1], str(new_connection_port)])
# session.UpdatePhysicalConnection(
#     resourceAFullPath=child.Name,
#     resourceBFullPath=child.Connections[0].FullPath
# )
pass