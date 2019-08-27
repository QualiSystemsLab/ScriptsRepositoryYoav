from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
import cloudshell.api.cloudshell_api as csapi

sandbox = Sandbox()
def choose_customer(sandbox, components):
    """
    :param Sandbox sandbox:
    :return:
    """
    out = sandbox.automation_api.ExecuteCommand(
        reservationId=sandbox.id,
        targetName='Livestatuschanger',
        targetType='Service',
        commandName='change_live_status',
        commandInputs=[],
        printOutput=True
    ).Output

DefaultSetupWorkflow().register(sandbox)
sandbox.workflow.add_to_provisioning(choose_customer, None)
sandbox.execute_setup()
