from cloudshell.api.cloudshell_api import CloudShellAPISession, ApiEditAppRequest, \
    ReservationAppResource, AppDetails, NameValuePair, DefaultDeployment, Deployment
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

res_id = '852464d3-5106-4a2b-8598-fdae7ea8cf9e'

session = CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
from cloudshell.api.cloudshell_api import CloudShellAPISession, ApiEditAppRequest, \
    ReservationAppResource, AppDetails, NameValuePair, DefaultDeployment, Deployment


def convert_get_to_set_app(app_object):
    '''
    :param ReservationAppResource app_object:
    :return ApiEditAppRequest:
    '''
    Attributes = [NameValuePair(Name=attr.Name, Value=attr.Value) for attr in app_object.LogicalResource.Attributes]
    default_deployment = [deployment for deployment in app_object.DeploymentPaths if deployment.IsDefault == True][0]
    deployment_attributes = [NameValuePair(Name=attr.Name, Value=attr.Value) for
                             attr in app_object.DeploymentPaths[0].DeploymentService.Attributes]
    new_deployment = Deployment(Attributes=deployment_attributes)

    app_request = ApiEditAppRequest(Name=app_object.Name,
                                    NewName=app_object.Name,
                                    Description=app_object.Description,
                                    AppDetails=AppDetails(ModelName=app_object.LogicalResource.Model,
                                                          Attributes=Attributes,
                                                          Driver=app_object.LogicalResource.Driver
                                                          ),
                                    DefaultDeployment=DefaultDeployment(Name=app_object.DeploymentPaths[0].Name,
                                                                        Deployment=new_deployment)
                                    )

    return app_request

def change_attribute(edit_app_object, attribute_name, attribute_value):
    '''
    :param str attribute_name:
    :param ApiEditAppRequest edit_app_object:
    :return:
    '''
    for attribute in edit_app_object.AppDetails.Attributes:
        if attribute_name == attribute.Name or '{0}.{1}'.format(edit_app_object.AppDetails.ModelName, attribute_name) == attribute.Name:
            attribute.Value = attribute_value
            print 'replaced password for app {}'.format(edit_app_object.Name)
    return edit_app_object

all_apps = session.GetReservationDetails(res_id).ReservationDescription.Apps
app_names = [app.Name for app in all_apps]
all_app_get_objects = session.GetAppsDetailsInReservation(
    reservationId=res_id,
    appNames=app_names
)
for app in all_app_get_objects.Apps:
    converted_object = convert_get_to_set_app(app)
    changed_converted_object = change_attribute(converted_object, 'Password', 'abcd12342314')
    session.EditAppsInReservation(
        reservationId=res_id,
        editAppsRequests=[changed_converted_object]
    )
qq = session.GetAppsDetailsInReservation(
    reservationId=res_id,
    appNames=app_names
)

pass
