import atexit
import OpenSSL
import ssl
import sys
import time
import json
import os

from pyVim.connect import Disconnect, SmartConnectNoSSL
from pyVmomi import vim
import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as helpers

# reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
# resource_context = json.loads(os.environ['RESOURCECONTEXT'])
# connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])

class vmware_console():
    def __init__(self):
        pass

    def get_vm(self, content, name):
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

    def main(self):
        self.get_cs_data()
        port = 443

        try:
            si = SmartConnectNoSSL(host=self.host,
                                   user=self.user,
                                   pwd=self.pwd)
        except Exception as e:
            print 'Could not connect to vCenter host'
            print repr(e)
            sys.exit(1)

        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
        vm = self.get_vm(content, self.name)
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

        vc_cert = ssl.get_server_certificate((self.host, port))
        vc_pem = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,
                                                 vc_cert)
        vc_fingerprint = vc_pem.digest('sha1')

        token_address = "http://" + self.host + ":" + console_port + "/console/?vmId=" \
                        + str(vm_moid) + "&vmName=" + self.name + "&host=" + vcenter_fqdn \
                        + "&sessionTicket=" + session + "&thumbprint=" + vc_fingerprint

        print "Open the following URL in your browser to access the " \
              "Remote Console.\n" \
              "You have 60 seconds to open the URL, or the session" \
              "will be terminated.\n"
        print '<a href="{0}">console link</a>'.format(token_address)
        print "Waiting for 60 seconds, then exit"

    def get_cs_data(self):
        self.session = helpers.get_api_session()
        # self.session = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
        #                                    token_id=connectivity_details['adminAuthToken'],
        #                                    domain=reservation_details['domain'])
        resource_context = helpers.get_resource_context_details_dict()
        self.name = resource_context['name']
        res_dets = self.session.GetResourceDetails(resource_context['name'])
        self.host = self.session.GetResourceDetails(res_dets.VmDetails.CloudProviderFullName).RootAddress
        cp_dets = self.session.GetResourceDetails(res_dets.VmDetails.CloudProviderFullName)
        self.user = [attr.Value for attr in cp_dets.ResourceAttributes if attr.Name == 'User'][0]
        self.pwd = self.session.DecryptPassword(
            [attr.Value for attr in cp_dets.ResourceAttributes if attr.Name == 'Password'][0]).Value