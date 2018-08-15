import rest_api_handler
import json

with open('creds.json', 'r') as creds:
    login_data = json.loads(creds.read())

rest_handler = rest_api_handler.rest_handler(login_data)
a = json.loads(rest_handler.get_all_job_details().content)
pass