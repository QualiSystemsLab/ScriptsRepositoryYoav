from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
from credentials import credentials
from first_module import first_module_flow

DEBUG_PRINT = False
LIVE_SANDBOX_ID = "dbb7119b-e1ee-47a7-95a0-425a5b89db29"
TARGET_RESOURCE_NAME = None
TARGET_SERVICE_NAME = None

attach_to_cloudshell_as(user=credentials["user"],
                        password=credentials["password"],
                        domain=credentials["domain"],
                        reservation_id=LIVE_SANDBOX_ID,
                        server_address=credentials['server'],
                        resource_name=TARGET_RESOURCE_NAME,
                        service_name=TARGET_SERVICE_NAME)

sandbox = Sandbox()
first_module_flow(sandbox=sandbox, components=None)
