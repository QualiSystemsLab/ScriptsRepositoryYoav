import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers


res_id = script_helpers.get_reservation_context_details().id
session = script_helpers.get_api_session()
reservation_details = session.GetReservationDetails(script_helpers.get_reservation_context_details().id)
session.WriteMessageToReservationOutput(
    reservationId=res_id,
    message='aaaa'
)

session.U