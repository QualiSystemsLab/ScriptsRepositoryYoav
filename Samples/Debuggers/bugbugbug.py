from xml.etree.ElementTree import ElementTree as ET


class attackedMachinesData:
    def __init__(self):
        self.machines = []
        self.vlan = ''
        self.router_ip = ''
        self.gateway = ''
        self.NName = ''

class attackedMachineData:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

class NN_Manipulator():
    def __init__(self):
        pass

    def manipulate_xml(self, tree, machines):
        IP_List = tree.findall('network/domain')
        element_finder = tree.findall('network/networkModel/element')
        tree.find('network/label/string').text = machines.NName
        tree.find('testmodel').attrib['network'] = machines.NName
        tree.find('network').attrib['name'] = machines.NName
        for item in IP_List:
            name = item.attrib['name']
            new_ip = [b.ip for b in machines.machines if b.name == name]
            if new_ip:
                item.find('.//range').attrib['max'] = new_ip[0]
                item.find('.//range').attrib['min'] = new_ip[0]
            else:
                item.find('subnet').attrib['router_ip'] = machines.router_ip
                item.find('subnet').attrib['gateway'] = machines.gateway
                item.find('subnet').attrib['innervlan'] = machines.vlan
        for element in element_finder:
            type = element.attrib['type']
            if type == 'vlan':
                vlan_ids = element.findall('int')
                for vlan_id in vlan_ids:
                    if vlan_id.attrib['id'] == 'inner_vlan':
                        vlan_id.text = machines.vlan
            if type == 'ip_external_hosts':
                id = element.find('string').text
                new_ip = [b.ip for b in machines.machines if b.name == id]
                if new_ip:
                    pass
                    element.find('ip_address').text = new_ip[0]
            if type == 'ip_router':
                router_elements = element.findall('ip_address')
                for router_element in router_elements:
                    if router_element.attrib['id'] == 'ip_address':
                        router_element.text = machines.router_ip
                    elif router_element.attrib['id'] == 'gateway_ip_address':
                        router_element.text = machines.gateway
                    else:
                        pass
        return tree


abcd = NN_Manipulator()
ETO = ET()
tree = ETO.parse(r"C:\temp\testfiles\fabe35f7-d857-4836-8b75-125e3e068a6f\yoav_new_test_cs.xml")
machines = attackedMachinesData()
machines.machines.append(attackedMachineData('Linux', 'QAZQAZQAZ'))
machines.machines.append(attackedMachineData('Windows', 'QAZQAZQAZ'))
machines.vlan = 'WWWWWW'
machines.gateway = 'QQQQQQ'
machines.router_ip = 'KKKKKKKK'
machines.NName = 'BBBBBBB'
machines.BPTName = 'HHHHHH'
mytree = abcd.manipulate_xml(tree, machines)
ETO.write(open(r"C:\temp\testfiles\fabe35f7-d857-4836-8b75-125e3e068a6f\test.xml", 'wb'))
ETO.write(open(r"C:\temp\testfiles\fabe35f7-d857-4836-8b75-125e3e068a6f\test.bpt", 'wb'))
pass
