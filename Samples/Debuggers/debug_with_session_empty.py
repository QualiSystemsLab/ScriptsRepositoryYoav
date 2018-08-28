import cloudshell.api.cloudshell_api as api

username = 'nati.k'
password = '1111'
server = '40.113.155.10'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

res_det = session.GetReservationDetails('5f4b9ad5-7dbd-43c8-a36d-e5aaf9c7e155').ReservationDescription.Services

pass