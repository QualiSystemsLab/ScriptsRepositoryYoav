from cloudshell.workflow.orchestration.sandbox import Sandbox

def write_a_message_to_output(sandbox, components):
    '''
    :param Sandbox sandbox:
    :param components:
    :return:
    '''
    pro_stage = sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Status
    sandbox.automation_api.WriteMessageToReservationOutput(
        reservationId=sandbox.id,
        message=pro_stage + 'message logged'
    )
