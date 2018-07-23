#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor
from cloudshell.networking.cisco.command_actions.iface_actions import IFaceActions
from cloudshell.networking.cisco.nxos.command_templates import nxos_add_remove_vlan as nxos_vlan_cmd_template


class CiscoNXOSIFaceActions(IFaceActions):
    def __init__(self, cli_service, logger):
        """ Add remove vlan

        :param cli_service: config mode cli_service
        :type cli_service: CliService
        :param logger:
        :type logger: Logger
        :return:
        """

        super(CiscoNXOSIFaceActions, self).__init__(cli_service, logger)

    def _get_no_l2_protocol_tunnel_cmd(self, action_map=None, error_map=None):
        return CommandTemplateExecutor(self._cli_service,
                                       nxos_vlan_cmd_template.NXOS_NO_L2_TUNNEL,
                                       action_map=action_map,
                                       error_map=error_map)
