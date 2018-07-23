#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate
from cloudshell.networking.cisco.command_templates.add_remove_vlan import ACTION_MAP, ERROR_MAP

NXOS_L2_TUNNEL = CommandTemplate("l2protocol tunnel",
                                 action_map=ACTION_MAP,
                                 error_map=ERROR_MAP)

NXOS_NO_L2_TUNNEL = CommandTemplate("no l2protocol tunnel",
                                    action_map=ACTION_MAP,
                                    error_map=ERROR_MAP)
