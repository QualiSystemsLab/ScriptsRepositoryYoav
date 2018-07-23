import requests
import json
import os

dashboards_path = "C:\Users\yoav.e\Downloads\CloudShell Insight 8.0\CloudShell Insight 8.0\Dashboards"
folder_dashboards = os.listdir(dashboards_path)
all_dashboards = []
for dash in folder_dashboards:
    dash_file = open('{0}\{1}'.format(dashboards_path, dash), 'r')
    dash_content = dash_file.read()
    all_dashboards.append(dash_content)
    dash_file.close()

sisense_base = 'http://localhost:8081/api/v1'
login_data = {
    "username": "yoav.e@quali.com",
    "password": "Quali123"
}
user = 'yoav.e@quali.com'
password = 'Quali123'

login_url = '/authentication/login'

session = requests.session()
login_response = session.post(
    url=sisense_base + login_url,
    data=login_data
)
access_token = json.loads(login_response.text).get('access_token')
session.headers.update(
{
    "Authorization": "Bearer {}".format(access_token)
}
)
req_url = sisense_base + '/dashboards'.format('5ae57d86f53977000000004a')
get_dashboard = session.get(
    url=req_url
)
all_dboards = json.loads(get_dashboard.text)
for dashboard in all_dashboards:
    pass
pass