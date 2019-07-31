import requests
import json

class get_activity():
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        self.login_data = {
            "username": "yoav.e",
            "password": "1234",
            "domain": "Global"
        }
        self.hostname = '40.91.201.107'
        self.port = '82'

    def convert_af_to_html(self, sbox_id):
        login_URL = 'http://{0}:{1}/api/login'.format(self.hostname, self.port)
        token = requests.put(url=login_URL,
                             headers=self.headers,
                             data=json.dumps(self.login_data)
                             ).text
        auth_header = {'Authorization': 'Basic {0}'.format(token[1:-1])}
        self.headers.update(auth_header)
        Base_URL = 'http://{0}:{1}/api/v2'.format(self.hostname, self.port)
        AF_URL = '/sandboxes/{sandbox_identifier}/activity'.format(sandbox_identifier=sbox_id)
        my_AF = json.loads(requests.get(url=Base_URL + AF_URL, headers=self.headers).text)
        my_events = my_AF.get('events')
        html = self.create_html(my_events)
        file = open('af_for_sandbox_{}.html'.format(sbox_id), 'w')
        file.write(html)
        file.close()

    def create_html(self, events):
        html_page = '<!DOCTYPE html>\n<head>\n<title>Title</title>\n</head>\n'
        html_page += '<body>\n<table>\n'
        headers = events[0].keys()
        # create headers
        html_page += '<tr>\n'
        for header in headers:
            html_page += '<td>{}</td>\n'.format(header)
        html_page += '</tr>\n'
        for event in events:
            html_page += '<tr>\n'
            for item in event:
                html_page += '<td>{}</td>\n'.format(event[item])
            html_page += '</tr>\n'
        html_page += '</table>\n</body>\n</html>\n'
        return html_page

sbox_id = '9d90821c-7a4f-4c51-92c7-e4b9ff352a3b'
af = get_activity()
af.convert_af_to_html(sbox_id)
pass