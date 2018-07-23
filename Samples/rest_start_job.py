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
new_job_id = new_job.text[1:-1]
job_state = ''
while job_state != 'Done':
    rr = requests.get('http://localhost:9000/API/Scheduling/Jobs/{0}'.format(new_job_id), headers=auth)
    job_state = json.loads(rr.content)['JobState']
    print job_state
    time.sleep(5)
report_id = json.loads(rr.content)['Tests'][0]['ReportId']
print (report_id)
r = requests.get('http://localhost:88/Test/Report?reportId={0}'.format(report_id), stream=True)
path = 'c:\\temp\\my_report_1.pdf'
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
pass