import requests
import json


base_url = 'http://localhost:82/api/'
rest_session = requests.session()

rest_session.headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
login_data = {
  "username": "admin",
  "password": "admin",
  "domain": "Global"
}
login_json = json.dumps(login_data)
login_response = rest_session.put(
    url= "{0}login".format(base_url),
    data= login_json,
    headers=rest_session.headers
)
auth_header = {"Authorization": "Basic {}".format(login_response.text[1:-1])}
rest_session.headers.update(auth_header)

all_blueprints = json.loads(rest_session.get(
    url= "{}v2/blueprints".format(base_url)
).text)
my_blueprint = [bp for bp in all_blueprints if bp['name'] == 'sandbox_api_exercise'][0]
blueprint_id = my_blueprint['id']
# reserve this blueprint
reserve_body = json.dumps({
  "duration": "PT23H",
  "name": "training Sandbox",
})

reserve = rest_session.post(
    url="{base}v2/blueprints/{blueprint_identifier}/start".format(
        blueprint_identifier=blueprint_id,
        base=base_url
    ),
    data=reserve_body
)

# obtain the sandbox id
sandbox_id = json.loads(reserve.content)['id']

# get sandbox commands
commands = json.loads(rest_session.get(
    url="{base}v2/sandboxes/{sandbox_identifier}/commands".format(
        sandbox_identifier=sandbox_id,
        base=base_url
    )
).content)

# run command

run_command = rest_session.post(
    url="{base}v2/sandboxes/{sandbox_id}/commands/{command_name}/start".format(
        sandbox_id=sandbox_id,
        command_name='Run Tests',
        base=base_url
    )
)

# tear down the sandbox
unreserve = rest_session.post(
    url="{base}v2/sandboxes/{sandbox_id}/stop".format(
        sandbox_id=sandbox_id,
        base=base_url
    )
)


pass