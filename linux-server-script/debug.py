# from cloudshell.workflow.orchestration.sandbox import Sandbox
# from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
import driver
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext

from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh
import cloudshell.api.cloudshell_api as api
DEBUG_MODE = True
attach_to_cloudshell_as(user="admin",
                        password="admin",
                        domain="Global",
                        reservation_id="2435c61f-1842-45bd-b6a6-358c9a6ad724",
                        server_address="localhost",
                        resource_name='Centos VM_54f9-d724')


session = sh.get_api_session()
token = session.token_id

reservation_context = sh.get_reservation_context_details()
reservation_context.reservation_id = reservation_context.id

connectivity_context = sh.get_connectivity_context_details()
connectivity_context.admin_auth_token = token

context = ResourceCommandContext(
    connectivity=connectivity_context,
    resource=sh.get_resource_context_details(),
    reservation=reservation_context,
    connectors=''
)



# context = ResourceCommandContext(connectivity=sh.get_connectivity_context_details(),
#                                  reservation=sh.get_reservation_context_details(),
#                                  resource=sh.get_resource_context_details(),
#                                  connectors=None
#                                  )

init_context = InitCommandContext(connectivity=sh.get_connectivity_context_details(),
                                  resource=sh.get_resource_context_details())


my_driver = driver.SkyboxServerDriver()
my_driver.initialize(init_context)
my_driver.send_command(context, 'ifconfig')
# my_driver.configure(context)
pass