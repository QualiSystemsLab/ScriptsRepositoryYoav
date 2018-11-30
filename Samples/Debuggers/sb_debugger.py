import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.workflow.orchestration.sandbox import Sandbox
import winrm

resid = '1f8b3fab-bc12-4f3b-b0fe-4b6353648dde'

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

# command_inputs = [
#     api.InputNameValue("command", 'show system'),
# ]
# outp = session.ExecuteCommand(reservationId=resid,
#                                       targetName='vsrxwithdriver-8bdf5394',
#                                       targetType="Resource",
#                                       commandName="send_config_command",
#                                       commandInputs=command_inputs).Output
# if outp.__contains__('syslog'):
#     print 'success'
# res_det = session.GetResourceDetails('jumpb-win10-ac6adda4')
# username = filter(lambda x: x.Name == 'User', res_det.ResourceAttributes)[0].Value
# Pass_enc = filter(lambda x: x.Name == 'Password', res_det.ResourceAttributes)[0].Value
# pass_dec = session.DecryptPassword(Pass_enc).Value
# winrm_session = winrm.Session(
#     target=res_det.Address,
#     auth=(username, pass_dec )
# )
# outp = winrm_session.run_cmd('ipconfig')
# pass
def _decrypt(session, password):
    decypted = session.DecryptPassword(password).Value
    return decypted


ARMMODELS = ['Checkpoint', 'CheckpointMgmt', 'Fortigate']
reservation_details = session.GetReservationDetails(resid).ReservationDescription
services = reservation_details.Services
resources = reservation_details.Resources
for resource in resources:

    if resource.VmDetails:
        print '{}:\n'.format(resource.Name)
        res_details = session.GetResourceDetails(resource.Name)
        username = filter(lambda x: x.Name == 'User', res_details.ResourceAttributes)[0].Value
        Pass_enc = filter(lambda x: x.Name == 'Password', res_details.ResourceAttributes)[0].Value
        pass_dec = session.DecryptPassword(Pass_enc).Value
        print '   Username : {}'.format(username)
        print '   Password : {}'.format(pass_dec)
        for nic in resource.VmDetails.NetworkData:
            for add_data in nic.AdditionalData:
                print '       {0}: {1}'.format(add_data.Name, add_data.Value)
            print '\n'

for service in services:
    if service.ServiceName in ARMMODELS:
        vm_name = filter(lambda x: x.Name == '{}.VM Name'.format(service.ServiceName), service.Attributes)[0].Value
        print '{}:\n'.format(vm_name)
        username = filter(lambda x: x.Name == 'User', service.Attributes)[0].Value
        password = filter(lambda x: x.Name == 'Password', service.Attributes)[0].Value
        i = 0
        while i < 5:
            try:
                password = _decrypt(session, password)
            except:
                i = 1000
            i = i + 1

        print '     Username : {}'.format(username)
        print '     Password : {}'.format(password)
        nic_data = json.loads(session.ExecuteCommand(
            reservationId=resid,
            targetType='Service',
            targetName='Azuresupplementcommands',
            commandName='print_vm_nic_information',
            commandInputs=[api.InputNameValue(
                Name='alias',
                Value=service.Alias
            )]
        ).Output)
        for nic in nic_data:
            print ('        Private IP : {}'.format(nic['Private IP']))
            print ('        Public IP : {}'.format(nic['Public IP']))
            print ('        Subnet CIDR : {}'.format(nic['subnet CIDR']))
            print '\n'

