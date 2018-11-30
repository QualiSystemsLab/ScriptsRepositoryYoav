import json
from cloudshell.api.cloudshell_api import InputNameValue
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.api.cloudshell_api as api
from cloudshell.workflow.orchestration.sandbox import Sandbox

DCMODEL = 'Dcstaticvm'
ARMMODELS = ['Checkpoint', 'CheckpointMgmt', 'Fortigate']
NIC_ROLES = ['FortiBranch', 'WANCPFW']
SB_SERVER_MODEL = 'Skybox-Server'
VSRX_Model = 'VSRx_NS'


class fortitest():
    def __init__(self):
        pass

    def _get_connected_vsrx_nic_ip(self, session, forti_service, resid):
        vsrx = [res for res in session.GetReservationDetails(resid).ReservationDescription.Resources if
                res.ResourceModelName == VSRX_Model][0]
        vsrx_net_data = vsrx.VmDetails.NetworkData
        vsrx_net_data_dict = {}
        for net in vsrx_net_data:
            temp_ip = [attr.Value for attr in net.AdditionalData if attr.Name == 'ip'][0]
            vsrx_net_data_dict.update({net.NetworkId: temp_ip})
        nics_info = json.loads(session.ExecuteCommand(
            reservationId=resid,
            targetName=forti_service,
            targetType='Service',
            commandName='get_nic_information',
            commandInputs=[],
            printOutput=True
        ).Output)
        my_vsrx_nic_ip = None
        for nic in nics_info:
            if nic.get('Subnet Name') in vsrx_net_data_dict.keys():
                my_vsrx_nic_ip = vsrx_net_data_dict.get(nic.get('Subnet Name'))
        return my_vsrx_nic_ip


    def deploy_single_fortigate(self, sandbox, components, forti):
        """
        :param Sandbox sandbox:
        :param components:
        :return:
        """
        # 1. set all interfaces:
        nics_info = json.loads(sandbox.automation_api.ExecuteCommand(
            reservationId=sandbox.id,
            targetName=forti.Alias,
            targetType='Service',
            commandName='get_nic_information',
            commandInputs=[],
            printOutput=True
        ).Output)
        k = 1
        for nic_info in nics_info:
            print 'Port{}'.format(str(k))
            print nic_info.get('Private IP')
            sandbox.automation_api.ExecuteCommand(
                reservationId=sandbox.id,
                targetName=forti.Alias,
                targetType='Service',
                commandName='fortinet_service_set_ip',
                commandInputs=[InputNameValue('Interface', 'port{}'.format(str(k))),
                               InputNameValue('IP', nic_info.get('Private IP')),
                               InputNameValue('Netmask', '255.255.255.240')],
                printOutput=True
            )
            k = k+1
        # 2. set policy - allow all:
        sandbox.automation_api.ExecuteCommand(
            reservationId=sandbox.id,
            targetName=forti.Alias,
            targetType='Service',
            commandName='fortinet_service_set_ipv4_policy',
            commandInputs=[InputNameValue('source_interface', 'port1'),
                           InputNameValue('target_interface', 'port2'),
                           InputNameValue('policy_id', '100'),
                           InputNameValue('policy_name', 'allow_all_port1_to_port2')],
            printOutput=True
        )
        sandbox.automation_api.ExecuteCommand(
            reservationId=sandbox.id,
            targetName=forti.Alias,
            targetType='Service',
            commandName='fortinet_service_set_ipv4_policy',
            commandInputs=[InputNameValue('source_interface', 'port2'),
                           InputNameValue('target_interface', 'port1'),
                           InputNameValue('policy_id', '101'),
                           InputNameValue('policy_name', 'allow_all_port2_to_port1')],
            printOutput=True
        )
        # 3. set static routes:
        nic1_subnet = None
        for nic_info in nics_info:
            nic_name = nic_info.get('Nic Name')
            if nic_name.__contains__('Nic0'):
                nic0 = nic_info
            elif nic_name.__contains__('Nic1'):
                nic1 = nic_info
                nic1_subnet = nic1.get('Subnet Name').split('_')[-1].replace('-', '/')
        vsrx_nic = self._get_connected_vsrx_nic_ip(
            session=sandbox.automation_api,
            resid=sandbox.id,
            forti_service=forti.Alias
        )

        sandbox.automation_api.ExecuteCommand(
            reservationId=sandbox.id,
            targetName=forti.Alias,
            targetType='Service',
            commandName='fortinet_set_static_route',
            commandInputs=[InputNameValue('interface_name', 'port2'),
                           InputNameValue('dst_subnet', nic1_subnet),
                           InputNameValue('sequence_id', '101'),
                           InputNameValue('gateway', vsrx_nic)],
            printOutput=True
        )
        pass

    def deploy_fortigates(self, sandbox, components):
        """
        :param Sandbox sandbox:
        :param components:
        :return:
        """
        # 1. find Fortigate  in the sandbox:
        services = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Services
        forti_services = [ser for ser in services if ser.ServiceName == 'Fortigate']
        for forti in forti_services:
            self.deploy_single_fortigate(sandbox, components, forti)

class Sandbox_lite():
    def __init__(self):
        pass

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
# abcd = session.GetServices('Security', 'CheckpointMgmt')
services_vm_names = []
resid = '15f016de-692f-48a8-8be5-1d3744d31ad0'
sandbox = Sandbox_lite()
sandbox.automation_api = session
sandbox.id = resid
qq = fortitest()
qq.deploy_fortigates(sandbox, None)