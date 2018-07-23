# in Debug - getting a session
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

def simply_change_app_name(session, resid, app, new_name):
    session.EditAppsInReservation(
        reservationId=resid,
        editAppsRequests=[
            api.ApiEditAppRequest(
                Name=app.Name,
                NewName=new_name,
                Description=app.Description,
                AppDetails=app,
                DefaultDeployment=app.DeploymentPaths[0]
        )
        ]
    )


resid = 'b1519814-f423-498e-aea8-7b16cccd6aa0'
all_apps = session.GetReservationDetails(resid).ReservationDescription.Apps
for app in all_apps:
    simply_change_app_name(
        session=session,
        app=app,
        new_name='some new name',
        resid=resid
    )

pass