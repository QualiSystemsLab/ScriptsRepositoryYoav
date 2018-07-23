__author__ = 'yoav.e'

import requests
import atexit
import OpenSSL
import ssl
import sys
import os
import json
import cloudshell.api.cloudshell_api as api

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

# debug


# production
reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
resource_context = json.loads(os.environ['RESOURCECONTEXT'])
connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])

def get_vm(content, name):
    try:
        name = unicode(name, 'utf-8')
    except TypeError:
        pass

    vm = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True)

    for c in container.view:
        if c.name == name:
            vm = c
            break
    return vm

def activate_console():
    """
    Simple command-line program to generate a URL
    to open HTML5 Console in Web browser
    """

    port = '443'
    cssession = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
                                       token_id=connectivity_details['adminAuthToken'],
                                       domain=reservation_details['domain'])
    vm_with_details = cssession.GetResourceDetails(resource_context['name'])
    cloud_provider = cssession.GetResourceDetails(vm_with_details.VmDetails.CloudProviderFullName)
    user = [attr.Value for attr in cloud_provider.ResourceAttributes if attr.Name == 'User'][0]
    password = cssession.DecryptPassword([attr.Value for attr in cloud_provider.ResourceAttributes if attr.Name == 'Password'][0]).Value
    vm_name = resource_context['name']
    host = cloud_provider.Address

    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    requests.packages.urllib3.disable_warnings()
    try:
        si = SmartConnect(host=host,
                          user=user,
                          pwd=password,
                          port=int(port),
                          sslContext=context)
    except Exception as e:
        print 'Could not connect to vCenter host'
        print repr(e)
        sys.exit(1)

    atexit.register(Disconnect, si)

    content = si.RetrieveContent()

    vm = get_vm(content, vm_name)
    vm_moid = vm._moId

    vcenter_data = content.setting
    vcenter_settings = vcenter_data.setting
    console_port = '7331'

    for item in vcenter_settings:
        key = getattr(item, 'key')
        if key == 'VirtualCenter.FQDN':
            vcenter_fqdn = getattr(item, 'value')

    session_manager = content.sessionManager
    session = session_manager.AcquireCloneTicket()
    vc_cert = ssl.get_server_certificate((host, int(port)))
    vc_pem = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, vc_cert)
    vc_fingerprint = vc_pem.digest('sha1')

    outstring = "http://" + host + ":" + console_port + "/console/?vmId=" \
                + str(vm_moid) + "&vmName=" + vm_name + "&host=" + vcenter_fqdn \
                + "&sessionTicket=" + session + "&thumbprint=" + vc_fingerprint
    outHTML = 'Vmware console is now activated. \nuse the following link to access console:  <a href=' + outstring + '>console link</a> \nor use the drop-down menu option'
    cssession.WriteMessageToReservationOutput(reservation_details['id'], outHTML)
