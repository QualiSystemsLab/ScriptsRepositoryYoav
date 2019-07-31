import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
import json
import winrm
from cloudshell.core.logger import qs_logger
import qs_cs_sandbox_extractor


resid = '5faff89a-42fb-4f4f-a738-d98e34dcd8eb'

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


session = api.CloudShellAPISession(host=server, username=username, password=password, domain=domain)

count_dict = {}
print 'VM Name                      VM Size'
print '---------------------------------------------------------'
for res in session.GetReservationDetails(resid).ReservationDescription.Resources:

    if res.VmDetails:
        vm_size = [data.Value for data in res.VmDetails.InstanceData if data.Name == 'vm size'][0]
        print '{0: <25}         {1: <12}'.format(res.Name, vm_size)
        if vm_size in count_dict:
            size_count = count_dict[vm_size] + 1
        else:
            size_count = 1
        count_dict.update({vm_size: size_count})
print '\n\n\n' \
      'VM Size                  Count'
print '---------------------------------------------------------'
for k,v in count_dict.iteritems():
    print '{0: <25}      {1: <25}'.format(k,v)


pass