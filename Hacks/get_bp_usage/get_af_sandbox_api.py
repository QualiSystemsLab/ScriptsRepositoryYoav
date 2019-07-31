import requests
import json


class Rest_api_client():
    def __init__(self, username, password, domain='Global', host='Localhost'):
        self.login(username, password, domain, host)

    def login(self, username, password, domain='Global', host='Localhost'):
        login_url = 'http://{}:82/api/login'.format(host)
        self.base_url = 'http://{}:82/api/v2'.format(host)
        login_data = {
          "username": username,
          "password": password,
          "domain": domain
        }
        self.rest_session = requests.session()
        login_out = self.rest_session.put(
            url=login_url,
            json=login_data
        )
        token = login_out.content[1:-1]
        self.rest_session.headers.update({
            "Authorization": "Basic {}".format(token)
        })


    def get_all_sandboxes(self):
        '''
        :param requests.Session rest_session:
        :return:
        '''

        get_sandboxes_url = '/sandboxes'
        get_sandboxes_params = {
            "show_historic": "true"
        }
        all_sandboxes = self.rest_session.get(
            url = self.base_url + get_sandboxes_url,
            params=get_sandboxes_params
        )
        return all_sandboxes

    def get_sandboxes_from_blueprint(self, sandboxes, blueprint_id):
        relevant_sandboxes = []
        for sandbox in sandboxes:
            sandbox_blueprint = sandbox.get('blueprint')
            if sandbox_blueprint:
                sandbox_blueprint_id = sandbox_blueprint.get('id')
                if sandbox_blueprint_id == blueprint_id:
                    relevant_sandboxes.append(sandbox)
        return relevant_sandboxes


    def get_sandbox_activity_feed(self, sandbox):
        '''
        :param requests.Session rest_session:
        :param sandbox:
        :return:
        '''
        base_url = 'http://localhost:82/api/v2'
        af_url = '/sandboxes/{sandbox_identifier}/activity'.format(sandbox_identifier=sandbox)
        af_params = {
            "error_only": "true"
        }
        sb_af = self.rest_session.get(
            url=base_url + af_url,
            params=af_params
        )
        sb_af_json = json.loads(sb_af.content)
        return sb_af_json

    def get_af_error_digest(self, sandboxes_from_blueprint):
        report = ''
        for sb in sandboxes_from_blueprint:
            my_af = self.get_sandbox_activity_feed(sb)
            report += '<p>Report for Sandbox with ID {} :</p>'.format(sb)
            report += '<br /><br />'
            events = my_af.get('events')
            if events:
                report += '<table>'
                report += '<tr>'
                report += '<th> time </th>'
                report += '<th> event_type </th>'
                report += '<th> event_text </th>'
                report += '<th> output </th>'
                report += '</tr>'

                for event in events:
                    report += '<tr>'
                    # report += 'time:'
                    report += '<td>{}</td>'.format(event.get('time'))
                    # report += ' event_type:'
                    report += '<td>{}</td>'.format(event.get('event_type'))
                    # report += ' event_text:'
                    report += '<td>{}</td>'.format(event.get('event_text'))
                    # report += ' output:'
                    output = '<td>{}</td>'.format(event.get('output'))
                    if output:
                        report += event.get('output')
                    report += '</tr>'
                report += '</table>'
            report += '<br />'
        return report
