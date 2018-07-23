import cloudshell.api.cloudshell_api as api

def get_cs_api_session():
    username = 'admin'
    password = 'admin'
    server = 'localhost'
    domain = 'Global'

    session = api.CloudShellAPISession(
        username=username,
        password=password,
        domain=domain,
        host=server
    )
    return session



resid = 'fff7eea5-db15-436d-9e2b-065995644e88'

session = get_cs_api_session()
aa = (session.GetResourceCommands('NxOS Simulator').Commands)
def save():
    return session.ExecuteCommand(
    reservationId=resid,
    targetType='Resource',
    targetName='NxOS Simulator',
    commandName='save',
    commandInputs=[
        api.InputNameValue('folder_path', 'tftp://172.16.1.20'),
        api.InputNameValue('configuration_type', 'Startup'),
        api.InputNameValue('vrf_management_name', 'management')
    ]

).Output

def restore(filename):
    session.ExecuteCommand(
        reservationId=resid,
        targetType='Resource',
        targetName='NxOS Simulator',
        commandName='restore',
        commandInputs=[
            api.InputNameValue('path', 'tftp://172.16.1.21/{0}'.format(filename)),
            api.InputNameValue('configuration_type', 'Running'),
            api.InputNameValue('restore_method', 'Append'),
            api.InputNameValue('vrf_management_name', 'management')
        ]

    )
restore('NxOSbase')
# strtup = save()
pass