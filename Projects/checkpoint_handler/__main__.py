import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import debug
import cloudshell_cli_handler

def decrypt(password):
    decypted = session.DecryptPassword(password).Value
    return decypted


debug.get_debug_session()
res_id = script_helpers.get_reservation_context_details().id
session = script_helpers.get_api_session()
resources = session.GetReservationDetails(res_id).ReservationDescription.Resources

password = script_helpers.get_resource_context_details().attributes.get('{0}.Admin Password'.format(script_helpers.get_resource_context_details().model))

i = 0
while i < 5:
    try:
        password = decrypt(password)
    except:
        i = 1000
    i = i + 1

CS_Cli = cloudshell_cli_handler.CreateSession(
    host=script_helpers.get_resource_context_details().address,
    username=script_helpers.get_resource_context_details().attributes.get('{0}.Admin Username'.format(script_helpers.get_resource_context_details().model)),
    password=password
)
pass

