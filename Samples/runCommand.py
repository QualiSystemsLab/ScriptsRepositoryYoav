import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sc_help
import cloudshell.api.cloudshell_api as api

resid = '9abac2bb-32cc-404f-8f1f-7c6d411683c2'
dev_help.attach_to_cloudshell_as(
 user='admin',
 password='admin',
 reservation_id=resid,
 domain='Global'
)
session = sc_help.get_api_session()
res_det = session.GetResourceCommands('NxOS Simulator')
session.ExecuteCommand(
    reservationId=resid,
    targetType='Resource',
    targetName='IOS emulator',
    commandName='run_custom_config_command',
    commandInputs=[api.InputNameValue('custom_command', '')]
)
session.SetResourceLiveStatus(

)


pass