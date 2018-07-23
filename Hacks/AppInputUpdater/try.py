import cloudshell.api.cloudshell_api as api

username = 'admin'
password = 'admin'
server = '192.168.85.6'
domain = 'Global'

session = api.CloudShellAPISession(server, username, password, domain)
res_id = '05a48690-7b72-4f92-9848-a7e1df590cc9'
qq = session.GetAppsDetailsInReservation(reservationId=res_id, appNames=['SomeApp'])
pass

