import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import os

res_id = script_helpers.get_reservation_context_details().id
session = script_helpers.get_api_session()
message = os.environ['messagetoprint']
reservation_details = session.GetReservationDetails(script_helpers.get_reservation_context_details().id)
session.WriteMessageToReservationOutput(
    reservationId=res_id,
    message=message
)
