import get_cs_session
import os

def Create_resource_request():
    Family = os.environ["Resource_Family"]
    Model = os.environ["Resource_Model"]
    Name = os.environ["Resource_Name"]
    Address = os.environ["Resource_Address"]
    Folder = os.environ["Folder"]
    Parent = os.environ["Parent_Resource"]
    Description = os.environ["Resource_Description"]
    session, helpers = get_cs_session.create_cs_session('no')
    resid = helpers.get_reservation_context_details().id
    res = ''
    try:
        res = session.CreateResource(
        resourceFamily=Family,
        resourceModel=Model,
        resourceName=Name,
        resourceAddress=Address,
        folderFullPath=Folder,
        parentResourceFullPath=Parent,
        resourceDescription=Description
        )
        session.WriteMessageToReservationOutput(resid, '\nCreated the resource {0} \n '.format(Name))
    except Exception as e:
        session.WriteMessageToReservationOutput(resid, '\nCan not create resource {0} \nReason: {1} \n'.format(Name, e.message))
    return res


# res = Create_resource_request(
#     'Router',
#     'Cisco 2811',
#     'Yoav Test Router',
#     '111.222.333.444',
#     'Test  autoload',
#     '',
#     'some desc'
# )
# rex = Create_resource_request(
#     'Generic Port',
#     'Generic Ethernet Port',
#     'Yoav Test Router port',
#     '111.222.333.444',
#     'Test  autoload',
#     'Yoav Test Router',
#     'some desc'
# )