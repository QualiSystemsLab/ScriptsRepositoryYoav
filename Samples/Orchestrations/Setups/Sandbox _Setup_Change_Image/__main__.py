from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
import cloudshell.api.cloudshell_api as csapi
import image_changer




sandbox = Sandbox()

BP_commands = image_changer.Blueprint_extra_commands(sandbox.id)
DefaultSetupWorkflow().register(sandbox)
sandbox.workflow.add_to_preparation(BP_commands.enforce_image_name, None)
sandbox.execute_setup()
