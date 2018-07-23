import cloudshell.api.cloudshell_api as api7

# Destination details
d_username = 'admin'
d_password = 'admin'
d_server = 'qs.cisco.com'
d_domain = 'Global'

d_session = api7.CloudShellAPISession(d_server, d_username, d_password, d_domain)

group_dict = {}
domains_dict = {}
emailed_users = []
cs_groups = list()
cs_domains = list()

CS_users = d_session.GetAllUsersDetails()

for CS_user in CS_users.Users:
    emailed_users.append(CS_user.Email)

print ','.join(str(p) for p in emailed_users)
pass