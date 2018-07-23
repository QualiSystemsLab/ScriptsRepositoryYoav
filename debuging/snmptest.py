from cloudshell.snmp.quali_snmp import QualiSnmp as SNMP
from cloudshell.core.logger.qs_logger import get_qs_logger
import pysnmp


PDU_PX1_logger = get_qs_logger('123', 'PDU_PX1_logger', '66678')
SNMP_session = SNMP('u32pdu-j09-02.cisco.com', PDU_PX1_logger, snmp_community='public')
pass
