from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from blueprint_commands import extra_setup_commands


sandbox = Sandbox()
extra_commands_instance = extra_setup_commands(sandbox.id)

DefaultSetupWorkflow().register(sandbox)

sandbox.workflow.add_to_configuration(extra_commands_instance.run_command_on_vms)

sandbox.execute_setup()







