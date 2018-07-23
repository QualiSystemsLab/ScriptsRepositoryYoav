import cloudshell.api.cloudshell_api as api


class phys_conn():
    def __init__(self, source, target):
        self.source = source
        self.target = target


username = 'admin'
password = 'admin'
server = 'qs.cisco.com'
domain = 'Global'
# resource = 'SSP-Topo-Data-Sw'
resource = 'F1-DUT01-SSP3RU'
new_resource = 'AA'
def get_connections(rd, rec_connections):
    if rd.ChildResources:
        for c in rd.ChildResources:
            get_connections(c, rec_connections)
            if c.Connections:
                for cc in c.Connections:
                    new_con = phys_conn(c.Name ,cc.FullPath)
                    rec_connections.append(new_con)
    return rec_connections

session = api.CloudShellAPISession(server, username, password, domain)
rd = session.GetResourceDetails(resource)
rec_connections = []
new_rec_connections = []
get_connections(rd, rec_connections)
reqs = []
for rec in rec_connections:
    print '{0} - {1}'.format(rec.source, rec.target)
    # new_rec_connections.append(phys_conn(new_resource + '/' + rec.source.split('/')[1], rec.target))
# for new_rec in new_rec_connections:
#     reqs.append(api.PhysicalConnectionUpdateRequest(new_rec.source, new_rec.target, '10'))
pass
