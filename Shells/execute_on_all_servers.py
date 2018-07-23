import cloudshell.api.cloudshell_api as api
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

all_obelix_servers = session.FindResources(
    resourceModel='Obelix'
).Resources
reservation = session.CreateImmediateReservation(
    reservationName='update_all_obelix',
    owner='admin',
    durationInMinutes=15
)
for ob in all_obelix_servers:
    session.ExecuteCommand(
        reservationId=reservation.Reservation.Id,
        targetName=ob.Name,
        targetType='Resource',
        commandName='update_server_stbs'
    )
session.EndReservation(
    reservationId=reservation.Reservation.Id
)
pass