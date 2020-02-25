from cloudshell.helpers.scripts.cloudshell_scripts_helpers import get_api_session, get_reservation_context_details, get_resource_context_details
from centos_driver import CentosServerDriver
import os
command = os.environ['command']
session = get_api_session()
driver_instance = CentosServerDriver()
resource_context = get_resource_context_details()
reservation_context=  get_reservation_context_details()
out = driver_instance.send_command(session=session, command=command, resource=resource_context, reservation=reservation_context)
print out
