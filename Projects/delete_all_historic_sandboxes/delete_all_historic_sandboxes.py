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
    "Authorization": "Basic {}".format(login_response)
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
