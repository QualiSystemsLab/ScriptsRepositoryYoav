import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

# username = 'admin'
# password = 'admin'
# server = '192.168.0.11'
# domain = 'Global'

# session = api.CloudShellAPISession(
#     username=username,
#     password=password,
#     domain=domain,
#     host=server
# )


# res_dets = session.GetResourceDetails(script_helpers.get_resource_context_details().name)
# dev_helpers.attach_to_cloudshell_as(
#     user=username,
#     password=password,
#     domain=domain,
#     server_address=server,
#     reservation_id='c924fc0d-9a7b-4c83-baab-2f718b5f8667'
# )
session = script_helpers.get_api_session()
reservation_details = session.GetReservationDetails(script_helpers.get_reservation_context_details().id)
ixnet_service_name = reservation_details.ReservationDescription.Services[0].Alias
qqq = session.GetServiceCommands(ixnet_service_name)

json_output = session.ExecuteCommand(
    reservationId=script_helpers.get_reservation_context_details().id,
    targetName=ixnet_service_name,
    targetType='Service',
    commandName='get_statistics',
    commandInputs=[api.InputNameValue(
        Name='view_name',
        Value='Port Statistics'
        ),
        api.InputNameValue(
            Name='output_type',
            Value='JSON'
        )],
    printOutput=True
).Output
session.WriteMessageToReservationOutput(
    reservationId=script_helpers.get_reservation_context_details().id,
    message='this has run successfully using the service {0}'.format(ixnet_service_name)
)

pass


