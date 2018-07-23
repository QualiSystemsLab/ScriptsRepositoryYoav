from cloudshell.api.cloudshell_api import InputNameValue
# from cloudshell.workflow.orchestration.sandbox import Sandbox
from os import listdir
from os.path import isfile, join


# Michael
# Yoav add Solve abstract TGN

def Deploy_DHCP_First(sandbox, components):
    """
    :param Sandbox sandbox:
    :param Components components:
    :return:
    """
    res_det = sandbox.automation_api.GetReservationDetails(sandbox.id)
    DHCP_apps = [dhcp for dhcp in res_det.ReservationDescription.Apps if dhcp.LogicalResource.Model == 'DHCP Server']
    if DHCP_apps.__len__() > 0:
        DHCP_app = DHCP_apps[0]
        sandbox.automation_api.DeployAppToCloudProvider(
            reservationId=sandbox.id,
            appName=DHCP_app.Name,
            commandInputs=[],
            printOutput=True
        )
    res_det = sandbox.automation_api.GetReservationDetails(sandbox.id)
    for connection in res_det.ReservationDescription.Connectors:
        try:
            Source_model = sandbox.automation_api.GetResourceDetails(connection.Source).ResourceModelName
        except:
            Source_model = ''
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, Source_model)
        try:
            Target_model = sandbox.automation_api.GetResourceDetails(connection.Target).ResourceModelName
        except:
            Target_model = ''
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, Target_model)
        if Source_model == DHCP_app.LogicalResource.Model or Target_model == DHCP_app.LogicalResource.Model:
            sandbox.automation_api.ConnectRoutesInReservation(
                reservationId=sandbox.id,
                endpoints=[connection.Source, connection.Target],
                mappingType='bi'
            )

def solve_abstract_tgn(sandbox, components):
    res_det = sandbox.automation_api.GetReservationDetails(sandbox.id)
    in_port = [x for x in res_det.ReservationDescription.TopologiesReservedResources if x.Alias == 'Inbound']
    out_port = [x for x in res_det.ReservationDescription.TopologiesReservedResources if x.Alias == 'Outbound']
    sandbox.automation_api.SetAttributeValue(
        resourceFullPath=in_port[0].Name,
        attributeName='CS_TrafficGeneratorPort.Logical Name',
        attributeValue='Port 1'
    )
    sandbox.automation_api.SetAttributeValue(
        resourceFullPath=out_port[0].Name,
        attributeName='CS_TrafficGeneratorPort.Logical Name',
        attributeValue='Port 2'
    )

def solve_abstract_tgn_first_gen(sandbox, components):
    res_det = sandbox.automation_api.GetReservationDetails(sandbox.id)
    in_port = [x for x in res_det.ReservationDescription.TopologiesReservedResources if x.Alias == 'Inbound']
    out_port = [x for x in res_det.ReservationDescription.TopologiesReservedResources if x.Alias == 'Outbound']
    sandbox.automation_api.SetAttributeValue(
        resourceFullPath=in_port[0].Name,
        attributeName='Logical Name',
        attributeValue='Port1'
    )
    sandbox.automation_api.SetAttributeValue(
        resourceFullPath=out_port[0].Name,
        attributeName='Logical Name',
        attributeValue='Port2'
    )

def connectL1Routes(sandbox, components):
    """
    :param Sandbox sandbox:
    :return:
    """
    sandboxL1Routes = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.RequestedRoutesInfo
    for route in sandboxL1Routes:
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                               "connecting source and target: " + route.Source + " " + route.Target)
        sandbox.automation_api.ConnectRoutesInReservation(sandbox.id, [route.Source,route.Target], 'bi')

    pass


def loadNetworkingDevicesConfig(sandbox, components):
    """
    :param Sandbox sandbox:
    :return:
    """

    # config_path = 'c:\\__quali files\\networking configs'
    config_path = 'ftp://admin:admin@172.16.0.196'
    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                           "ftp path is: " + config_path)
    blueprint_name = sandbox.reservationContextDetails.environment_name
    blueprint_suffix = blueprint_name.replace(' ' ,'_')
    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                           "blueprint_suffix: " + blueprint_suffix)


    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, "length of inputs: " + str(len(sandbox.global_inputs)))
    if len(sandbox.global_inputs) > 0:
        user_config_type_input = sandbox.global_inputs['Config Type']
        # if config_type == 'default':
        #     restore_method = 'override'
        # else:
        #     restore_method = 'append'
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                               "config_type input selected: " + user_config_type_input)

        for resource_name, resource in sandbox.components.resources.iteritems():
            # if resource.ResourceFamilyName == "Switch" or resource.ResourceFamilyName == "Router":
            if "Switch" in resource.ResourceModelName or "Router" in resource.ResourceModelName:
                resouce_modelname_suffix = resource.ResourceModelName.replace('Switch','')
                resouce_modelname_suffix = resouce_modelname_suffix.replace('Router','')
                resouce_modelname_suffix = resouce_modelname_suffix.replace(' ','')
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resouce_modelname_suffix: " + resouce_modelname_suffix)
                load_config_inputs = []
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource name: " + resource_name)

                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource family: " + resource.ResourceFamilyName)

                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource model: " + resource.ResourceModelName)

                # load the default config on all devices as override. the file name should be {device model name}_default.txt}


                config_type = 'running'
                restore_method = 'override'
                file_extension =''
                if 'Huawei' in resouce_modelname_suffix:
                    file_extension = '.zip'
                    # config_type = 'StartUp'
                else:
                    file_extension = '.txt'

                # load_config_inputs.append(InputNameValue('path', config_path + "/" + str(resource.ResourceModelName).replace(' ' ,'_') + "_default.txt" ))
                load_config_inputs.append(InputNameValue('path', config_path + "/" + resouce_modelname_suffix + '_' + blueprint_suffix + file_extension ))
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "full config file path: " +config_path + "/" + resouce_modelname_suffix + '_' + blueprint_suffix + file_extension)
                load_config_inputs.append(InputNameValue('configuration_type', config_type))
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "configuration_type: " + config_type)
                load_config_inputs.append(InputNameValue('restore_method', restore_method))
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "restore_method: " + restore_method)
                load_config_inputs.append(InputNameValue('vrf_management_name', ''))


                sandbox.automation_api.ExecuteCommand(reservationId=sandbox.id,
                                                      targetName=resource_name,
                                                      targetType='Resource',
                                                      commandName='restore',
                                                      commandInputs=load_config_inputs,
                                                      printOutput=True)

                # begin loading "append" config files in case the user input is "all" - go to the config files folder and find all files with device name except default

                if user_config_type_input == 'ALL':
                    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                           "user input is ALL, appending all files  ")
                    config_files_folder_path = 'C:\\__QualiFiles\\networking_configs'
                    onlyfiles = [f for f in listdir(config_files_folder_path) if isfile(join(config_files_folder_path, f))]
                    for file in onlyfiles:
                        # if str(file).find(str(resource.ResourceModelName).replace(' ' ,'_'))
                        if str(resource.ResourceModelName).replace(' ' ,'_') in str(file) and 'default' not in str(file):
                            sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                                   "appending file path: " + str(file))
                            #now run the restore command in append mode

                            config_type = 'running'
                            restore_method = 'append'
                            
                            load_config_inputs = []

                            load_config_inputs.append(InputNameValue('path', config_path + "/" + str(file)))
                            sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                                   "full config file path: " + config_path + "/" + str(file))
                            load_config_inputs.append(InputNameValue('configuration_type', config_type))
                            sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                                   "configuration_type: " + config_type)
                            load_config_inputs.append(InputNameValue('restore_method', restore_method))
                            sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                                   "restore_method: " + restore_method)
                            load_config_inputs.append(InputNameValue('vrf_management_name', ''))

                            sandbox.automation_api.ExecuteCommand(reservationId=sandbox.id,
                                                                  targetName=resource_name,
                                                                  targetType='Resource',
                                                                  commandName='restore',
                                                                  commandInputs=load_config_inputs,
                                                                  printOutput=True)


            else:
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource name: " + resource_name)

                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource family: " + resource.ResourceFamilyName)

                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource model: " + resource.ResourceModelName)
                sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id,
                                                                       "resource model is static, skip configuration " + resource.ResourceModelName)

# def restore_base_switch(sandbox, components):
#     return restore_on_switches(sandbox, components, 'NxOSbase')

def restore_test_switch(sandbox, components):
    config_name = sandbox.global_inputs.get('config_to_restore')
    restore_on_switches(sandbox, components, 'NxOSbase')
    return restore_on_switches(sandbox, components, config_name)


def restore_on_switches(sandbox, components, filename):
    """
    :param Sandbox sandbox:
    :return:
    """
    switches = [res for res in sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Resources
                if res.ResourceFamilyName == 'CS_Switch']
    for switch in switches:
        sandbox.automation_api.WriteMessageToReservationOutput(
            reservationId=sandbox.id,
            message='performing restore of {0} to switch {1}'.format(filename, switch.Name)
        )
        oput = sandbox.automation_api.ExecuteCommand(
            reservationId=sandbox.id,
            targetName=switch.Name,
            targetType='Resource',
            commandName='restore_demo',
            commandInputs=[
                InputNameValue('configuration_type', 'Running'),
                InputNameValue('filename', filename)
            ],
            printOutput=True
        ).Output


