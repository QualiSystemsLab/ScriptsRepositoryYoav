from cloudshell.core.logger import qs_logger
from cloudshell.api.cloudshell_api import InputNameValue, ResourceInfo, ServiceInstance, AttributeNameValue, \
    ApiEditAppRequest, ReservationAppResource, AppDetails, NameValuePair, DefaultDeployment, Deployment

class Blueprint_extra_commands():
    def __init__(self, resid):
        self.logger = qs_logger.get_qs_logger(
            log_group=resid,
            log_category='SkyBox_custom_Setup',
            log_file_prefix='Skybox_Setup'
        )

    def enforce_image_name(self, sandbox, components):
        self._enforce_image_name(sandbox, components)


    def _enforce_image_name(self, sandbox, components):
        '''
        :param Sandbox sandbox:
        :param components:
        :return:
        '''
        IMAGE_NAME = sandbox.global_inputs['Image Name']
        all_apps = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Apps
        app_names = [app.Name for app in all_apps]
        all_app_get_objects = sandbox.automation_api.GetAppsDetailsInReservation(
            reservationId=sandbox.id,
            appNames=app_names
        )

        for app in all_app_get_objects.Apps:
            self.logger.info('starting password change process for app {}'.format(app.Name))
            converted_object = self._convert_get_to_set_app(app)
            changed_converted_object = self._change_deploy_image(converted_object, IMAGE_NAME)
            # changed_converted_object = self._change_attribute(converted_object, 'Password', IMAGE_NAME)
            sandbox.automation_api.EditAppsInReservation(
                reservationId=sandbox.id,
                editAppsRequests=[changed_converted_object]
            )
            self.logger.info('password changed for app {0} to {1}'.format(app.Name, IMAGE_NAME))


    def _convert_get_to_set_app(self, app_object):
        '''
        :param ReservationAppResource app_object:
        :return ApiEditAppRequest:
        '''
        Attributes = [NameValuePair(Name=attr.Name, Value=attr.Value) for attr in app_object.LogicalResource.Attributes]
        default_deployment = [deployment for deployment in app_object.DeploymentPaths if deployment.IsDefault][0]
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

    def _change_deploy_image(self, edit_app_object, attribute_value):
        '''
        :param str attribute_name:
        :param ApiEditAppRequest edit_app_object:
        :return:
        '''
        for attribute in edit_app_object.DefaultDeployment.Deployment.Attributes:
            if attribute.Name == 'Azure Image':
                attribute.Value = attribute_value
                self.logger.info('replaced Image for app {}'.format(edit_app_object.Name))
        return edit_app_object


    def _change_attribute(self, edit_app_object, attribute_name, attribute_value):
        '''
        :param str attribute_name:
        :param ApiEditAppRequest edit_app_object:
        :return:
        '''
        for attribute in edit_app_object.AppDetails.Attributes:
            if attribute_name == attribute.Name or '{0}.{1}'.format(edit_app_object.AppDetails.ModelName,
                                                                    attribute_name) == attribute.Name:
                attribute.Value = attribute_value
                self.logger.info('replaced password for app {}'.format(edit_app_object.Name))
        return edit_app_object