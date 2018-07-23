import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession(
    host='localhost',
    username='admin',
    password='admin',
    domain='Global'
)

# qq = session.GetResourceCommands(
#     resourceFullPath='IOS Israel Demo'
# )
#
# session.ExecuteCommand(
#     reservationId='7888b3c9-85ff-4aac-8e00-5b4059dc5516',
#     targetName='IOS Israel Demo',
#     targetType='Resource',
#     commandName='run_custom_config_command',
#     commandInputs=[
#         api.InputNameValue(Name='custom_command',
#                            Value='interface fastethernet 0/2 description 3333'
#                            )
#     ]
# )
pass