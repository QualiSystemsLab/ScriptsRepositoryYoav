from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from provisioning_override import custom_provisioning


attach_to_cloudshell_as(user="admin",
                        password="admin",
                        domain="Global",
                        reservation_id="be71319c-cf01-4adc-a560-bf41596d824f",
                        server_address="localhost")


sandbox = Sandbox()
DefaultSetupWorkflow().register(sandbox, enable_provisioning=False)
cpi = custom_provisioning()

sandbox.workflow.add_to_provisioning(cpi.provisioning_overrider, None)

sandbox.execute_setup()
