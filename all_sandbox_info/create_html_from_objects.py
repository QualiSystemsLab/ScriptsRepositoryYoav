
class virtualMachine():
    def __init__(self):
        self.name = ''
        self.username = ''
        self.password = ''
        self.publicIP = ''
        self.nics = []

class virtualNic():
    def __init__(self):
        self.name = ''
        self.privateIP = ''
        self.mac_address = ''
        self.subnet_CIDR = ''

class subnet():
    def __init__(self):
        self.name = ''
        self.attributes = []

def createHTMLtablereport(all_virtual_assets, all_subnets):
    '''
    :param [virtualMachine] all_virtual_assets:
    :param [subnet] all_subnets:
    :return:
    '''

    report = '<p>Sandbox Virtual Machines details:</p>'
    for v_asset in all_virtual_assets:
        header = 'Virtual Machine Name: {0}<br><br> User Name: {1}<br> Password {2}<br> Public IP: {3} <br><br>'.format(
            v_asset.name, v_asset.username, v_asset.password, v_asset.publicIP
        )
        report += '<p>'+header + '</p><table border="1">'
        report += '<tr>'
        report += '<td>Private IP</td>'
        report += '<td>MAC Address</td>'
        # report += '<td>subnet CIDR</td>'
        report += '</tr>'
        for nic in v_asset.nics:
            report += '<tr>'
            if not nic.privateIP:
                report += '<td>' + 'No IP assigned' + '</td>'
            else:
                report += '<td>' + nic.privateIP + '</td>'
            report += '<td>' + nic.mac_address + '</td>'
            # report += '<td>' + nic.subnet_CIDR + '</td>'
            report += '</tr>'
        report += '</table>'
        #subnets
    report += '<h1>' + 'Vlans' + '</h1>'
    for subnet in all_subnets:
        report += '<p>      ' + subnet.name + '</p>'
            # for attr in subnet.attributes:
            #     report += '<p>' + attr.Name + ' : ' + attr.Value + '</p>'

    return report