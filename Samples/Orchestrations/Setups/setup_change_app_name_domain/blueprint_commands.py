from cloudshell.api.cloudshell_api import InputNameValue, ApiEditAppRequest



def change_app_name(sandbox, components):
    all_apps = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Apps
    domain = sandbox.reservationContextDetails.domain
    for i, app in enumerate(all_apps):
        sandbox.automation_api.EditAppsInReservation(
            reservationId=sandbox.id,
            editAppsRequests=[ApiEditAppRequest(
                Name=app.Name,
                NewName='New_App_Domain_{1}_{0}'.format(str(i), domain),
                Description=app.Description,
                AppDetails=app.LogicalResource,
                DefaultDeployment=app.DeploymentPaths[0]
            )]
        )



