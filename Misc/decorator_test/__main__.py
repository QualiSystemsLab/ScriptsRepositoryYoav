from retrying_qslogger.retrying_qslogger import retry
import random
import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, Connector
from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
from cloudshell.workflow.orchestration.sandbox import Sandbox


username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

resid = '325e5105-47c9-4add-8e6c-8fd6a6f1fc8e'

dev_help.attach_to_cloudshell_as(
    user=username,
    password=password,
    domain=domain,
    reservation_id=resid,
    server_address=server
)


def get_reservation_id():
    return "adwacasc"

class best_of():
    deploy = 'z1234'
    def __init__(self):
        deploy = '1234ss'
        self.fake_res_id = "123141231"

    def set_deploy(self):
        deploy = 'cderfv'

    def abcd(self, context):
        context.reservation_id = self.fake_res_id
        self.reservation_id = context.reservation_id
        self._abcd(112, context)
        pass

    @retry(stop_max_attempt_number=1)
    def _abcd(self, inp, context):
        inp = random.random() * inp
        try:
            if inp > 10:
                print 'exception'
                raise Exception('yay')
            else:
                print 'no exception'
        except Exception as e:
            print ('aaa')
            raise e

class fake_context():
    def __init__(self, reservation_id):
        self.reservation_id = reservation_id

def get_debug_session():
    username = 'admin'
    password = 'admin'
    domain = 'Global'
    server = 'localhost'
    resId = '2435c61f-1842-45bd-b6a6-358c9a6ad724'
    attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId
    )

get_debug_session()
session = sh.get_api_session()
token = session.token_id

reservation_context = sh.get_reservation_context_details()
reservation_context.reservation_id = reservation_context.id

connectivity_context = sh.get_connectivity_context_details()
connectivity_context.admin_auth_token = token

# resource_context = sh.get_resource_context_details()

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
    # resource=sh.get_resource_context_details(),
    resource='',
    reservation=reservation_context,
    connectors=context_connectors_reformatted
)

sbox = Sandbox()

myClass = best_of()
myClass.set_deploy()
myClass.abcd(sbox)
pass