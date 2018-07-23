from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
import cloudshell.api.cloudshell_api as csapi

allcustomers = {
    'Customer A': '201-220',
    'Customer B': '221-240',
    'Customer C': '241-260',
}


sandbox = Sandbox()
def choose_customer(sandbox, components):
    """
    :param Sandbox sandbox:
    :return:
    """

    customer_name = sandbox.global_inputs['Customer Name']
    vlan_range = allcustomers[customer_name]
    attr_req = csapi.AttributeNameValue(
        Name='Allocation Ranges',
        Value=vlan_range
    )
    sandbox.automation_api.SetServiceAttributesValues(
        reservationId=sandbox.id,
        serviceAlias='VLAN Auto_Customer',
        attributeRequests=[attr_req]
    )
    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, 'setting environment for {}'.format(customer_name))


DefaultSetupWorkflow().register(sandbox)
sandbox.workflow.add_to_provisioning(choose_customer, None)
sandbox.execute_setup()
