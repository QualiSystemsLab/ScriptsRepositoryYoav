from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow

import blueprint_commands


sandbox = Sandbox()

DefaultSetupWorkflow().register(sandbox)

sandbox.workflow.add_to_configuration(blueprint_commands.run_command_on_vms)

sandbox.execute_setup()







