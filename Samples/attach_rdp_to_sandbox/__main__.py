import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import attach_to_reservation
from rdp_populator import rdp_populator
import sys, string, os

# DEBUG : remove before running live
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dh
dh.attach_to_cloudshell_as(
    user= 'admin',
    password='admin',
    domain='Global',
    reservation_id='e03d8f4b-a233-490f-b3d4-5088b3aaf9be',
    server_address='localhost',
    resource_name='Centos VM_3432-f9be'
)

def _decrypt(session, password):
    decypted = session.DecryptPassword(password).Value
    return decypted

session = script_help.get_api_session()
resid = script_help.get_reservation_context_details().id

# resource_details = session
address = script_help.get_resource_context_details().address
username = script_help.get_resource_context_details().attributes.get('User')
enc_cs_password = script_help.get_resource_context_details().attributes.get('Password')
cleartext_password = session.DecryptPassword(enc_cs_password).Value
pass_enc = os.popen("cryptRDP5.exe {}".format(cleartext_password)).read()

rdp_text = rdp_populator(
    username=username,
    password=pass_enc,
    ip=address
)

FILEPATH = r'c:\temp\{}.rdp'.format(script_help.get_resource_context_details().name)
with open(FILEPATH, 'w') as upload_file:
    upload_file.write(rdp_text)

attach_to_reservation.attachFile(
    serverMachine=script_help.get_connectivity_context_details().server_address,
    resid=script_help.get_reservation_context_details().id,
    user=script_help.get_connectivity_context_details().admin_user,
    password=script_help.get_connectivity_context_details().admin_pass,
    domain=script_help.get_reservation_context_details().domain,
    file_path=FILEPATH,
    filename='machine'
)
