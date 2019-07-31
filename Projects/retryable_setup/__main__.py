from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from provisioning_override import custom_provisioning

sandbox = Sandbox()

DefaultSetupWorkflow().register(sandbox, enable_provisioning=False)

cpi = custom_provisioning()

sandbox.workflow.add_to_provisioning(cpi.provisioning_overrider, None)

sandbox.execute_setup()
