import qualipy.scripts.cloudshell_dev_helpers as dhelpers
import qualipy.scripts.cloudshell_scripts_helpers as helpers


reservationId = 'b0ce36a1-48be-4ff7-9d9b-80bdc430ab68'
dhelpers.attach_to_cloudshell_as('admin', 'admin', 'Global', reservationId, server_address='q1.cisco.com')
api_session = helpers.get_api_session()

playable_Switches = []
switches = api_session.GetReservationDetails(reservationId)
for switch in switches.ReservationDescription.Resources:
    if switch.ResourceFamilyName == 'Power Port':
        playable_Switches.append(switch.Name.split("/")[0])
for aswitch in playable_Switches:
    api_session.ExecuteResourceConnectedCommand(reservationId, aswitch,
                                                'PowerOff', 'power', parameterValues=[],
                                                printOutput=True)
pass