import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import attach_to_reservation
from create_html_from_objects import virtualMachine, virtualNic, createHTMLtablereport, subnet

# DEBUG : remove before running live
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dh
dh.attach_to_cloudshell_as(
    user = 'admin',
    password = 'admin',
    domain = 'Global',
    reservation_id='cbad7deb-cc77-474f-9d72-24575ec385c8',
    server_address='localhost'
)

def _decrypt(session, password):
    decypted = session.DecryptPassword(password).Value
    return decypted



session = script_help.get_api_session()
resid = script_help.get_reservation_context_details().id
report = ''

reservation_details = session.GetReservationDetails(resid).ReservationDescription
services = reservation_details.Services
resources = reservation_details.Resources

all_virtual_assets = []

for resource in resources:

    if resource.VmDetails:
        current_virtual_asset = virtualMachine()
        current_virtual_asset.name = resource.Name
        report += '{}:\n'.format(resource.Name)
        res_details = session.GetResourceDetails(resource.Name)
        username = filter(lambda x: x.Name == 'User' or x.Name == '{}.User'.format(resource.ResourceModelName), res_details.ResourceAttributes)[0].Value
        current_virtual_asset.username = username
        Pass_enc = filter(lambda x: x.Name == 'Password' or x.Name == '{}.Password'.format(resource.ResourceModelName), res_details.ResourceAttributes)[0].Value
        pass_dec = session.DecryptPassword(Pass_enc).Value
        current_virtual_asset.password = pass_dec
        report += '   Username : {}\n'.format(username)
        report += '   Password : {}\n'.format(pass_dec)
        resource_details = session.GetResourceDetails(resource.Name)
        current_virtual_asset.publicIP = [attr.Value for attr in resource_details.ResourceAttributes if attr.Name == 'Public IP' or attr.Name == '{}.Public IP'.format(resource.ResourceModelName)][0]
        for nic in resource.VmDetails.NetworkData:
            current_nic = virtualNic()
            # current_nic.subnet_CIDR = nic.NetworkId.split('_')[1].replace('-', '/')
            for add_data in nic.AdditionalData:
                if add_data.Name == 'ip':
                    current_nic.privateIP = add_data.Value
                if add_data.Name == 'mac address':
                    current_nic.mac_address = add_data.Value
                report += '       {0}: {1}\n'.format(add_data.Name, add_data.Value)
            current_virtual_asset.nics.append(current_nic)
            report += '\n'
        all_virtual_assets.append(current_virtual_asset)

# find subnets
all_subnets = []
for service in services:
    if service.ServiceName == 'VLAN Auto' or service.ServiceName == 'VLAN Manual':
        current_subnet = subnet()
        report += ('        VLAN : {}\n'.format(service.Alias))
        current_subnet.name = service.Alias
        # current_subnet.attributes = service.Attributes
        report += '\n'
        # for attr in service.Attributes:
        #     report += ('        {0} : {1}\n'.format(attr.Name, attr.Value))
        report += '\n'
        all_subnets.append(current_subnet)




    html_text = createHTMLtablereport(all_virtual_assets, all_subnets)
    FILEPATH = r'c:\temp\report.html'
    with open(FILEPATH, 'w') as upload_file:
        upload_file.write(html_text)

attach_to_reservation.attachFile(
    serverMachine=script_help.get_connectivity_context_details().server_address,
    resid=script_help.get_reservation_context_details().id,
    user=script_help.get_connectivity_context_details().admin_user,
    password=script_help.get_connectivity_context_details().admin_pass,
    domain=script_help.get_reservation_context_details().domain,
    file_path=FILEPATH
)

print report
