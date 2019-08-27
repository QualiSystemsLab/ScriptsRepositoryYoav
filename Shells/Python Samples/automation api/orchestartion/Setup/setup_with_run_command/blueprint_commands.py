from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.core.logger import qs_logger
import time

class extra_setup_commands():
    def __init__(self, resid):
        self.logger = qs_logger.get_qs_logger(
            log_group=resid,
            log_category='BT_custom_Setup',
            log_file_prefix='BT_Setup'
        )

    def run_command_on_vms(self, sandbox, components):
        """
        :param Sandbox sandbox:
        :return:
        """
        command = sandbox.global_inputs.get('command')
        vms = [res for res in sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Resources
                    if res.ResourceModelName == 'Centos']
        self.logger.info('found {0} vms. running {1} on them'.format(str(vms.__len__()), command))
        time.sleep(20)
        for vm in vms:

            sandbox.automation_api.WriteMessageToReservationOutput(
                reservationId=sandbox.id,
                message='performing {1} on {0} '.format(vm.Name, command)
            )
            self.logger.info('performing {1} on {0} '.format(vm.Name, command))
            out = sandbox.automation_api.ExecuteCommand(
                reservationId=sandbox.id,
                targetName=vm.Name,
                targetType='Resource',
                commandName='send_command',
                commandInputs=[
                    InputNameValue('command', command)
                ],
                printOutput=True
            ).Output
            self.logger.info('command output : {}'.format(out))




