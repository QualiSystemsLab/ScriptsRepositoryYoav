from cloudshell.core.logger import qs_logger
from cloudshell.api.cloudshell_api import CloudShellAPISession, InputNameValue
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext
from cloudshell.helpers.scripts.cloudshell_scripts_helpers import ResourceContextDetails, ReservationContextDetails
from cloudshell.cli.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.command_mode import CommandMode

COREVSRXFILENAME = 'linux_server'

class CentosServerDriver():

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

    def _get_logger_with_reservation_id(self, resid):
        self.logger = qs_logger._create_logger(
            log_group=resid,
            log_category='linux_server',
            log_file_prefix='linux_server'
        )

    def send_command(self, session, command, resource, reservation):
        """
        :param CloudShellAPISession session:
        :param ResourceContextDetails resource:
        :param ReservationContextDetails reservation:
        :return:
        """
        self._get_logger_with_reservation_id(reservation.id)
        self.logger.info('started')
        self.logger.info('address: {}'.format(resource.address))

        try:
            username = resource.attributes.get('User')
            self.logger.info('username: {}'.format(username))
            password_enc = resource.attributes.get('Password')
            self.logger.info('password enc: {}'.format(password_enc))
            password = session.DecryptPassword(password_enc).Value
            self.logger.info('password dec: {}'.format(password))
        except:
            self.logger.info('exception ; with model')
            username = resource.attributes.get('{}.User'.format(resource.model))
            self.logger.info('username: {}'.format(username))
            password_enc = resource.attributes.get('{}.Password'.format(resource.model))
            self.logger.info('password enc: {}'.format(password_enc))
            password = session.DecryptPassword(password_enc).Value
            self.logger.info('password dec: {}'.format(password))

        if not isinstance(command, list):
            commands = [command]
        else:
            commands = command
        self.logger.info('command(s)' + ','.join(commands))

        host= resource.address
        self.cli = CLI()
        self.mode = CommandMode(r'\$\s*$')# for example r'%\s*$'
        self.session_types = [SSHSession(host=host,
                                         username=username,
                                         password=password)]
        self.logger.info('host {0} user {1} password {2}'.format(host, username, password))
        self.session_cli = self.cli.get_session(command_mode=self.mode,
                                            new_sessions=self.session_types)
        self.logger.info('created session')
        outp = []
        out = None
        self.logger.info('using session')
        with self.session_cli as my_session:
            self.logger.info('command list before')
            if isinstance(command, list):
                self.logger.info('command list')
                for single_command in command:
                    self.logger.info('sending command {}'.format(single_command))
                    current_outp = my_session.send_command(single_command)
                    outp.append(current_outp)
                    self.logger.info('got output {}'.format(current_outp))
                    out = '\n'.join(outp)
            else:
                self.logger.info('single command')
                self.logger.info('sending command {}'.format(command))
                out = my_session.send_command(command)
                self.logger.info('got output {}'.format(out))

        return out

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass