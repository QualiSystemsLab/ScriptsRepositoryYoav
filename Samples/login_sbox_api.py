import requests
import json

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
pass