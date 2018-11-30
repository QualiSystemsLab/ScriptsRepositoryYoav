import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.workflow.orchestration.sandbox import Sandbox

ARMMODELS = ['Checkpoint', 'CheckpointMgmt', 'Fortigate']
NIC_ROLES = ['FortiBranch', 'WANCPFW']

def add_third_nics(self, sandbox, components):
    """
    :param Sandbox sandbox:
    :param components:
    :return:
    """
    third_nic_arms = []
    for ser in sandbox.automation_api.GetReservationDetails(sandbox.id).ReservationDescription.Services:
        if ser.ServiceName in ARMMODELS:
            role = [attr.Value for attr in ser.Attributes if attr.Name == '{}.Role'.format(ser.ServiceName)][0]
            sandbox.automation_api.WriteMessageToReservationOutput(
                reservationId=sandbox.id,
                message="role found: {}".format(role))

            if role in NIC_ROLES:
                third_nic_arms.append(ser)
                sandbox.automation_api.WriteMessageToReservationOutput(
                    reservationId=sandbox.id,
                    message="add 3rd nic to : {}".format(ser.Alias))
    if third_nic_arms.__len__() > 0:
        for finger in third_nic_arms:
            self.logger.info("Deploying {}".format(finger.Alias))
            sandbox.automation_api.WriteMessageToReservationOutput(
                reservationId=sandbox.id,
                message="Deploying {}".format(finger.Alias)
            )
            sandbox.automation_api.EnqueueCommand(
                reservationId=sandbox.id,
                targetName=finger.Alias,
                targetType='Service',
                commandName='add_nic',
                commandInputs=[],
                printOutput=True
            )
            self.logger.info("Deployed {}".format(finger.Alias))
            sandbox.automation_api.WriteMessageToReservationOutput(
                reservationId=sandbox.id,
                message="Deployed {}".format(finger.Alias)
            )
    else:
        self.logger.warn("did not find any ARM services")
        sandbox.automation_api.WriteMessageToReservationOutput(
            reservationId=sandbox.id,
            message="did not find any ARM services"
        )


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
# abcd = session.GetServices('Security', 'CheckpointMgmt')
services_vm_names = []
resid = '1566b46f-71fe-4250-8a73-4675873df5ba'


qq = session.GetReservationDetails(resid).ReservationDescription.Services
for ser in qq:
    if ser.ServiceName in ARMMODELS:
        service_vm_name = [attr.Value for attr in ser.Attributes if attr.Name == '{}.VM Name'.format(ser.ServiceName)][0]
        User = [attr.Value for attr in ser.Attributes if attr.Name == 'User'][
            0]
        pword = [attr.Value for attr in ser.Attributes if attr.Name == 'Password'][
            0]
        print ser.Alias
        print service_vm_name
        print User
        print session.DecryptPassword(session.DecryptPassword(pword).Value).Value
        print '\n\n'
#         services_vm_names.append(service_vm_name)
#         print '\n\n\n\n'

pass
# third_nic_arms = []
# for ser in qq:
#     if ser.ServiceName in ARMMODELS:
#         role = [attr.Value for attr in ser.Attributes if attr.Name == '{}.Role'.format(ser.ServiceName)][0]
#
#         if role in NIC_ROLES:
#             third_nic_arms.append(ser)
#
# ann = session.GetResourceDetails('sb-collector-de546b93').ResourceAttributes
# # my_out = session.ExecuteCommand(
# #             reservationId=resid,
# #             targetName='CheckpointMgmt',
# #             targetType='Service',
# #             commandName='get_nic_information',
# #             commandInputs=[],
# #             printOutput=True
# #             ).Output
# # my_out_json = json.loads(my_out)
# pass
#
# #
# # def _decrypt(session, password):
# #     decypted = session.DecryptPassword(password).Value
# #     return decypted
# # session.SetServiceAttributesValues(
# #     reservationId='3e03394a-015a-483b-b168-d57eee15a425',
# #     serviceAlias='Checkpoint',
# #     attributeRequests=[
# #         api.AttributeNameValue('User', 'admin'),
# #         api.AttributeNameValue('Password', 'P@ssw0rd1234')
# #     ]
# # )
# #
# # password_a = 'qSd/eT6xqAW8/BfrcVJE7P48xz/sXFObYyCuHmO6xFM='
# # i = 0
# # while i < 5:
# #     try:
# #         password_a = _decrypt(session, password_a)
# #     except:
# #         i = 1000
# #     i = i + 1
# # print 'password is : {}'.format(password_a)
# # dec1 = session.DecryptPassword('qSd/eT6xqAW8/BfrcVJE7P48xz/sXFObYyCuHmO6xFM=').Value
# # dec2 = session.DecryptPassword(dec1).Value
# pass
#
# dev_help.attach_to_cloudshell_as(
#     user = 'admin',
#     password = 'Itbabyl0n',
#     server_address = '40.118.18.233',
#     domain='Global',
#     reservation_id='ba2b04e1-738b-4cf2-b795-9092bb466032'
# )
# import os
# # os.environ['RESERVATIONLIFECYCLECONTEXT'] = json.dumps('[{"subnet CIDR": "10.0.5.160/28"}]')
# sandbox = Sandbox()
# pass
