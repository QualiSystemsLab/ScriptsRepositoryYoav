import cloudshell.api.cloudshell_api as api
username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'


session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
all_topologies = session.GetTopologiesByCategory()
for blueprint in all_topologies.Topologies:
    blueprint_name = blueprint
    blueprint_details = None
    try:
        blueprint_details = session.GetTopologyDetails(blueprint_name)
    except:
        print 'Blueprint with name {} was not found '.format(blueprint_name)
    if blueprint_details:
        if blueprint_details.Apps.__len__() == 0 \
                and blueprint_details.Resources.__len__() == 0 \
                and blueprint_details.Services.__len__() == 0 \
                and blueprint_details.AbstractResources.__len__() == 0:
            session.DeleteTopology(blueprint_details.Name)
            print 'Blueprint with name {0} was deleted'.format(blueprint_details.Name)
