import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
import json
import winrm
from cloudshell.core.logger import qs_logger
import qs_cs_sandbox_extractor


resid = '74e69801-63d7-4c0c-bb5c-6a2ea8139ddd'

username = 'admin'
password = 'Itbabyl0n'
server = '40.91.201.107'
domain = 'Global'

dev_help.attach_to_cloudshell_as(
    user=username,
    password=password,
    domain=domain,
    reservation_id=resid,
    server_address=server
)


session = api.CloudShellAPISession(host=server, username=username, password=password, domain=domain)

qq = session.GetReservationDetails('74e69801-63d7-4c0c-bb5c-6a2ea8139ddd')
pass
# tp_det = session.GetTopologyDetails('Skybox_vLab_1.7')
#
#
# apps = tp_det.Apps
#
# res_det = session.GetReservationDetails(resid).ReservationDescription.Resources
# apps = session.GetReservationDetails(resid).ReservationDescription.Apps
# for res in res_det:
#     ss = session.GetResourceDetails(res.Name).ResourceAttributes
#     for s in ss:
#         if s.Name.__contains__('assword'):
#             print res.Name
#             print s.Name
#             print session.DecryptPassword(s.Value).Value
#             print '========================================\n'
# for app in apps:
#     ss = app.LogicalResource.Attributes
#     for s in ss:
#         if s.Name.__contains__('assword'):
#             print app.Name
#             print s.Name
#             print session.DecryptPassword(s.Value).Value
#             print '========================================\n'
# pass

