import pandas as pd
import requests


class policy_object():
    def __init__(self):
        self.source = ''
        self.destination = ''
        self.services = []
        self.action_allow = False
        self.VPN_Enabled = True


def create_policy_objects_list(env_name):
    link_to_excel = 'https://github.com/NationOfJoe/jsonTemplates/blob/master/firewall_policies/{env_name}.xlsx?raw=true'.format(env_name=env_name)
    df = pd.read_excel(link_to_excel, sheet_name='checkpoint')
    headers = df.columns
    policy_objects = []
    for index, row in df.iterrows():
        temp_policy_object = policy_object()
        temp_policy_object.source = row['Source']
        temp_policy_object.destination = row['Destination']
        if isinstance(row['Services'], float):
            temp_policy_object.services = []
        else:
            temp_policy_object.services = row['Services'].split(',')

        if row['Action'] == 'Allow':
            temp_policy_object.action_allow = True
        else:
            temp_policy_object.action_allow = False
        if row['VPN'] == 'Enabled':
            temp_policy_object.VPN_Enabled = True
        else:
            temp_policy_object.VPN_Enabled = False
        policy_objects.append(temp_policy_object)
    return policy_objects


policy_objs = create_policy_objects_list('Skybox_vLab_1.1')
pass

