import json
import os
import cloudshell.api.cloudshell_api as api


# Production
reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])


# username = connectivity_details['adminUser']
# password = connectivity_details['adminPass']
# server = connectivity_details['serverAddress']
# domain = reservation_details['domain']
#
# session = api.CloudShellAPISession(server, username, password, domain)
# debug:
# session = api.CloudShellAPISession('10.87.42.117', 'admin', 'admin', 'Global')

attribute_names = [
    'SSH Address',
    'SSH Password',
    'SSH Port',
    'SSH Userame',
    'Telnet Address',
    'Telnet Port',
    'Telnet Username',
    'Telnet Password'
]


def Terminals_wipe():
    session = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
                                       token_id=connectivity_details['adminAuthToken'],
                                       domain=reservation_details['domain'])
    session.WriteMessageToReservationOutput(reservation_details['id'], 'Logged On')
    reservation_details_data = session.GetReservationDetails(reservation_details['id']).ReservationDescription.Resources
    if reservation_details_data.__len__() < 1:
        raise Exception("no resources detected")
    else:
        for resource in reservation_details_data:
            for attr in attribute_names:
                at_n_v = ''
                try:
                    at_n_v = session.GetAttributeValue(
                             resourceFullPath=resource.Name,
                             attributeName=attr
                             )
                    # session.WriteMessageToReservationOutput(reservation_details['id'], at_n_v.Name)
                    # session.WriteMessageToReservationOutput(reservation_details['id'], at_n_v.Value)
                except:
                    pass
                try:
                    session.SetAttributeValue(
                        resourceFullPath=resource.Name,
                        attributeName=at_n_v.Name,
                        attributeValue=''
                    )
                    session.WriteMessageToReservationOutput(reservation_details['id'],
                                                            'attribute {0} on resource {1} has been wiped.\n'.format(
                                                                attr, resource.Name
                                                            ))
                except Exception as e:
                    if e.message == 'Error updating attribute value':
                        try:
                            session.SetAttributeValue(
                                resourceFullPath=resource.Name,
                                attributeName=at_n_v.Name,
                                attributeValue='-1'
                            )
                            session.WriteMessageToReservationOutput(reservation_details['id'],
                                                                    'attribute {0} on resource {1} has been wiped.\n'.format(
                                                                        attr, resource.Name
                                                                    ))
                        except:
                            pass
                    elif e.message == '\'str\' object has no attribute \'Name\'':
                        session.WriteMessageToReservationOutput(reservation_details['id'],
                                                                'There is no attribute {0} on resource {1}.\n'.format(
                                                                    attr, resource.Name
                                                                ))
                    else:
                        session.WriteMessageToReservationOutput(reservation_details['id'],
                                                            'can not change attribute {0} on resource {1}. reason {2}\n'.format(
                                                                attr, resource.Name, e.message
                                                            ))

