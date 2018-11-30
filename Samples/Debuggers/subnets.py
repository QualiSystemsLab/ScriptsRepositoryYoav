from py_linq import Enumerable
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

class testclass():
    def __init__(self):
        pass

    def _service_is_subnet(self, service, public):
        attributes = Enumerable(service.Attributes)
        return attributes.any(lambda att: att.Name == 'Subnet Id') and \
               attributes.any(lambda att: att.Name == 'Public' and att.Value == public) and \
               attributes.any(lambda att: att.Name == 'internet' and att.Value == 'False')


    def _extract_subnet_data(self, services, targets, public):
        subnet = Enumerable(services).where(lambda s: s.Alias in targets) \
            .where(lambda s: self._service_is_subnet(s, public)).first_or_default()

        if not subnet:
            raise Exception("No {public} subnet found for Fortigate".format(public=public))

        name = Enumerable(subnet.Attributes) \
            .where(lambda att: att.Name == 'Subnet Id') \
            .select(lambda att: att.Value).first()

        cidr_range = Enumerable(subnet.Attributes) \
            .where(lambda att: att.Name == 'Allocated CIDR') \
            .select(lambda att: att.Value).first()

        return name, cidr_range


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
resid = 'f9d61fe9-a9e0-49ef-aeaa-c17188021f0e'
qq = testclass()

reservation = session.GetReservationDetails(resid).ReservationDescription
connectors = [conn for conn in reservation.Connectors if conn.Source == 'Fortigate' or conn.Target == 'Fortigate']
targets = Enumerable(connectors).select(lambda x:x.Target).to_list()
public_subnet, public_cidr = qq._extract_subnet_data(reservation.Services, targets, 'True')
pass
