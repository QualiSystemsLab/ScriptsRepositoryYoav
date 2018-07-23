import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sch

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
resid = '688e3112-e7d4-4d5d-a9f3-671c33bc1549'
all_apps = session.GetReservationDetails(resid).ReservationDescription.Apps
for i,app in enumerate(all_apps):
    session.EditAppsInReservation(
        reservationId=resid,
        editAppsRequests=[api.ApiEditAppRequest(
            Name=app.Name,
            NewName='New_App_Name_{0}'.format(str(i)),
            Description=app.Description,
            AppDetails=app.LogicalResource,
            DefaultDeployment=app.DeploymentPaths[0]
        )]
    )
pass