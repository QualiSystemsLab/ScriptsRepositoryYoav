import requests
import json

class sandbox_api():
    def __init__(self, server, username, password, domain):
        self.base_url = 'http://{}:82/api/'.format(server)
        self.rest_session = requests.session()

        self.rest_session.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
}
        self.login_data = {
          "username": "{}".format(username),
          "password": "{}".format(password),
          "domain": "{}".format(domain)
        }
        self.login_json = json.dumps(self.login_data)
        login_response = self.rest_session.put(
            url= "{0}login".format(self.base_url),
            data= self.login_json
        )
        auth_header = {"Authorization": "Basic {}".format(login_response.text[1:-1])}
        self.rest_session.headers.update(auth_header)

    def get_blueprints(self):
        all_blueprints = json.loads(self.rest_session.get(
            url= "{}v2/blueprints".format(self.base_url)
        ).text)
        return all_blueprints


    def reserve(self, blueprint_id):
        # reserve this blueprint
        reserve_body = json.dumps({
          "duration": "PT23H",
          "name": "training Sandbox",
        })

        reserve = self.rest_session.post(
            url="{base}v2/blueprints/{blueprint_identifier}/start".format(
                blueprint_identifier=blueprint_id,
                base=self.base_url
            ),
            data=reserve_body
        )

        result_json = json.loads(reserve.content)
        if reserve.status_code == 200:

            # obtain the sandbox id
            sandbox_id = result_json['id']
        else:
            raise Exception(reserve.text)
        return sandbox_id

    # get sandbox commands
    def get_sandbox_commands(self, sandbox_id):
        commands = json.loads(self.rest_session.get(
            url="{base}v2/sandboxes/{sandbox_identifier}/commands".format(
                sandbox_identifier=sandbox_id,
                base=self.base_url
            )
        ).content)
        return commands
    # run command

    def run_blueprint_command(self, sandbox_id, command):
        run_command = self.rest_session.post(
            url="{base}v2/sandboxes/{sandbox_id}/commands/{command_name}/start".format(
                sandbox_id=sandbox_id,
                command_name=command,
                base=self.base_url
            )
        )
        return run_command

    # tear down the sandbox
    def end_sandbox(self, sandbox_id):
        unreserve = self.rest_session.post(
            url="{base}v2/sandboxes/{sandbox_id}/stop".format(
                sandbox_id=sandbox_id,
                base=self.base_url
            )
    )



