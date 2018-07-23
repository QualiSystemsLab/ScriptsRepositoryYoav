import requests
import json
from quali_utils.quali_packaging import PackageEditor as qt

qt.add_attribute_to_abstract()
loginurl = 'http://qs.cisco.com:82/api'

data = {
    'username': 'admin',
    'password': 'admin',
    'domain': 'Global'
}
r = requests.put(url=loginurl + r'/login', json=data)

Aut_header = "Basic " + r.text.replace('"', '')
# need to ask the user what is the name of the environment that he want to get the details on

gs_url = loginurl + r'/v1/sandboxes'
r_get_sandboxes = requests.get(gs_url, headers={'Authorization': Aut_header})
asw = json.loads(r_get_sandboxes._content)

gb_url = loginurl + r'/v1/blueprints'
r_get_blueprints = requests.get(gb_url, headers={'Authorization': Aut_header})
ccc = json.loads(r_get_blueprints._content)
pass