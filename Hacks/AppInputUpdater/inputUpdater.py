import json
import os
import cloudshell.api.cloudshell_api as api
import drivercontext


class InputUpdater:

    def initialize(self, context):
        """
        :type context: drivercontext.InitCommandContext
        """
        pass

    def change_app_input_value(self, AppName, attr_name, attr_value, context):
        """
        :type context: drivercontext.ResourceCommandContext
        """
        edit_list = []
        session = api.CloudShellAPISession(context.connectivity.server_address,
                                           token_id=context.connectivity.admin_auth_token,
                                           domain=context.reservation.domain)
        Appdetails = session.GetAppsDetailsInReservation(context.reservation.reservation_id,[AppName])
        DeployModel = Appdetails.Apps[0].DeploymentPaths[0].DeploymentService.Model
        AppModel = Appdetails.Apps[0].LogicalResource.Model
        session.WriteMessageToReservationOutput(context.reservation.reservation_id,DeployModel)
        edit_vals = api.ApiEditAppRequest(AppName,
                                          AppName,
                                          '',
                                          api.AppDetails(ModelName=AppModel,
                                                         Attributes=[],
                                                         Driver=''),
                                          api.DefaultDeployment(DeployModel,
                                                                api.Deployment(
                                                                    [api.NameValuePair(attr_name, attr_value)]
                                                                ),
                                                                Installation=None
                                                                )
                                          )
        edit_list.append(edit_vals)
        qq = session.EditAppsInReservation(
            reservationId=context.reservation.reservation_id,
            editAppsRequests=edit_list
        )
        session.RemoveResourcesFromReservation(

        )
        return qq

    def cleanup(self):
        pass