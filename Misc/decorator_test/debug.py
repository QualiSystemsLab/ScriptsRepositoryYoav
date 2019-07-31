from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext
import driver
from cloudshell.shell.core.driver_context import ResourceContextDetails, ReservationContextDetails, Connector

def get_debug_session():
    username = 'admin'
    password = 'admin'
    domain = 'Global'
    server = 'localhost'
    resId = '325e5105-47c9-4add-8e6c-8fd6a6f1fc8e'
    attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
        service_name='UptimeEnforcer'
    )

get_debug_session()
session = sh.get_api_session()
token = session.token_id

reservation_context = sh.get_reservation_context_details()
reservation_context.reservation_id = reservation_context.id

connectivity_context = sh.get_connectivity_context_details()
connectivity_context.admin_auth_token = token

resource_context = sh.get_resource_context_details()

reservation_description = session.GetReservationDetails(reservation_context.id).ReservationDescription
services = reservation_description.Services
connectors = reservation_description.Connectors
context_connectors = [conn for conn in connectors if resource_context.name in [conn.Source, conn.Target]]
context_connectors_reformatted = []
for conn in context_connectors:
    temp_connector = Connector(
        source=conn.Source,
        target=conn.Target,
        alias=conn.Alias,
        attributes=conn.Attributes,
        connection_type=conn.Type,
        direction=conn.Direction,
        targetFamily='',
        targetAttributes='',
        targetType='',
        targetModel=''
    )
    context_connectors_reformatted.append(temp_connector)


context = ResourceCommandContext(
    connectivity=connectivity_context,
    resource=sh.get_resource_context_details(),
    reservation=reservation_context,
    connectors=context_connectors_reformatted
)

myclass = driver.UptimeEnforcerDriver()
myclass.check_uptime_status(context)
pass