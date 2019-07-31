import json

class route():
    def __init__(self):
        self.destination = ''
        self.cidr = ''

class subnet():
    def __init__(self):
        self.Name = ''
        self.routes = []

all_routes = []

# Subnet number 1 - Internet_Transit
temp_subnet = subnet()
temp_subnet.Name = 'Internet_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = 'Internet'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 2 - DMZ_Server_Farm
temp_subnet = subnet()
temp_subnet.Name = 'DMZ_Server_Farm'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 3 - Clients
temp_subnet = subnet()
temp_subnet.Name = 'Clients'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 4 - SecOps
temp_subnet = subnet()
temp_subnet.Name = 'SecOps'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = 'Internet'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 5 - App_DB_Transit
temp_subnet = subnet()
temp_subnet.Name = 'App_DB_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<App_Developers>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Internal_DB>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 6 - App_Developers
temp_subnet = subnet()
temp_subnet.Name = 'App_Developers'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 7 - Internal_DB
temp_subnet = subnet()
temp_subnet.Name = 'Internal_DB'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 8 - Internal_Servers
temp_subnet = subnet()
temp_subnet.Name = 'Internal_Servers'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 9 - Internal_Transit
temp_subnet = subnet()
temp_subnet.Name = 'Internal_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Internal_Servers>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 10 CP_SRX_Transit
temp_subnet = subnet()
temp_subnet.Name = 'CP_SRX_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Internet_Transit>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<DMZ_Server_Farm>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<DMZ>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 11 - Management_Network
temp_subnet = subnet()
temp_subnet.Name = 'Management_Network'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 12 - CSR_Transit
temp_subnet = subnet()
temp_subnet.Name = 'CSR_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

# temp_route = route()
# temp_route.cidr='<<Web_Dev_Transit>>'
# temp_route.destination = '<<External_Subnet>>'
# temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Web_App>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Dev>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 13 - Web_Dev_Transit
temp_subnet = subnet()
temp_subnet.Name = 'Web_Dev_Transit'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Web_App>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<Dev>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 14 - DMZ
temp_subnet = subnet()
temp_subnet.Name = 'DMZ'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<DMZ_Server_Farm>>'
temp_route.destination = '<<External_Subnet>>'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)


# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 15 - Web_App
temp_subnet = subnet()
temp_subnet.Name = 'Web_App'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# Subnet number 16 - Dev
temp_subnet = subnet()
temp_subnet.Name = 'Dev'

temp_route = route()
temp_route.cidr='0.0.0.0/0'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='10.0.0.0/8'
temp_route.destination = 'None'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<sandbox_wide_subnet>>'
temp_route.destination = '<<Internal_Subnet>>'
temp_subnet.routes.append(temp_route)

temp_route = route()
temp_route.cidr='<<self_CIDR>>'
temp_route.destination = 'VnetLocal'
temp_subnet.routes.append(temp_route)

all_routes.append(temp_subnet)



with open(r'E:\Github\Quali\customers\Skybox-jsons\SkyboxDataFiles\RoutePolicy\all_routing_options.json', 'w') as f:
    f.write(json.dumps(all_routes, default=lambda o: o.__dict__, sort_keys=True, indent=4))
