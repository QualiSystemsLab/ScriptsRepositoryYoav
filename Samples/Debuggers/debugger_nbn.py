import cloudshell.api.cloudshell_api as api


username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'
new_server = 'localhost'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

resid = 'afbe67f8-c6b5-4014-9d9f-c37943f51f06'

session.SetReservationLiveStatus(
    liveStatusName='Progress 20',
    additionalInfo='this is a live status',
    reservationId=resid
)