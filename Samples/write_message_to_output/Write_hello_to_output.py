import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sh


def run():
    session = sh.get_api_session()
    resources = session.GetReservationDetails(sh.get_reservation_context_details().id).ReservationDescription.Resources
    pcs = []
    switch = sh.get_resource_context_details().name
    for res in resources:
        if res.ResourceModelName.__contains__('GenericPortChannel'):
            # pcs.append(res.Name)
            command = 'show interfaces {}'.format(res.Name.split('/')[-1])
            session.ExecuteCommand(
                reservationId=sh.get_reservation_context_details().id,
                targetType='Resource',
                targetName=switch,
                commandName='run_custom_command',
                commandInputs=[api.InputNameValue('custom_command', command)],
                printOutput=True
            )