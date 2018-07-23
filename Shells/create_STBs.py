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
def create_stb(name, vendor, model):
    session.CreateResource(
        resourceFamily='CS_GenericResource',
        resourceAddress='NA',
        resourceModel='SetTopBox{}'.format(vendor),
        resourceName=name,
        folderFullPath='STB',
    )
    session.UpdateResourceDriver(
        resourceFullPath=name,
        driverName='SetTopBox{}'.format(vendor)
    )
    session.SetAttributeValue(
        resourceFullPath=name,
        attributeName='SetTopBox{}.DtvStbModel'.format(vendor),
        attributeValue='{0}-{1}'.format(vendor, model)
    )
    session.AutoLoad(name)

def create_obelix(name):
    session.CreateResource(
        resourceFamily='CS_GenericResource',
        resourceAddress='NA',
        resourceModel='Obelix',
        resourceName=name,
        folderFullPath='Obelix Servers',
    )
    session.UpdateResourceDriver(
        resourceFullPath=name,
        driverName='Obelix'
    )
    session.SetAttributeValue(
        resourceFullPath=name,
        attributeName='Obelix.DtvSlotCount',
        attributeValue='16'
    )
    session.AutoLoad(name)

def create_connections():
    all_servers = session.FindResources(resourceModel='obelix').Resources
    all_obelix_ports = []
    for server in all_servers:
        for child in session.GetResourceDetails(server.Name).ChildResources:
            all_obelix_ports.append(child)
    for i, ob_port in enumerate(all_obelix_ports):
        session.UpdatePhysicalConnection(
            resourceAFullPath=ob_port.Name,
            resourceBFullPath='stb{}/Port 1'.format(i)
        )


vendors = ['Samsung',
           'Toshiba',
           'Philips',
           'Siemens',
           'Hauwei']

# for j, vend in enumerate(vendors):
#     for i in range(10):
#         create_stb('stb{0}'.format(str(10*j + i + 51)), vend, str(1 + (i % 3)))
# for k in range(5):
#     create_obelix('Obelix_Server_{}'.format(str(k+1)))
create_connections()
pass