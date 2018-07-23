#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.networking.cisco.flows.cisco_disable_snmp_flow import CiscoDisableSnmpFlow

from cloudshell.networking.cisco.flows.cisco_enable_snmp_flow import CiscoEnableSnmpFlow
from cloudshell.networking.cisco.snmp.cisco_snmp_handler import CiscoSnmpHandler


class CiscoNXOSSnmpHandler(CiscoSnmpHandler):
    def _create_enable_flow(self):
        return CiscoEnableSnmpFlow(self.cli_handler, self._logger, create_group=False)

    def _create_disable_flow(self):
        return CiscoDisableSnmpFlow(self.cli_handler, self._logger, remove_group=False)
