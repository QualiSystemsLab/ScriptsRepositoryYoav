import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

resid = '1d8ce04b-2a8e-456e-841f-f4dcf5fe6d72'

username = 'admin'
password = 'Itbabyl0n'
server = '40.91.201.107'
domain = 'Global'

dev_help.attach_to_cloudshell_as(
    user=username,
    password=password,
    domain=domain,
    reservation_id=resid,
    server_address=server
)

def find_all_subnet_connections(session, subnet_name, connections):
    '''
    :param CloudShellAPISession session:
    :param subnet_name:
    :param [api.Connector] connections:
    :return:
    '''
    connected_to_subnet = []
    for connection in connections:
        if connection.Source == subnet_name:
            connected_to_subnet.append(connection.Target)
        elif connection.Target == subnet_name:
            connected_to_subnet.append(connection.Source)
    return connected_to_subnet

def find_gateway_entity(gateway_name, resources , services):
    '''
    :param CloudShellAPISession session:
    '''
    resources_from_apps = [res for res in resources if res.AppDetails]
    gateway = [x.Name for x in resources_from_apps if x.AppDetails.AppName.lower() == gateway_name.lower()]
    if gateway.__len__() > 0:
        return gateway[0]
    else:
        gateway = [x.Alias for x in services if x.Alias.lower() == gateway_name.lower()]
        if gateway.__len__() > 0:
            return gateway[0]
        else:
            gateway = None
            return gateway

session = script_help.get_api_session()
resource_description = session.GetReservationDetails(resid).ReservationDescription
services = resource_description.Services
resources = resource_description.Resources
connections = resource_description.Connectors
subnets = [service for service in services if service.ServiceName == 'Subnet']

for subnet in subnets:
    internal_gateway_raw = [attr.Value for attr in subnet.Attributes if attr.Name == 'Internal Gateway'][0]
    external_gateway_raw = [attr.Value for attr in subnet.Attributes if attr.Name == 'External Gateway'][0]
    if internal_gateway_raw != '':
        subnet.internal_gateway = find_gateway_entity(internal_gateway_raw, resources, services)
    if external_gateway_raw != '':
        subnet.external_gateway = find_gateway_entity(external_gateway_raw, resources, services)


# for subnet in subnets:
#     subnet.connections = find_all_subnet_connections
#     (
#         session,
#         subnet.Alias,
#         connections
#     )
pass
session.SetAppSecurityGroups()