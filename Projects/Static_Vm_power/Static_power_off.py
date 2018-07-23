import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_helpers
import debug


debug.get_debug_session()
session = script_helpers.get_api_session()
sandbox_id = script_helpers.get_reservation_context_details().id
sandbox_resources = session.GetReservationDetails(sandbox_id).ReservationDescription.Resources
static_vms = [res for res in sandbox_resources if res.ResourceModelName == 'vCenter Static VM']
if static_vms.__len__() > 0:
    for static_vm in static_vms:
        session.ExecuteResourceConnectedCommand(
            reservationId=sandbox_id,
            resourceFullPath=static_vm.Name,
            commandName='PowerOff',
            commandTag='power',
            parameterValues=[],
            printOutput=True
        )
else:
    session.WriteMessageToReservationOutput(
        reservationId=sandbox_id,
        message='No Static VMs to turn off!'
    )
pass