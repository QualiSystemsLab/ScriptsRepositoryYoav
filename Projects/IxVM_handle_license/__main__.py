import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers
import license_ssh_handler

# res_dets = session.GetResourceDetails(script_helpers.get_resource_context_details().name)

# import debug
# debug.get_debug_session()

# hostname = '192.168.42.161'
# username = 'admin'
# password = 'admin'
port = 22

session = script_helpers.get_api_session()
reservation_details = session.GetReservationDetails(script_helpers.get_reservation_context_details().id)
lic_handler = license_ssh_handler.configure_license(
    hostname=script_helpers.get_resource_context_details().address,
    user=script_helpers.get_resource_context_details().attributes.get('User'),
    password=session.DecryptPassword(script_helpers.get_resource_context_details().attributes.get('Password')).Value,
    port=port,
    lic_server_address=script_helpers.get_resource_context_details().attributes.get('License Server')
)
lic_handler.config_license()
pass


