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

class L1_Port():
    def __init__(self, name, free):
        self.name = name
        self.free = free

def inventory2ndGen(session, Family, Model, Name):
    '''
    :param api.CloudShellAPISession session:
    :return:
    '''
    l1 = 'L1_Mock'
    session.CreateResource(
        resourceFamily=Family,
        resourceModel=Model,
        resourceName=Name,
        resourceAddress='111',
    )
    session.UpdateResourceDriver(
        resourceFullPath=Name,
        driverName=Model
    )
    session.AutoLoad(Name)
    subs = get_all_subs(resource_details=session.GetResourceDetails(Name))
    for sub in subs:
        connect_to_l1(session, l1, sub)

def connect_to_l1(session, l1, resource):
    '''
    :param api.CloudShellAPISession session:
    :return:
    '''
    free_port = get_all_free_l1_ports(session, l1)[0]
    session.UpdatePhysicalConnection(
        resource.name,
        free_port.name
    )


def get_all_free_l1_ports(session, l1):
    '''
    :param api.CloudShellAPISession session:
    :return:
    '''
    PORT_MODEL = 'L1Mock Port'
    all_ports = []
    all_free_ports = []
    l1_details = session.GetResourceDetails(l1)
    all_ports = get_all_subs(all_ports, l1_details)
    all_free_ports = [port for port in all_ports if port.free == True]
    return all_free_ports


def get_all_subs(my_list=[], resource_details=None):
    '''
    :param my_list:
    :param resource_details:
    :return:
    '''
    if resource_details.ChildResources.__len__() == 0:
        my_list.append(L1_Port(resource_details.Name, True if resource_details.Connections.__len__() == 0 else False))
    else:
        for x in resource_details.ChildResources:
            get_all_subs(my_list, x)
    return my_list

# actual script

for i in range(1,6):
    inventory2ndGen(session=session,
                    Family='CS_ComputeServer',
                    Model='Coupler',
                    Name='Coupler_{}'.format(str(i)))
    inventory2ndGen(session=session,
                    Family='CS_ComputeServer',
                    Model='CapturePc',
                    Name='CapturePc_{}'.format(str(i)))
for x in range(1,11):
    inventory2ndGen(session=session,
                    Family='CS_ComputeServer',
                    Model='Dut',
                    Name='Dut{}'.format(str(x)))
pass