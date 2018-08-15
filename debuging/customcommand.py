import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession(
    host='localhost',
    username='admin',
    password='admin',
    domain='Global'
)

# qq = session.GetResourceCommands(
#     resourceFullPath='IOS Israel Demo'
# )
#
# session.ExecuteCommand(
#     reservationId='7888b3c9-85ff-4aac-8e00-5b4059dc5516',
#     targetName='IOS Israel Demo',
#     targetType='Resource',
#     commandName='run_custom_config_command',
#     commandInputs=[
#         api.InputNameValue(Name='custom_command',
#                            Value='interface fastethernet 0/2 description 3333'
#                            )
#     ]
# )
def create_port_for_ap(session, name, parent):
    '''
    :param api.CloudShellAPISession session:
    :param str name:
    :return:
    '''
    session.CreateResource(
        resourceFamily='Port',
        resourceModel='Port Model',
        resourceName=name,
        resourceAddress=name,
        parentResourceFullPath=parent
    )

all_pc = session.FindResources(resourceModel='PC').Resources
try:
    for pc in all_pc:
        create_port_for_ap(session, 'Port', pc.Name)
except:
    pass
all_gal = session.FindResources(resourceModel='Galileo').Resources
try:
    for gal in all_gal:
        for i in range(1,5):
            create_port_for_ap(session, 'Port {}'.format(str(i)), gal.Name)
except:
    pass
all_ap = session.FindResources(resourceModel='AP').Resources
for ap in all_ap:
    try:
        create_port_for_ap(session, 'ap-pc', ap.Name)
        create_port_for_ap(session, 'ap-ap', ap.Name)
        create_port_for_ap(session, 'ap-gallileo', ap.Name)
    except:
        pass
    session.UpdatePhysicalConnection(
        '{0}/{1}'.format(ap.Name, 'ap-pc'),
        '{0}/Port'.format('-'.join([ap.Name.split('-')[1],ap.Name.split('-')[0]])),
        overrideExistingConnections=True
    )
    res_num = int(ap.Name.split('-')[0])
    if res_num > 4:
        session.UpdatePhysicalConnection(
            '{0}/{1}'.format(ap.Name, 'ap-gallileo'),
            'Galileo-atahall-6/Port {}'.format(res_num.__mod__(4) + 1),
            overrideExistingConnections=True
        )
    else:
        session.UpdatePhysicalConnection(
            '{0}/{1}'.format(ap.Name, 'ap-gallileo'),
             'Galileo-atahall-5/Port {}'.format(res_num.__mod__(4) + 1),
            overrideExistingConnections=True
        )

pass