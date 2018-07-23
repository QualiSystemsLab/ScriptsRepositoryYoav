import json
import re
import datetime
str_to_update = {
                    "664d591d-1f81-44e0-9677-0b4f4d61806d": "38",
                    "b351adb4-fc97-4a01-961a-83be5ccbd250": "TorkPRODUSADEMO",
                    "ffd961ef-4816-4035-ae1e-59d1d0ef9f19": "#{Empty}"
                }


def _compare_versions(self, current_version, new_version):
    parts_of_current_version = current_version.split('.')
    parts_of_new_version = new_version.split('.')
    for i, vers in enumerate(parts_of_current_version):
        if int(vers) > int(parts_of_new_version[i]):
            return current_version
        elif int(vers) < int(parts_of_new_version[i]):
            return new_version

def combine_dicts(*dicts):
    return reduce(lambda dict1, dict2: dict(zip(dict1.keys() + dict2.keys(), dict1.values() + dict2.values())), dicts)

leProject = 'Projects-204'
leEnv = 'Environments-233'
jfile = open(r"D:\temp\SCA_find_package_trail\project_TOL_websites_releases.txt", "r")
jfile_snd = open(r"D:\temp\SCA_find_package_trail\project_TOL_websites_release_deployment_ok.txt", "r")
jfile_trd = open(r"D:\temp\SCA_find_package_trail\project_TOL_websites_release_deployment_ok2.txt", "r")
jfile_alld = open(r"D:\temp\SCA_find_package_trail\all_deployments.txt", "r")
# jfile_snd = open(r"D:\temp\SCA_find_package_trail\project_TOL_websites_release_deployment_NOT.txt", "r")
myjson = json.load(jfile)
next_json = json.load(jfile_snd)
last_json = json.load(jfile_trd)
alld = json.load(jfile_alld)
# allVars = myjson['Items']
environment_id = 'Environments-162'
latest_version = '0.0.0.0'
env_exists = 0
latest_date = datetime.datetime(1970, 1, 1)
all_deployments = {'Items': alld}
for deploy_item in all_deployments['Items']:
    my_environment = deploy_item['EnvironmentId']
    if environment_id == my_environment:
        my_date = deploy_item['Created']
        my_formatted_date = datetime.datetime(int(my_date.split('-')[0]),
                                              int(my_date.split('-')[1]),
                                              int(my_date.split('-')[2].split('T')[0]),
                                              int(my_date.split('T')[1].split(':')[0]),
                                              int(my_date.split('T')[1].split(':')[1]),
                                              int(my_date.split('T')[1].split(':')[2].split('.')[0])
                                              )
        latest_date = my_formatted_date if my_formatted_date > latest_date else latest_date
        if my_formatted_date == latest_date:
            a = 14
            latest_package_name = package['SelectedPackages'][0]['Version']














for var in myjson['Items']:
    # if re.match("^[\.0-9_-]*$", var['Version']):
    #     k = var['SelectedPackages'][0]['Version']
        for t in next_json['Items']:
            my_environment = t['EnvironmentId']
            my_date = t['Created']
            my_formatted_date = datetime.datetime(int(my_date.split('-')[0]),
                                                  int(my_date.split('-')[1]),
                                                  int(my_date.split('-')[2].split('T')[0]),
                                                  int(my_date.split('T')[1].split(':')[0]),
                                                  int(my_date.split('T')[1].split(':')[1]),
                                                  int(my_date.split('T')[1].split(':')[2].split('.')[0])
                                                  )
            latest_date = my_formatted_date if my_formatted_date > base_datetime else base_datetime
            pass
        my_version = '{0}'.format(var['SelectedPackages'][0]['Version'])
        latest_version = _compare_versions('a', latest_version, my_version)

myjson.update(str_to_update)
pass





















# /api/feeds/feeds-nexus/packages?packageId=TOL.Web.Demo


#
# a = '1.5.1'
# b = '1.5.30'
#
# def compare_versions(current_version, new_version):
#     parts_of_current_version = current_version.split('.')
#     parts_of_new_version = new_version.split('.')
#     for i, vers in enumerate(parts_of_current_version):
#         if int(vers) > int(parts_of_new_version[i]):
#             return current_version
#         elif int(vers) < int(parts_of_new_version[i]):
#             return new_version
#
# c = compare_versions(a, b)
# pass