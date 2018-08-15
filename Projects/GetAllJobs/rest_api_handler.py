import requests
import json
import time

class rest_handler():
    def __init__(self, login_data):
        self.server = login_data.get('server')
        self.login = requests.put('http://{0}:9000/API/Auth/Login'.format(self.server), data=login_data).text[1:-1]
        self.auth = {
                'Authorization': 'Basic {0}'.format(self.login)
        }

    def run_job(self, test_name, blueprint='', jobDuration="5",
                parameters=[], global_inputs=[], executionServers=[], testDuration="3"):
        test_parameters = []
        for parameter in parameters:
            test_parameters.append({"ParameterName": "{0}".format(parameter.Name),
                                    "ParameterValue": "{0}".format(parameter.Value)})
        bp_global_inputs = []
        for global_input in global_inputs:
            bp_global_inputs.append({"Name": "{0}".format(global_input.Name),
                                     "Value": "{0}".format(global_input.Value)})


        job_data ={
                    "name": "automated_job",
                    "description": "",
                    "executionServers": executionServers,
                    "loggingProfile": "All",
                    "estimatedDuration": "{}".format(jobDuration),
                    "stopOnFail": "false",
                    "stopOnError": "false",
                    "tests": [
                        {
                            "TestPath": "TestShell\\Tests\\Shared\\{0}".format(test_name),
                            "TestDuration": "{}".format(testDuration),
                            "Parameters": test_parameters
                        }
                    ],
                    "Topology": {
                        "Name": "{0}".format(blueprint),
                        "GlobalInputs": bp_global_inputs,
                        "RequirementsInput": [],
                        "AdditionalInput": []
                    },
                    "durationTimeBuffer": "2",
                    "emailNotifications": "All",
                    "type": "TestShell"
            }

        job_data_json = json.dumps(job_data)
        new_job = requests.post('http://{0}:9000/API/Scheduling/Queue'.format(self.server),
                                headers=self.auth,
                                json=json.loads(job_data_json))
        if new_job.status_code == 400:
            print (new_job.text)
        elif new_job.status_code == 200:
            return new_job

    def get_job_details(self, job_id):
        my_job = requests.get('http://{1}:9000/API/Scheduling/Jobs/{0}'.format(job_id, self.server),
                                headers=self.auth,
                                )
        return my_job

    def get_all_job_details(self):
        my_job = requests.get('http://{0}:9000/API/Scheduling/Executions'.format(self.server),
                                headers=self.auth,
                                )
        return my_job