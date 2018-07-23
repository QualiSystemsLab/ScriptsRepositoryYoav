#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.devices.runners.firmware_runner import FirmwareRunner

from cloudshell.networking.cisco.flows.cisco_load_firmware_flow import CiscoLoadFirmwareFlow


class CiscoNXOSFirmwareRunner(FirmwareRunner):
    RELOAD_TIMEOUT = 500

    def __init__(self, logger, cli_handler, file_system="bootflash:"):
        """Handle firmware upgrade process

        :param CliHandler cli_handler: Cli object
        :param qs_logger logger: logger
        :param str file_system: file_system
        """

        super(CiscoNXOSFirmwareRunner, self).__init__(logger=logger, cli_handler=cli_handler)
        self._file_system = file_system

    @property
    def load_firmware_flow(self):
        return CiscoLoadFirmwareFlow(self.cli_handler, self._logger, default_file_system=self._file_system)
