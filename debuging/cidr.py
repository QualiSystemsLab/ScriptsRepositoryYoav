import cloudshell.api.cloudshell_api as api

def _extract_cidr_from_network_id(network_id):
    """
    :param str network_id:
    :return:
    """
    cidr_id = network_id.split("_")[1]
    ip, submask = cidr_id.split("-")
    octets = ip.split(".")
    last_octet = octets[3]
    incremented_ip = str(int(last_octet) + 1)
    octets[3] = incremented_ip
    new_ip = ".".join(octets)
    cidr = new_ip + "/" + submask
    return cidr


username = 'admin'
password = 'Itbabyl0n'
server = '40.118.18.233'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

res = session.GetResourceDetails('vsrxwithdriver-27e979ab')
network_data = res.VmDetails.NetworkData
for x in network_data:
    my_ip = filter(lambda z:z.Name == 'ip', x.AdditionalData)[0].Value
    pass
# _extract_cidr_from_network_id(network_data[0].NetworkId)