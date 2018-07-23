import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sc_help

resid = 'b2997114-dc5e-4767-9d93-834246a44559'
dev_help.attach_to_cloudshell_as(
 user='dom_admin',
 password='da',
 reservation_id=resid,
 domain='Global'
)
session = sc_help.get_api_session()
res_det = session.GetReservationDetails(resid)
pass