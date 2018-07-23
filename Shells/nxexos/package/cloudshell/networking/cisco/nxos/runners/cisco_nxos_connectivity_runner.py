#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.networking.cisco.nxos.flows.cisco_nxos_add_vlan_flow import CiscoNXOSAddVlanFlow
from cloudshell.networking.cisco.nxos.flows.cisco_nxos_remove_vlan_flow import CiscoNXOSRemoveVlanFlow
from cloudshell.networking.cisco.runners.cisco_connectivity_runner import CiscoConnectivityRunner
from cloudshell.networking.cisco.cli.cisco_cli_handler import CiscoCliHandler



class CiscoNXOSConnectivityRunner(CiscoConnectivityRunner):
    @property
    def add_vlan_flow(self):
        return CiscoNXOSAddVlanFlow(self.cli_handler, self._logger)

    @property
    def remove_vlan_flow(self):
        return CiscoNXOSRemoveVlanFlow(self.cli_handler, self._logger)
