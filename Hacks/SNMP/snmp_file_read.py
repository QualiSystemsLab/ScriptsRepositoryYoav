from cloudshell.snmp.quali_snmp import ObjectIdentity, ObjectType, QualiSnmp
from cloudshell.core.logger import qs_logger
from cloudshell.snmp.snmp_parameters import SNMPV2ReadParameters


class SNMP_data():
    def __init__(self, oid, type, value):
        self.oid = oid
        self.type = type
        self.value = value

logger = qs_logger.get_qs_logger()
qsnmp_params = SNMPV2ReadParameters(
    ip='192.168.105.4',
    snmp_read_community='publi'
)

filename = r"C:\Users\yoav.e\AppData\Roaming\Quali\Recordings\192.168.105.4\192.168.105.4.snmp"
with open(filename, "r") as f:
    all_lines = f.readlines()
snmp_all_data = []
qsnmp_instance = QualiSnmp(
    snmp_parameters=qsnmp_params,
    logger=logger
)
for line in all_lines:
    split_line = line.split(',')
    snmp_all_data.append(SNMP_data(split_line[0], split_line[1], split_line[2]))
for q in snmp_all_data:
    Otype = ObjectType(ObjectIdentity(q.oid), q.value)
    Otype.resolveWithMib(qsnmp_instance.mib_viewer)
    print Otype
    pass
