import cloudshell.api.cloudshell_api as api
import requests
import json
username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

login_url= 'http://localhost:82/api/login'
login_data = {
  "username": "admin",
  "password": "admin",
  "domain": "Global"
}
login_response = requests.put(
    url=login_url,
    json=login_data
).text[1:-1]

headers = {
    "Authorization": "Basic NGSrWDtbmUmtEWoSiQvHGA=="
}
sandboxes_current_url = 'http://localhost:82/api/v2/sandboxes'
sandboxes_current = requests.get(
    url=sandboxes_current_url,
    headers=headers
).text
sandboxes__current_json = json.loads(sandboxes_current)

sandboxes_historic_url = 'http://localhost:82/api/v2/sandboxes?show_historic=true'
sandboxes_historic = requests.get(
    url=sandboxes_historic_url,
    headers=headers
).text
sandboxes_historic_json = json.loads(sandboxes_historic)
old_sandboxes = []
for item in sandboxes_historic_json:
    if item not in sandboxes__current_json:
        old_sandboxes.append(item.get('id'))
session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
for sbox in old_sandboxes:
    session.DeleteReservation(
        reservationId=sbox
    )

pass
# sandbox_id = '89db43f7-a90c-4267-b198-8a03384ef631'
# res_det = session.GetReservationDetails(sandbox_id)
# DHCP_apps = [dhcp for dhcp in res_det.ReservationDescription.Apps if dhcp.LogicalResource.Model == 'DHCP Server']
# if DHCP_apps.__len__() > 0:
#     DHCP_app = DHCP_apps[0]
#     # session.DeployAppToCloudProvider(
#     #     reservationId=sandbox_id,
#     #     appName=DHCP_app.Name,
#     #     commandInputs=[],
#     #     printOutput=True
#     # )
#     for connection in res_det.ReservationDescription.Connectors:
#         try:
#             Source_model = session.GetResourceDetails(connection.Source)
#         except:
#             Source_model = None
#         try:
#             Target_model = session.GetResourceDetails(connection.Target)
#         except:
#             Target_model = None
#         if Source_model == DHCP_app.LogicalResource.Model or Target_model == DHCP_app.LogicalResource.Model:
#             session.ConnectRoutesInReservation(
#                 reservationId=sandbox_id,
#                 endpoints=[connection.Source, connection.Target],
#                 mappingType='bi'
#             )
# session.SetCustomShellAttribute(
#     modelName='Ixia Chassis Shell 2G',
#     attributeName='Execution Server Selector',
# )
# session.DeleteTopology(
#
# )

# for i in range(5):
#     blueprint_name = 'CloudShell Sandbox Template{0}'.format(str(i))
#     blueprint_details = None
#     try:
#         blueprint_details = session.GetTopologyDetails(blueprint_name)
#     except:
#         pass
#     if blueprint_details:
#         if blueprint_details.Apps.__len__() == 0 \
#                 and blueprint_details.Resources.__len__() == 0 \
#                 and blueprint_details.Services.__len__() == 0 \
#                 and blueprint_details.AbstractResources.__len__() == 0:
#             session.DeleteTopology(blueprint_details.Name)
# pass


pass