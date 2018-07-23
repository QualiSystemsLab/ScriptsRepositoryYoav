from cloudshell.networking.cisco.nxos.flows.cisco_nxos_restore_flow import CiscoNXOSRestoreFlow
from cloudshell.networking.cisco.runners.cisco_configuration_runner import CiscoConfigurationRunner


class CiscoNXOSConfigurationRunner(CiscoConfigurationRunner):
    @property
    def restore_flow(self):
        return CiscoNXOSRestoreFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def file_system(self):
        return "bootflash:"
