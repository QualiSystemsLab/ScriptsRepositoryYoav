import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

session = script_helpers.get_api_session()
session.WriteMessageToReservationOutput(
    reservationId=script_helpers.get_reservation_context_details().id,
    message='Hello world'
)




