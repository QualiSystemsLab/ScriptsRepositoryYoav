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
job_data ={
            "name": "job1",
            "description": "",
            "executionServers": [],
            "loggingProfile": "All",
            "estimatedDuration": "2",
            "stopOnFail": "false",
            "stopOnError": "false",
            "tests": [
                {
                    "TestPath": "TestShell\\Tests\\Shared\\ASharedTest",
                    "TestDuration": "3",
                    "Parameters": []
                }
            ],
            "topology": "",
            "durationTimeBuffer": "2",
            "emailNotifications": "All",
            "type": "TestShell"
    }

job_data_json = json.dumps(job_data)
new_job = requests.post('http://localhost:9000/API/Scheduling/Queue', headers=auth, json=json.loads(job_data_json))
