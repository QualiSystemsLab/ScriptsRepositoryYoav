import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

resid = '0acc10c9-3056-4b3b-93e5-328aade2210a'

username = 'admin'
password = 'Itbabyl0n'
server = '40.91.201.107'
domain = 'Global'

dev_help.attach_to_cloudshell_as(
    user=username,
    password=password,
    domain=domain,
    reservation_id=resid,
    server_address=server
)
session = script_help.get_api_session()
reservation_details = session.GetReservationDetails(resid).ReservationDescription
pass