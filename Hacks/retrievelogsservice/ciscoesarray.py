class execution_server():
    def __init__(self, domain='', ess='', address=''):
        self.domain = domain
        self.ess = ess
        self.address = address

# declare all known es servers:
es_servers = []
es_servers.append(execution_server('SSP SJC', 'SSP-SJC7', 'qexec7-ssp-sjc.cisco.com'))
es_servers.append(execution_server('SSP RTP', 'SSP-RTP7', 'qexec7-ssp-rtp.cisco.com'))
es_servers.append(execution_server('SSP BGL', 'SSP-BGL7', 'qexec7-ssp-bgl.cisco.com'))
es_servers.append(execution_server('SSP Regression', 'f17', 'qexec7-f1.cisco.com'))
es_servers.append(execution_server('BGL02', 'BGL02', 'qexec-bgl02.cisco.com'))
es_servers.append(execution_server('Global', 'Local', 'qs.cisco.com'))


