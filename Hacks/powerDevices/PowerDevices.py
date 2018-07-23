import json
import os
import cloudshell.api.cloudshell_api as api


# Production
# reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
# # resource_context = json.loads(os.environ['RESOURCECONTEXT'])
# connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])


#
# session = api.CloudShellAPISession(server, username, password, domain)
# debug:
# session = api.CloudShellAPISession('qs.cisco.com', 'admin', 'admin', 'Global')




def Power_Physical_Devices():
    # AppName = os.environ['App_Name']
    # attr_name = os.environ['Attribute_Name']
    # attr_value = os.environ['New_Image_Name']
    # auto_deploy = os.environ['Auto_deploy']
    # session = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
    #                                    token_id=connectivity_details['adminAuthToken'],
    #                                    domain=reservation_details['domain'])
    physical_resources = []
    session = api.CloudShellAPISession('qs.cisco.com', 'admin', 'admin', 'Global')
    qq = session.GetReservationDetails(
        reservationId='9fd08e7c-e35e-4027-8531-b394731890a7'
    )
    for res in qq.ReservationDescription.Resources:
        res_det = session.GetResourceDetails(res.Name)
        for child in res_det.ChildResources:
            if child.ResourceFamilyName == 'Power Port':
                physical_resources.append(res.Name)
    if physical_resources:
        for phys_res in physical_resources:
            session.ExecuteResourceConnectedCommand(
                reservationId='',
                resourceFullPath=phys_res.Name,
                commandName='',
                commandName='power',
            )
    pass

Power_Physical_Devices()
pass