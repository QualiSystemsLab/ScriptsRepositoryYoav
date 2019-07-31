import json
import time
from multiprocessing import get_logger
from cloudshell.core.logger import qs_logger
from azure.mgmt.network import NetworkManagementClient
from cloudshell.api.cloudshell_api import CloudShellAPISession, InputNameValue
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, CancellationContext
# from data_model import *  # run 'shellfoundry generate' to generate data model classes
from msrestazure.azure_active_directory import ServicePrincipalCredentials
from retrying_qslogger.retrying_qslogger import retry
import create_data_files

import cloudshell_cli_handler

import qs_cs_config_parser as parse_config

COREVSRXFILENAME = 'linux_server'

class SkyboxServerDriver(ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def _get_logger_with_reservation_id(self, context):
        self.logger = qs_logger._create_logger(
            log_group=context.reservation.reservation_id,
            log_category='skybox_server',
            log_file_prefix='skybox_server'
        )

    @retry(stop_max_attempt_number=1)
    def _extract_azure_connectivity(self, sandbox_id, cloud_provider, api):

        client_id = ''
        client_secret = ''
        subscription = ''
        tenant = ''
        managmenet_rg = ''
        for attribute in cloud_provider.ResourceAttributes:
            if attribute.Name == 'Azure Application ID':
                client_id = attribute.Value
            if attribute.Name == 'Azure Application Key':
                client_secret = attribute.Value
            if attribute.Name == 'Azure Subscription ID':
                subscription = attribute.Value
            if attribute.Name == 'Azure Tenant ID':
                tenant = attribute.Value
            if attribute.Name == 'Management Group Name':
                managmenet_rg = attribute.Value

        self.logger.info('Decryping cp ' + client_secret)

        client_secret = api.DecryptPassword(client_secret).Value

        return client_id, client_secret, tenant, subscription, managmenet_rg

    @retry(stop_max_attempt_number=1)
    def _get_network_client(self, client_id, client_secret, tenant, subscription):
        credentials = ServicePrincipalCredentials(client_id=client_id,
                                                  secret=client_secret,
                                                  tenant=tenant)
        return NetworkManagementClient(credentials, subscription)

    @retry(stop_max_attempt_number=1)
    def _get_vsrx_connection_params(self, context, session):
        user = ''
        password = ''
        public_ip = ''
        for attribute in context.resource.attributes:
            self.logger.info(attribute + context.resource.attributes[attribute])

            if attribute == 'User':
                user = context.resource.attributes[attribute]
            if attribute == 'Password':
                password = context.resource.attributes[attribute]
            if attribute == 'Public IP':
                public_ip = context.resource.attributes[attribute]

        self.logger.info( 'Decryping vsrx ' + password)
        password = session.DecryptPassword(password).Value
        self.logger.info( 'Decryped vsrx ' + password)

        return password, public_ip, user, context.resource.address

    def send_command(self, context, command):
        self._get_logger_with_reservation_id(context)
        outp = self._send_command(context, command)
        return outp

    @retry(stop_max_attempt_number=1)
    def _send_command(self, context, command):
        """
        :param ResourceCommandContext context:
        :return:
        """
        session = CloudShellAPISession(host=context.connectivity.server_address,
                                       token_id=context.connectivity.admin_auth_token,
                                       domain=context.reservation.domain)
        username = context.resource.attributes.get('User'.format(Model=context.resource.model))
        password_enc = context.resource.attributes.get('Password'.format(Model=context.resource.model))
        password = session.DecryptPassword(password_enc).Value
        my_session = cloudshell_cli_handler.CreateSession(
            host=context.resource.address,
            username=username,
            password=password,
            logger=self.logger
        )
        if not isinstance(command, list):
            commands = [command]
        else:
            commands = command
        outp = my_session.send_terminal_command(commands, password=password)
        self.logger.info(outp)
        return outp

    # @retry(stop_max_attempt_number=20, wait_fixed=20000)
    # def _poll_iteration(self, context):
    #     command = 'show system'
    #     outp = self.send_config_command(
    #         context,
    #         command
    #     )
    #     if isinstance(outp, list):
    #         outp = '\n'.join(outp)
    #
    #     if outp.__contains__('syslog'):
    #         self.logger.info('VSRX has responded and is now considered up')
    #     else:
    #         self.logger.error('VSRX is not responding to SSH as of yet')
    #         raise Exception('VSRX is not up yet')
    #     return outp
    #
    #
    # def poll(self, context):
    #     '''
    #     :param Sandbox sandbox:
    #     :param vsrx_res:
    #     :return:
    #     '''
    #     self._get_logger_with_reservation_id(context)
    #     self._poll_iteration(context)

    def create_info_files(self, context):
        self._get_logger_with_reservation_id(context)
        data_file_generator = create_data_files.data_files_generator(context)
        all_subnets_string = data_file_generator.all_subnets()
        command = 'echo "{}" | tee /tmp/all_subnets.txt'.format(all_subnets_string)
        self.send_command(context, command)

    def run_parsed_config(self, context):
        self._get_logger_with_reservation_id(context)
        session = CloudShellAPISession(host=context.connectivity.server_address,
                                       token_id=context.connectivity.admin_auth_token,
                                       domain=context.reservation.domain)
        Reservation_Description = session.GetReservationDetails(context.reservation.reservation_id).ReservationDescription
        parser = parse_config.parse_commands(session, res_id=context.reservation.reservation_id, logger=self.logger)
        parsed_commands = parser.replace_placeholders(file_name=COREVSRXFILENAME,
                                                      file_type='txt',
                                                      reservation_description=Reservation_Description)
        # for command in parsed_commands:
        #     self._send_command(context, command=command)
        result = []
        try:
            temp_result = self._send_command(context=context, command=parsed_commands)
        except Exception as e:
            self.logger.error(e)
            temp_result = e
        result.append(temp_result)

        return result
        #
        # self._send_command(context, parsed_commands)

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass