import requests
import json

class switchport():
    def __init__(self):
        self.switch_name = ''
        self.data = ''
        self.Port = ''
        self.remote_device = ''
        self.remote_port = ''
        self.remote_port_id = ''

class my_device():
    def __init__(self):
        self.name = ''
        self.model = ''
        self.ports = list()
        self.excess_data = ''
        self.attributes = dict()
        self.type = ''


d42_url = 'https://devit-rackman.cisco.com/'
getalldevices_url = '/api/1.0/switchports'
get_rack_url = '/api/1.0/racks/3823'
get_device_url = '/api/1.0/devices/id/'
get_pdu_url = '/api/1.0/power_units/'
switchport_id_switch_url = '/api/1.0/switchports/?switch_id='
switchport_id_switch_url_2 = '/api/1.0/switchports/?switch2_id='
switchport_list = []
switch_name = 'SJC-KPB-06'


# r = requests.get(d42_url + getalldevices_url, auth=('yekshtei', 'Trew234%'))
# all_switchports = json.loads(r.content)['switchports']
rack = requests.get(d42_url + get_rack_url, auth=('yekshtei', 'Trew234%'))
rack_info = json.loads(rack.content)
devices = []
for device in rack_info['devices']:
    device_id = device['device']['device_id']
    device_details_raw = requests.get(d42_url + get_device_url + str(device_id), auth=('yekshtei', 'Trew234%'))
    device_details = json.loads(device_details_raw.content)
    new_device = my_device()
    if device_details['hw_model'].__contains__('Nexus'):
        new_device.model = 'Cisco NXOS'
    if device_details['hw_model'].__contains__('Queens'):
        new_device.model = 'SSP-QP'
    if device_details['hw_model'].__contains__('FPR'):
        new_device.model = 'SSP-BS'
    if device_details['hw_model'].__contains__('CISCO2901'):
        new_device.model = 'Terminal Server'
    new_device.name = device_details['name']
    # print ('device {0} from model {1}'.format(device_details['name'], device_details['hw_model']))
    new_device.excess_data = device_details
    new_device.type = device_details['type']
    if new_device.type == 'physical':
        ports_data_raw = requests.get(d42_url + switchport_id_switch_url + str(device_id), auth=('yekshtei', 'Trew234%'))
        ports_data = json.loads(ports_data_raw.content)
    else:
        ports_data_raw = requests.get(d42_url + switchport_id_switch_url_2 + str(device_id), auth=('yekshtei', 'Trew234%'))
        ports_data = json.loads(ports_data_raw.content)
    new_device.ports = ports_data
    if device_details['serial_no']:
        new_device.attributes.update({'Serial_Number': device_details['serial_no']})
    if new_device.model:
        devices.append(new_device)

for pdu_unit in rack_info['pdus']:
    pdu_id = pdu_unit['pdu_id']
    pdu_details_raw = requests.get(d42_url + get_pdu_url + str(pdu_id), auth=('yekshtei', 'Trew234%'))
    pdu_details = json.loads(pdu_details_raw.content)
    new_pdu = my_device()
    if pdu_details['pdu_model']['name'].__contains__('PX2'):
        new_pdu.model = 'Raritan PX2'
    new_pdu.name = pdu_details['name']
    for pdu_port in pdu_details['pdu_ports']:
        new_port = switchport()
        new_port.port = pdu_port['port_name']
        if pdu_port['connected_to']:
            new_port.remote_device = pdu_port['object']
        new_pdu.ports.append(new_port)
    devices.append(new_pdu)
    pass
pass


# for swp in all_switchports:
#     try:
#         aswp = switchport(swp['switch']['name'],
#                           swp['port'],
#                           swp['remote_device'],
#                           swp['remote_port'],
#                           swp['remote_port_id'],
#                           swp
#                           )
#         switchport_list.append(aswp)
#     except:
#         pass
# aaa = []
# rack_switches = []
# for arack in rack_info['devices']:
#     rack_switches.append(arack['device'])
# for t in rack_switches:
#     for q in switchport_list:
#         if q.switch_name == t['name']:
#             aaa.append(q)
# pass


# def find_sp_by_id(switchports, id):
#     for ssp in switchports:
#         try:
#             if ssp['switchport_id'] == id:
#                 sp = ssp
#                 continue
#         except:
#             pass
#     return sp

