import qualipy.api.cloudshell_api as api_6
import cloudshell.api.cloudshell_api as api_7

class res_type():
    def __init__(self, Family, Model):
        self.Family = Family
        self.Model = Model

username = 'admin'
password = 'admin'
server_6 = 'q1.cisco.com'
server_7 = 'qs.cisco.com'
O_domain = 'Global'
N_domain = 'Global'

session_6 = api_6.CloudShellAPISession(server_6, username, password, O_domain)
session_7 = api_7.CloudShellAPISession(server_7, username, password, N_domain)

to_inventory = []
to_inventory.append(res_type('Switch', 'Cisco IOS Switch'))
to_inventory.append(res_type('Switch', 'Cisco NXOS Switch'))
to_inventory.append(res_type('SSP Chassis', 'all'))
to_inventory.append(res_type('Firewalls', 'all'))
to_inventory.append(res_type('Terminal Server', 'all'))
to_inventory.append(res_type('Power Controller', 'all'))

for item in to_inventory:
    if item.Model == 'all':
        inv_value = session_6.FindResources(resourceFamily=item.Family).Resources.__len__()
    else:
        inv_value = session_6.FindResources(resourceFamily=item.Family, resourceModel=item.Model).Resources.__len__()
    print ('there are {0} items for family {1} and model {2}'.format(str(inv_value), item.Family, item.Model))

users = session_7.GetAllUsersDetails()
print ('there are {0} users'.format(str(users.Users.__len__())))
pass

