import cloudshell.api.cloudshell_api as api
from cloudshell.api.cloudshell_api import CloudShellAPISession , AttributeNameValue
import time
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.workflow.orchestration.sandbox import Sandbox


ARMMODELS = ['Checkpoint', 'CheckpointMgmt', 'Fortigate']
VSRX_Model = 'VSRx_NS'

def check_ARM_status(session, resid):
    '''
    :param CloudShellAPISession session:
    :return:
    '''
    status = 'running'
    counter = 0
    while status == 'running':
        all_services = session.GetReservationDetails(resid).ReservationDescription.Services
        statii = []
        for ser in all_services:
            if ser.ServiceName in ARMMODELS:
                status = [attr.Value for attr in ser.Attributes if attr.Name == '{}.status'.format(ser.ServiceName)][0]
                statii.append(status)
        status = 'deployed'
        for stat in statii:
            if stat != 'deployed':
                status = 'running'
            elif stat == 'error':
                status = 'error'
        print '{} , {} times'.format(status, str(counter))
        if status == 'running':
            counter = counter + 1
            time.sleep(10)
    return status

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
resid = 'dd6d6491-fa99-44f0-9f52-0576434ff3e0'
# static = check_ARM_status(session, resid)


def _get_connected_vsrx_nic_ip(session, forti_service):
    vsrx = [res for res in session.GetReservationDetails(resid).ReservationDescription.Resources if res.ResourceModelName == VSRX_Model][0]
    vsrx_net_data = vsrx.VmDetails.NetworkData
    vsrx_net_data_dict = {}
    for net in vsrx_net_data:
        temp_ip = [attr.Value for attr in net.AdditionalData if attr.Name == 'ip'][0]
        vsrx_net_data_dict.update({net.NetworkId: temp_ip})
    nics_info = json.loads(session.ExecuteCommand(
        reservationId=resid,
        targetName=forti_service,
        targetType='Service',
        commandName='get_nic_information',
        commandInputs=[],
        printOutput=True
    ).Output)
    my_vsrx_nic_ip = None
    for nic in nics_info:
        if nic.get('Subnet Name') in vsrx_net_data_dict.keys():
            my_vsrx_nic_ip = vsrx_net_data_dict.get(nic.get('Subnet Name'))
    return my_vsrx_nic_ip

def get_user_password(session, resid, service_alias):
    '''
    :param CloudShellAPISession session:
    :param resid:
    :param service_alias:
    :return:
    '''
    my_service = [ser for ser in session.GetReservationDetails(resid).ReservationDescription.Services if ser.Alias == service_alias][0]
    user = [attr.Value for attr in my_service.Attributes if attr.Name == 'User'][0]
    # APP = [attr.Value for attr in my_service.Attributes if attr.Name == '{}.Admin Password Plain'.format(my_service.ServiceName)][0]
    enc_pw = [attr.Value for attr in my_service.Attributes if attr.Name == 'Password'][0]
    dec_pw = session.DecryptPassword(enc_pw).Value
    try:
        sec_dec_pw = session.DecryptPassword(dec_pw).Value
    except:
        sec_dec_pw = ''
    print my_service.Alias
    print 'user : {}'.format(user)
    print 'decrypted once : {}'.format(dec_pw)
    print 'decrypted twice : {}'.format(sec_dec_pw)
    # print 'plain pass attribute : {}'.format(APP)


def get_user_password_resource(session, resource_name):
    '''
    :param CloudShellAPISession session:
    :param resid:
    :param service_alias:
    :return:
    '''
    # my_service = [res for res in session.GetReservationDetails(resid).ReservationDescription.Resource if res.name == resource_name][0]
    my_resource = session.GetResourceDetails(resource_name)

    user = [attr.Value for attr in my_resource.ResourceAttributes if attr.Name == 'User'][0]
    # APP = [attr.Value for attr in my_service.Attributes if attr.Name == '{}.Admin Password Plain'.format(my_service.ServiceName)][0]
    enc_pw = [attr.Value for attr in my_resource.ResourceAttributes if attr.Name == 'Password'][0]
    dec_pw = session.DecryptPassword(enc_pw).Value
    try:
        sec_dec_pw = session.DecryptPassword(dec_pw).Value
    except:
        sec_dec_pw = ''
    print resource_name
    print 'user : {}'.format(user)
    print 'decrypted once : {}'.format(dec_pw)
    print 'decrypted twice : {}'.format(sec_dec_pw)
    # print 'plain pass attribute : {}'.format(APP)


def set_user_password(session, resid, service_alias):
    '''
    :param CloudShellAPISession session:
    :param resid:
    :param service_alias:
    :return:
    '''
    my_service = [ser for ser in session.GetReservationDetails(resid).ReservationDescription.Services if ser.Alias == service_alias][0]
    session.SetServiceAttributesValues(
        reservationId=resid,
        serviceAlias=service_alias,
        attributeRequests=[AttributeNameValue('User', 'admin'),
                           AttributeNameValue('Password', 'P@ssw0rd1234')]
    )



get_user_password_resource(session, 'sb-collector-cde3b5c0')
pass
