from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext
from cloudshell.api.cloudshell_api import CloudShellAPISession


class data_files_generator():
    def __init__(self, context):
        '''
        :param ResourceCommandContext context:
        '''
        self.session = CloudShellAPISession(host=context.connectivity.server_address,
                                       token_id=context.connectivity.admin_auth_token,
                                       domain=context.reservation.domain)

        self.reservation_description = self.session.GetReservationDetails(context.reservation.reservation_id).ReservationDescription
        self.services = self.reservation_description.Services
        self.subnets = [service for service in self.services if service.ServiceName == 'Subnet']
        self.resources = self.reservation_description.Resources

    def all_subnets(self):
        all_subnets = ''
        for subnet in self.subnets:
            name = ''.join(subnet.Alias.split('-')[:-2])
            cidr = [attr for attr in subnet.Attributes if attr.Name == 'Allocated CIDR'][0].Value
            all_subnets += '{1}     {0}\n'.format(name, cidr)
        return all_subnets

