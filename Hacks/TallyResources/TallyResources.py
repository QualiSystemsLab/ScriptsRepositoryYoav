import cloudshell.api.cloudshell_api as api
username = 'admin'
password = 'admin'
server = 'qs.cisco.com'
O_domain = 'Global'
N_domain = 'Global'
session = api.CloudShellAPISession(server, username, password, N_domain)
session.E
families = ['switch',
            'Firewalls',
            'SSP Chassis',
            'SSP CI Regression VMs',
            'Terminal Server',
            'Generic App Family',
            'Virtual Machine Instance',
            'VMs',
            'Web Security Appliance'
            ]
total_tally = 0
for family in families:
    try:
        all_items = session.FindResources(resourceFamily=family, maxResults=2000)
        print ('from family {0} there are {1} resources'.format(family, all_items.Resources.__len__()))
        total_tally += all_items.Resources.__len__()
    except:
        pass
print ('total tally of resources counted: {} resources'.format(total_tally))