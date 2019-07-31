import requests
import json
import time

login_data = {
    'username': 'qualivpn',
    'password': 'Quali123!+',
    'domain': 'Global'
}
server = '10.13.1.198'
suite_name = 'Yoav_Test'

login = requests.put('http://{0}:9000/API/Auth/Login'.format(server), data=login_data).text[1:-1]
auth = {
    'Authorization': 'Basic {0}'.format(login)
}

suite_data_raw = requests.get('http://{1}:9000/API/Scheduling/SuiteTemplates/{0}'.format(suite_name, server),
                              headers=auth)
suite_data_raw = json.loads(suite_data_raw.content)

suite_data = '''
{'EndReservationullnd': True,
    'DomainId': 'dbaf480c-09f7-46d3-a2e2-e35d3e374a16',
    'Description': null,
              'EmailNotifications': 'ErrorsOnly',
              'ExistingReservationId': null,
              'CreateDate': '2019-04-11T12:23:58',
              'SuiteName': null,
              'ModificationDate': '2019-04-11T12:23:58',
              'Owner': 'qualivpn',
              'JobsDetails': [
                {'ExecutionServers': [],
                 'Name': 'JOB',
                 'EmailNotifications': null,
                 'Type': 'TestShell',
                 'Tests': [
                        {'EstimatedDuration': 3.0,
                         'Parameters': [],
                         'ReportLink': null,
                         'State': null,
                         'Result': null,
                         'StartTime': null,
                         'TestPath': 'TestShell\\Tests\\Shared\\CommonTests\\GetTopologyV9',
                         'EndTime': null,
                         'ReportId': null}],
                 'Description': null,
                 'LoggingProfile': 'Results',
                 'DurationTimeBuffer': 3.0,
                 'StopOnFail': False,
                 'Topology': {'GlobalInputs':
                                  [{'PossibleValues': ['[Any]',
                                                       '2x_Shielded_Box_1',
                                                       '2xAir4920_Box_WL',
                                                       '2xAir4830_Box_Izm_Cage2',
                                                       '4x_Shielded_Box_1',
                                                       '4x_Shielded_Box_2',
                                                       '2x_Shielded_Box_2',
                                                       '3x_Shielded_Box'],
                                                             'Name': 'location', 'Value': '[Any]'}],
                                           'Name': 'DVT_2xAir4XXX_Setup_PerCommit__TEST_BY_YOAV',
                              'AdditionalInput': [],
                              'RequirementsInput': [
                                               {'PossibleValues': ['[Any]', 'Air4920', 'Air4930', 'Air4830'],
                                                'Type': 'attribute', 'ResourcePath': 'Root node', 'Value': '[Any]',
                                                'Name': 'Model'},
                                               {'PossibleValues': [], 'Type': 'quantity', 'ResourcePath': 'WL Client',
                                                'Value': '0', 'Name': 'Quantity'}, {
                                                   'PossibleValues': ['[Any]', '2x_Shielded_Box_1', '2xAir4920_Box_WL',
                                                                      '2xAir4830_Box_Izm_Cage2', '4x_Shielded_Box_1',
                                                                      '4x_Shielded_Box_2', '2x_Shielded_Box_2',
                                                                      '3x_Shielded_Box'], 'Type': 'attribute',
                                                   'ResourcePath': 'Root node', 'Value': '', 'Name': 'Location'}]},
              'StopOnError': False,
              'EstimatedDuration': -1.0}],
              'Type': 'TestShell',
              'RemoveJobsFromQueueAfter': -1.0,
              'SuiteTemplateName': 'Yoav_Test'
  }
'''

suite_data_json = json.loads(suite_data)

new_suite = requests.post('http://{}:9000/API/Scheduling/Suites',
                          headers=auth,
                          data=json.loads(suite_data_json))

pass


# new_job = requests.post('http://{}:9000/API/Scheduling/Queue', headers=auth, json=json.loads(job_data_json))
# new_job_id = new_job.text[1:-1]
# job_state = ''
# while job_state != 'Done':
#     rr = requests.get('http://{1}:9000/API/Scheduling/Jobs/{0}'.format(new_job_id, server), headers=auth)
#     job_state = json.loads(rr.content)['JobState']
#     print job_state
#     time.sleep(5)
# report_id = json.loads(rr.content)['Tests'][0]['ReportId']
# print (report_id)
# r = requests.get('http://{1}:88/Test/Report?reportId={0}'.format(report_id, server), stream=True)
# path = 'c:\\temp\\my_report_1.pdf'
# if r.status_code == 200:
#     with open(path, 'wb') as f:
#         for chunk in r.iter_content(1024):
#             f.write(chunk)
# pass
