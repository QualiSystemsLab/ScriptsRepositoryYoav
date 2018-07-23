import requests
import json
from datetime import datetime
import dateutil.parser


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
login_data = {
  "username": "",
  "password": "",
  "domain": "Global"
}
login_URL = 'http://localhost:82/api/login'
token = requests.put(url=login_URL,
                     headers=headers,
                     data=json.dumps(login_data)
                     ).text
auth_header = {'Authorization': 'Basic {0}'.format(token[1:-1])}
headers.update(auth_header)
orch_events = []
other_events = []
all_names = ['Setup', 'Teardown']
time_diffs = []

Base_URL = 'http://localhost:82/api/v2'
sbox_id = 'a1e39f61-69b0-4c5d-8dc4-0a1cfade43a8'
AF_URL = '/sandboxes/{sandbox_identifier}/activity'.format(sandbox_identifier=sbox_id)
my_AF = json.loads(requests.get(url=Base_URL + AF_URL,
                     headers=headers,
                     ).text)
for event in my_AF['events']:
    start_end = 'start' if event['event_text'].__contains__('start') else 'end' if event['event_text'].__contains__(
        'end') or event['event_text'].__contains__('completed') else None
    if event['event_text'].startswith('\'Setup\''):
        if start_end:
            orch_events.append({'Name': 'Setup',
                             'state': start_end,
                             'Timestamp': event['time']})
    elif event['event_text'].startswith('The setup'):
        component_name = event['event_text'].split('stage')[1].split('has')[0].strip()
        all_names.append(component_name)
        if start_end:
            orch_events.append({'Name': component_name,
                                 'state': start_end,
                                 'Timestamp': event['time']})
    elif event['event_text'].__contains__('\'Teardown\''):
        if start_end:
            orch_events.append({'Name': 'Teardown',
                                'state': start_end,
                                'Timestamp': event['time']})
    else:
        other_events.append(event)
all_names = list(set(all_names))
for name in all_names:
    start_time = dateutil.parser.parse([x for x in orch_events if x['Name'] == name and x['state'] == 'start'][0]['Timestamp'])
    end_time = dateutil.parser.parse([x for x in orch_events if x['Name'] == name and x['state'] == 'end'][0]['Timestamp'])
    diff = end_time - start_time
    time_diffs.append({'Name': name, 'Time_Taken': diff})
pass