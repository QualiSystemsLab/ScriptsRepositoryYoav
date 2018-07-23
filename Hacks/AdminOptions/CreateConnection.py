import get_cs_session
import os

def Create_Connection_request():
    session, helpers = get_cs_session.create_cs_session('no')
    resid = helpers.get_reservation_context_details().id
    first_port = os.environ["First_Port_Name"]
    second_port = os.environ["Second_Port_Name"]
    over_connections = os.environ["override"]
    # first_port = 'Yoav Test Router\Yoav Test Router port'
    # second_port = 'Yoav Test Router\Yoav Test Router port1'
    # over_connections = 'yes'
    possible_true = ['yes', 'Yes', 'True', 'true', 'sure', 'ok']
    if over_connections in possible_true:
        override = 'True'
    else:
        override = 'False'
    try:
        session.UpdatePhysicalConnection(
            resourceAFullPath=first_port,
            resourceBFullPath=second_port,
            overrideExistingConnections=override
        )
        session.WriteMessageToReservationOutput(resid, '\nCreated the connection between {0} and {1}\n '.
                                                format(first_port, second_port))
    except Exception as e:
        session.WriteMessageToReservationOutput(resid,
                                                '\nCould not Create the connection between {0} and {1} \nReason: {2} \n'.
                                                format(first_port, second_port, e.message))