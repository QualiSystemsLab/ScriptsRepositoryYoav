#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import time
from cloudshell.cli.cli_service_impl import CliServiceImpl

from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.session.telnet_session import TelnetSession
from cloudshell.devices.cli_handler_impl import CliHandlerImpl
from cloudshell.networking.cisco.cli.cisco_cli_handler import CiscoCliHandler
from cloudshell.networking.cisco.cli.cisco_command_modes import EnableCommandMode, DefaultCommandMode, ConfigCommandMode
from cloudshell.networking.cisco.sessions.console_ssh_session import ConsoleSSHSession
from cloudshell.networking.cisco.sessions.console_telnet_session import ConsoleTelnetSession


class CiscoNXOSCliHandler(CiscoCliHandler):
    def on_session_start(self, session, logger):
        """Send default commands to configure/clear session outputs
        :return:
        """

        cli_service = CliServiceImpl(session=session, command_mode=self.enable_mode, logger=logger)
        cli_service.send_command("terminal length 0", EnableCommandMode.PROMPT)
        cli_service.send_command("terminal width 300", EnableCommandMode.PROMPT)
        with cli_service.enter_mode(self.config_mode) as config_session:
            config_session.send_command("no logging console", ConfigCommandMode.PROMPT)
