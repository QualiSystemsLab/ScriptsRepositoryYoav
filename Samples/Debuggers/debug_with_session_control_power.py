import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sch

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'
new_server = 'localhost'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
resid = 'bddaf695-19f2-4a89-9e0a-46edb147e2b9'
# rd1 = session.GetResourceMappings([r.Name for r in rd.ChildResources[0].ChildResources])
qq = session.GetReservationDetails(resid).ReservationDescription.Resources
for q in qq:
    res_det = session.GetResourceDetails(q.Name)
    attr_value = [
        attr.Value for attr in res_det.ResourceAttributes if attr.Name == 'DHCP'
    ]
    if attr_value.__len__() > 0:
        if attr_value[0] == 'Yes':
            print "Do Power OFF"
        else:
            print "did not power off"
pass
