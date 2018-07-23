import requests
import json
import time
login_data = {
    'username': 'admin',
    'password': 'admin',
    'domain': 'Global'
}
login = requests.put('http://localhost:9000/API/Auth/Login', data=login_data).text[1:-1]
auth = {
    'Authorization': 'Basic {0}'.format(login)
}
job_data = {
    "Package Path": r"C:\temp\Shells\NxOS Save and Restore.zip"
           }

job_data_json = json.dumps(job_data)
new_job = requests.post('http://localhost:9000/API/Package/ImportPackage', headers=auth, data=job_data)
pass