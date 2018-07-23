import requests
import json
import time
# login data to login to cloudshell
login_data = {
    'username': 'admin',
    'password': 'admin',
    'domain': 'Global'
}
# actual login action
login = requests.put('http://localhost:9000/API/Auth/Login', data=login_data).text[1:-1]
# login token - used as pass against the quali server
auth = {
    'Authorization': 'Basic {0}'.format(login)
}
# ad-hoc job data that we are about to run. should customize and change 
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
# actual post request on above data localhost is my local server , should be replaced with your quali server adress (same port , 9000)
new_job = requests.post('http://localhost:9000/API/Scheduling/Queue', headers=auth, json=json.loads(job_data_json))
# getting job ID from the one previously executed. so we can poll it and get report data when complete
new_job_id = new_job.text[1:-1]
job_state = ''
# polling job status. when it will complete , we can get the report
while job_state != 'Done':
    rr = requests.get('http://localhost:9000/API/Scheduling/Jobs/{0}'.format(new_job_id), headers=auth )
    job_state = json.loads(rr.content)['JobState']
    print job_state
    time.sleep(5)
# after the job completed , we can get the report
report_id = json.loads(rr.content)['Tests'][0]['ReportId']
print (report_id)
# we use the report_id to get the specific report from the server localhost:88 is my local server , should be replaced with your server
r = requests.get('http://localhost:88/Test/Report?reportId={0}'.format(report_id), stream=True)
path = 'c:\\temp\\my_report_1.pdf'
# if the call was successful , there is a file , and will write it to 'path'
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
pass