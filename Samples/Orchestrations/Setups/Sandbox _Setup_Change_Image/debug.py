from cloudshell.workflow.orchestration.sandbox import Sandbox
# from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
import image_changer
from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as

DEBUG_MODE = True
attach_to_cloudshell_as(user="yoav.e",
                        password="1234",
                        domain="Global",
                        reservation_id="3430d615-9d35-4ddb-9913-495fb38af50b",
                        server_address="40.91.201.107")


sandbox = Sandbox()
BP_commands = image_changer.Blueprint_extra_commands(sandbox.id)



if DEBUG_MODE:
    BP_commands.enforce_image_name(sandbox, components=None)
    exit(0)
