import requests
import json
from datetime import datetime
import dateutil.parser
import time


class AF_handler():
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        login_data = {
          "username": "admin",
          "password": "admin",
          "domain": "Global"
        }
        login_URL = 'http://localhost:82/api/login'
        token = requests.put(url=login_URL,
                             headers=self.headers,
                             data=json.dumps(login_data)
                             ).text
        auth_header = {'Authorization': 'Basic {0}'.format(token[1:-1])}
        self.headers.update(auth_header)
        self.orch_events = []
        self.det_orch_events = []
        self.other_events = []
        self.all_names = ['Setup', 'Teardown']
        self.Base_URL = 'http://localhost:82/api/v2'

    def get_af_times(self, sbox_id):
        self.orch_events = []
        self.det_orch_events = []
        time_diffs = []
        AF_URL = '/sandboxes/{sandbox_identifier}/activity'.format(sandbox_identifier=sbox_id)
        time.sleep(1)
        my_AF = json.loads(requests.get(url=self.Base_URL + AF_URL,
                             headers=self.headers,
                             ).text)
        for event in my_AF['events']:
            start_end = 'start' if event['event_text'].__contains__('start') else 'end' if event['event_text'].__contains__(
                'end') or event['event_text'].__contains__('completed') else None
            if event['event_text'].startswith('\'Setup\''):
                if start_end:
                    self.orch_events.append({'Name': 'Setup',
                                     'state': start_end,
                                     'Timestamp': event['time']})
            elif event['event_text'].startswith('The setup'):
                component_name = event['event_text'].split('stage')[1].split('has')[0].strip()
                self.all_names.append(component_name)
                if start_end:
                    self.det_orch_events.append({'Name': component_name,
                                             'state': start_end,
                                             'Timestamp': event['time']})
            elif event['event_text'].__contains__('\'Teardown\''):
                if start_end:
                    self.orch_events.append({'Name': 'Teardown',
                                             'state': start_end,
                                             'Timestamp': event['time']})
            else:
                self.other_events.append(event)
        all_names = list(set(self.all_names))
        for name in all_names:
            start_y = None
            end_y = None
            for x in self.orch_events:
                if x['Name'] == name and x['state'] == 'start':
                    start_y = x['Timestamp']
                if x['Name'] == name and x['state'] == 'end':
                    end_y = x['Timestamp']

            if start_y and end_y:
                start_time = dateutil.parser.parse(start_y)
                end_time = dateutil.parser.parse(end_y)
                diff = end_time - start_time
                time_diffs.append({'Name': name,
                                   'Time_Taken': diff,
                                   'Start': start_time,
                                   'End': end_time,
                                   'Sandbox_ID': sbox_id})
        return time_diffs

    def get_all_sandboxes_from_blueprint(self):
        AF_URL = '/sandboxes/'
        my_AF = json.loads(requests.get(url=self.Base_URL + AF_URL,
                                        headers=self.headers,
                                        params=(
                                            ('show_historic', 'true'),
                                        )
                             ).text)
        return my_AF

    def get_blueprint_name_from_id(self, bp_id):
        AF_URL = '/blueprints/{blueprint_identifier}/'.format(blueprint_identifier=bp_id)
        my_AF = json.loads(requests.get(url=self.Base_URL + AF_URL,
                                        headers=self.headers,
                                        params=(
                                            ('show_historic', 'true'),
                                        )
                             ).text)
        if 'message' in my_AF:
            my_AF = None
        return my_AF