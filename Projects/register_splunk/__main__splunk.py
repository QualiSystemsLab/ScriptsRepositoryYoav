import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import paramiko
import debug
import firewall_ssh_handler
import cloudshell_cli_handler


FIREWALL = 'fortinet'
CLIENT = 'splunk'

debug.get_debug_session()
res_id = script_helpers.get_reservation_context_details().id
session = script_helpers.get_api_session()
resources = session.GetReservationDetails(res_id).ReservationDescription.Resources
splunk_resources = [res for res in resources if res.Name.lower().__contains__(CLIENT)]
fortigate_resources = [res for res in resources if res.Name.lower().__contains__(FIREWALL)]

qqq = cloudshell_cli_handler.CreateSessionSimpleCase()
qqq.create_my_session()


if splunk_resources.__len__() > 0 and fortigate_resources.__len__() > 0:
    splunk_resource = session.GetResourceDetails(splunk_resources[0].Name)
    fortigate_resource = session.GetResourceDetails(fortigate_resources[0].Name)
    f_ssh = cloudshell_cli_handler.CreateSession(
        host=fortigate_resource.Address,
        username=[attr.Value for attr in fortigate_resource.ResourceAttributes if attr.Name == 'User'][0],
        password=session.DecryptPassword(
            [attr.Value for attr in fortigate_resource.ResourceAttributes if attr.Name == 'Password'][0]).Value
        # splunk_address=splunk_resource.Address
    )

    # f_ssh = firewall_ssh_handler.configure_firewall(
    #     hostname=fortigate_resource.Address,
    #     user=[attr.Value for attr in fortigate_resource.ResourceAttributes if attr.Name == 'User'][0],
    #     password=session.DecryptPassword(
    #         [attr.Value for attr in fortigate_resource.ResourceAttributes if attr.Name == 'Password'][0]).Value,
    #     splunk_address=splunk_resource.Address
    # )
    # outp = f_ssh.config_license()

    outp = f_ssh.config_license()
else:
    raise Exception('didn\'t find a {0} or {1}'.format(FIREWALL, CLIENT))
pass


