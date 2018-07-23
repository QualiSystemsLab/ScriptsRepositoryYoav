__author__ = 'yoav.e'
import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_dev_helpers as cdh
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as csh
from natsort import natsorted
username = 'admin'
password = 'admin'
server = 'qs.cisco.com'
domain = 'SSP SJC'
session = api.CloudShellAPISession(server, username, password, domain)
# Controller_Resource_name = 'TVM-C-0011'
# controller_details = session.GetResourceDetails(Controller_Resource_name)
# print 'The username is {0} and Password is {1} for controller in address {2}'.format(
#     [attr.Value for attr in controller_details.ResourceAttributes if attr.Name == 'User'][0],
#     session.DecryptPassword([attr.Value for attr in controller_details.ResourceAttributes if attr.Name == 'Password'][0]).Value,
#     controller_details.FullAddress
# )
#
# services = session.GetReservationDetails('4e6c66e4-f388-41e2-9824-1c1040eb4123').ReservationDescription.Services
# pcs = []
# for service in services:
#     if service.ServiceName == 'Port Channel Service':
#         pcs.append(service)
# sorted_pcs = natsorted(pcs, key=lambda x: x.Alias)

# services = session.GetReservationDetails('7a866f43-34be-4e6a-8f05-5be9c36fb17e').ReservationDescription.Services
# resid = '1f72d302-7de7-47bc-8a7a-3a76b00e8992'
# qq = session.GetReservationDetails(resid).ReservationDescription.Resources
# vms = [q for q in qq if q.ResourceModelName == 'TVM_Interface']
# dd = session.GetResourceDetails('TVM_Interfaces')
# gws = []
# counter = [0, 0, 0, 0, 0, 0, 0, 0]
# for intf in dd.ChildResources:
#     gw = [attr.Value for attr in intf.ResourceAttributes if attr.Name == 'SSP Interface Role'][0]
#     print intf.Name, gw
#     gws.append({'Name': intf.Name, 'Gateway': gw})
#     counter[int(gw) - 1] += 1
# sorted_gws = []
# sorted_gws = sorted(gws, key=lambda x: x.get('Gateway'))
# pass

# a = api.UpdateTopologyRequirementsInputsRequest(ResourceName="SJC-KP",
#                                                 ParamName="Serial Number",
#                                                 Value="JAD201707RG",
#                                                 Type='Attributes')
# out = session.CreateImmediateTopologyReservation(
#     "test_reservation",
#     owner="wbaron",
#     durationInMinutes=60,
#     notifyOnStart=True,
#     notifyOnEnd=False,
#     notificationMinutesBeforeEnd=120,
#     topologyFullPath='SSP SJC topologies\Topo 1 Lite 16-10-24 [SSP-SJC]',
#     globalInputs=[],
#     requirementsInputs = a)


pass