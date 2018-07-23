from calculate import time_calculator
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as helpers
qq = time_calculator()
html_table = qq.calculate()
session = helpers.get_api_session()
resid = helpers.get_reservation_context_details().id
session.WriteMessageToReservationOutput(resid, html_table)