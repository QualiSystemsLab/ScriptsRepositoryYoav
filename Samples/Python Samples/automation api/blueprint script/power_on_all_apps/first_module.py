from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.api.cloudshell_api import InputNameValue, AttributeNameValue
from helper_code.thread_helpers import get_thread_results
from helper_code.custom_helpers import get_sandbox_apps, get_deployed_app_resources
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import sys

def get_arm_template_services(sandbox):
    services = sandbox.automation_api.GetReservationDetails(reservationId=sandbox.id).ReservationDescription.Services
    arm_services = [service for service in services if service.ServiceName not in ["Subnet", "Azuresupplementcommands"]]
    return arm_services
    pass


def get_azure_command_service(sandbox):
    services = sandbox.automation_api.GetReservationDetails(reservationId=sandbox.id).ReservationDescription.Services
    azure_command_service = [service for service in services if service.ServiceName == "Azuresupplementcommands"]

    if azure_command_service:
        return azure_command_service[0]
    pass


def power_off_arm_services(sandbox, arm_services):
    azure_command_service = get_azure_command_service(sandbox)

    for service in arm_services:
        cmd_input = [InputNameValue("alias", service.Alias)]
        sandbox.automation_api.EnqueueCommand(reservationId=sandbox.id,
                                              targetName=azure_command_service.ServiceName,
                                              targetType="Service",
                                              commandName="start_machine",
                                              commandInputs=cmd_input,
                                              printOutput=True)


def power_on_deployed_apps(sandbox, deployed_apps):
    # uses multi-threading
    def power_on_wrapper(sandbox, device):
        """
        :param Sandbox sandbox:
        :param TopologyReservedResourceInfo device:
        :return: ExecuteCommand response
        """
        return sandbox.automation_api.ExecuteResourceConnectedCommand(reservationId=sandbox.id,
                                                                      resourceFullPath=device.Name,
                                                                      commandName="PowerOn",
                                                                      commandTag="power",
                                                                      printOutput=True)

    threaded_power_off_apps = get_thread_results(sandbox=sandbox,
                                                 device_list=deployed_apps,
                                                 command_wrapper=power_on_wrapper)



SERVICE_MODEL = 'UptimeEnforcer'
def update_power_status_if_available(sandbox):
    """
    :param Sandbox sandbox:
    """
    services = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Services
    try:
        uptime_service = [ser for ser in services if ser.ServiceName == SERVICE_MODEL][0]
        ignore = False
    except:
        sandbox.automation_api.WriteMessageToReservationOutput(
            reservationId=sandbox.id,
            message='no uptime enforcer found , ignoring this part'
        )
        ignore = True
    if not ignore:
        sandbox.automation_api.SetServiceAttributesValues(
            reservationId=sandbox.id,
            serviceAlias=uptime_service.Alias,
            attributeRequests=[AttributeNameValue('{}.Status'.format(SERVICE_MODEL), 'Up')]
        )


def check_if_power_on_allowed(sandbox):
    services = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Services
    allowed_status = True
    try:
        uptime_service = [ser for ser in services if ser.ServiceName == SERVICE_MODEL][0]
        ignore = False
    except:
        sandbox.automation_api.WriteMessageToReservationOutput(
            reservationId=sandbox.id,
            message='no uptime enforcer found , ignoring this part'
        )
        ignore = True
    if not ignore:
        remaining_uptime = [attr.Value for attr in uptime_service.Attributes
                            if attr.Name == '{}.Remaining Uptime'.format(SERVICE_MODEL)][0]
        if remaining_uptime == '00:00':
            allowed_status = False
    return allowed_status

def excepthook(type, value, traceback):
    print(value)

# ========== Primary Function ==========
def first_module_flow(sandbox, components=None):
    """
    Function passed to orchestration flow MUST have two parameters
    :param Sandbox sandbox:
    :param components
    :return:
    """
    deployed_apps = get_deployed_app_resources(sandbox)
    allowed_status = check_if_power_on_allowed(sandbox)
    if allowed_status:
        power_on_deployed_apps(sandbox, deployed_apps)
        update_power_status_if_available(sandbox)
    else:
        sandbox.automation_api.WriteMessageToReservationOutput(
            reservationId=sandbox.id,
            message='can not start sandbox , no uptime left.'
        )
        sys.excepthook = excepthook
        raise Exception('can not start sandbox , no uptime left.\n if you need an extension , please contact <a href="mailto:Alex.Lotan@skyboxsecurity.com">Alex Lotan</a>')