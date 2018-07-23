# debug
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as helpers
from calculate import time_calculator

resid = '73a54deb-77fa-4110-b87c-50025e354995'
dev_helpers.attach_to_cloudshell_as(
    user='admin',
    password='admin',
    domain='Global',
    reservation_id=resid,
    server_address='localhost'
)
qq = time_calculator()
html_table = qq.calculate()
session = helpers.get_api_session()
resid = helpers.get_reservation_context_details().id
session.WriteMessageToReservationOutput(resid, html_table)
pass




