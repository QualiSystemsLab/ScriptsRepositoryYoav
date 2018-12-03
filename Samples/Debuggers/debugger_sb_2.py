import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.workflow.orchestration.sandbox import Sandbox
import winrm

resid = 'cf23f723-d193-4e0a-9965-0c1a9dc69801'

username = 'admin'
password = 'Itbabyl0n'
server = '40.118.18.233'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
ARMMODELS = ['Checkpoint', 'CheckpointMgmt', 'Fortigate']
def get_service_attribute_by_name(service, attribute_name):
    attr_value = filter(lambda x:x.Name == attribute_name, service.Attributes)[0].Value
    return attr_value

def get_alias_clean_name(alias):
    alias_list = alias.split('-')
    return ''.join(alias_list[:-2]).strip()

reservation_details = session.GetReservationDetails(resid).ReservationDescription
resources = reservation_details.Resources
services = reservation_details.Services
subnets = filter(lambda x:x.ServiceName == 'Subnet', services)
ARM_services = filter(lambda x:x.ServiceName in ARMMODELS, services)
for subnet in subnets:
    subnet_ip = get_service_attribute_by_name(subnet, 'Allocated CIDR').split('/')[0]
    command_inputs = [
        api.InputNameValue(Name='object_type', Value='network'),
        api.InputNameValue(Name='ip', Value=subnet_ip),
        api.InputNameValue(Name='name', Value='{}'.format(get_alias_clean_name(subnet.Alias))),
        api.InputNameValue(Name='subnet_mask', Value='255.255.255.240')
    ]
    session.ExecuteCommand(
        reservationId=resid,
        targetName='CheckpointMgmt',
        targetType='Service',
        commandName='create_single_object',
        commandInputs=command_inputs
    )
for resource in resources:
    if resource.VmDetails:
        command_inputs = [
            api.InputNameValue(Name='object_type', Value='host'),
            api.InputNameValue(Name='ip', Value=resource.FullAddress),
            api.InputNameValue(Name='name', Value=resource.Name),
        ]
        session.ExecuteCommand(
            reservationId=resid,
            targetName='CheckpointMgmt',
            targetType='Service',
            commandName='create_single_object',
            commandInputs=command_inputs
        )
for arm in ARM_services:
        command_inputs = [
            api.InputNameValue(Name='object_type', Value='host'),
            api.InputNameValue(Name='ip', Value=arm.Address),
            api.InputNameValue(Name='name', Value=arm.Alias),
        ]
        session.ExecuteCommand(
            reservationId=resid,
            targetName='CheckpointMgmt',
            targetType='Service',
            commandName='create_single_object',
            commandInputs=command_inputs
        )