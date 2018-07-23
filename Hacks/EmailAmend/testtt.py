import qualipy.api.cloudshell_api as api_6
import cloudshell.api.cloudshell_api as api_7

class res_type():
    def __init__(self, Family, Model):
        self.Family = Family
        self.Model = Model

username = 'admin'
password = 'admin'
server_6 = 'q1.cisco.com'
server_7 = 'qs.cisco.com'
O_domain = 'SJA'
N_domain = 'SJA'

session_6 = api_6.CloudShellAPISession(server_6, username, password, O_domain)
session_7 = api_7.CloudShellAPISession(server_7, username, password, N_domain)

qq = session_6.GetResourceDetails('SJA-ASA5525-2')
vvv = session_6.GetReservationDetails('d48bc658-01ce-4711-9806-44b6646fcb81')
bb = session_6.RecheckConflicts(['SJA-ASA5525-2'], 'True')
pass