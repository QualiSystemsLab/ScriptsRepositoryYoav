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
def create_cpe(name, model):
    session.CreateResource(
        resourceFamily='CPE',
        resourceAddress='NA',
        resourceModel='Generic CPE',
        resourceName=name,
        folderFullPath='CPEs',
    )

    session.SetAttributeValue(
        resourceFullPath=name,
        attributeName='CPE Name',
        attributeValue='{0}'.format(model)
    )
    for f in range(1):
        session.CreateResource(
            resourceFamily='Port',
            resourceAddress='{}'.format(str(f+1)),
            resourceModel='Generic Port',
            resourceName='Port {}'.format(str(f+1)),
            parentResourceFullPath=name
        )

def create_DSLAM(name, model):
    session.CreateResource(
        resourceFamily='DSLAM',
        resourceAddress='NA',
        resourceModel='Ericsson',
        resourceName=name,
        folderFullPath='DSLAMs',
    )

    session.SetAttributeValue(
        resourceFullPath=name,
        attributeName='DSLAM Name',
        attributeValue='{0}'.format(model)
    )
    for f in range(1):
        session.CreateResource(
            resourceFamily='Port',
            resourceAddress='{}'.format(str(f+1)),
            resourceModel='Generic Port',
            resourceName='DSLAM Port',
            parentResourceFullPath=name
        )


def create_connections():
    all_servers = session.FindResources(resourceModel='Generic CPE').Resources
    all_modems = session.FindResources(resourceModel='Ericsson').Resources
    all_obelix_ports = []
    all_modem_ports = []
    for server in all_servers:
        for child in session.GetResourceDetails(server.Name).ChildResources:
            all_obelix_ports.append(child)
    for modem in all_modems:
        for child in session.GetResourceDetails(modem.Name).ChildResources:
            all_modem_ports.append(child)
    device_list = []
    device_list.append(all_obelix_ports)
    device_list.append(all_modem_ports)
    for j in range(2):
        for i, ob_port in enumerate(device_list[j]):
            session.UpdatePhysicalConnection(
                resourceAFullPath=ob_port.Name,
                resourceBFullPath='L1 Mock/Blade {0}/Port {1}'.format(str(j+1), str(i+1).zfill(3))
            )

for i in range(10):
    create_cpe('CPE {}'.format(str(i + 1)), 'CPE {}'.format(str(i + 1)))
    create_DSLAM('DSLAM {}'.format(str(i + 1)), 'DSLAM {}'.format(str(i + 1)))
create_connections()
pass