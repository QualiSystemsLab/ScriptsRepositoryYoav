import cloudshell.api.cloudshell_api as api
username = 'admin'
password = 'admin'
server = '10.212.224.224'
domain = 'Global'


session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

print session.GetResourceDetails('IPT-ZBL124-M-SW-52').Address
pass_attr = [attr.Value for attr in session.GetResourceDetails('ipd-zbl1313-r-rr-32').ResourceAttributes if attr.Name.__contains__('Password')][0]
password = session.DecryptPassword(pass_attr).Value
print password