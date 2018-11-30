from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.api.cloudshell_api import InputNameValue, ResourceInfo, ServiceInstance , Connection ,SecurityGroup, SecurityGroupsConfiguration, SecurityGroupRule
DEBUG_MODE = True

res_id = '691f34e5-5cfe-40ac-9e3f-5892a9a78f0d'
attach_to_cloudshell_as(user="yoav.e",
                        password="1",
                        domain="Yoavs Domain",
                        reservation_id=res_id,
                        server_address="192.168.30.50")



sandbox = Sandbox()

res_det = sandbox.automation_api.GetReservationDetails(res_id).ReservationDescription
subnets = res_det.Services

my_subnet = subnets[1]
my_subnet_id = filter(lambda x: x.Name == 'Subnet Id', my_subnet.Attributes)[0].Value
res_id = '691f34e5-5cfe-40ac-9e3f-5892a9a78f0d'
rulez = []
for i in range(30):
    first_rule = SecurityGroupRule(
        FromPort='{}'.format(str(1000+i)),
        ToPort='{}'.format(str(1005+i)),
        Protocol='TCP',
        Source='12.23.45.0/25'
        )
    rulez.append(first_rule)

my_security_configuration = SecurityGroupsConfiguration(
    SubnetId=my_subnet_id,
    Rules=rulez
                                                        )
my_security_group = SecurityGroup(
    Name='Azure_VM',
    SecurityGroupsConfigurations=[my_security_configuration]
)
sandbox.automation_api.SetAppSecurityGroups(
    reservationId=res_id,
    securityGroups=[my_security_group]
)
#
# sandbox.automation_api.ConnectRoutesInReservation(
#     reservationId=res_id,
#     endpoints=[
#         'azurevm-a1e0ffd8',
#         'azure-cs-no-pub-4c037435'
#     ],
#     mappingType='bi'
# )
pass