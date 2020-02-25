from cloudshell.cli.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.command_mode import CommandMode

class CreateSession():

    def __init__(self, host, username, password, logger=None, command=None):
        self.cli = CLI()
        self.logger = logger
        self.mode = CommandMode(r'#')# for example r'%\s*$'
        self.session_types = [SSHSession(host=host,
                                         username=username,
                                         password=password)]
        self.logger.info('host {0} user{1} password {2}'.format(host, username, password))
        self.session = self.cli.get_session(command_mode=self.mode,
                                            new_sessions=self.session_types)
        self.logger.info('created session')
        outp = []
        out = None
        self.logger.info('using session')
        with self.session as my_session:
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
        self.out = out




    #
    # def send_terminal_command(self, command, password=None):
    #     outp = []
    #     out = None
    #     self.logger.info('using session')
    #     with self.session as my_session:
    #         if isinstance(command, list):
    #             self.logger.info('command list')
    #             for single_command in command:
    #                 self.logger.info('sending command {}'.format(single_command))
    #                 current_outp = my_session.send_command(single_command)
    #                 outp.append(current_outp)
    #                 self.logger.info('got output {}'.format(current_outp))
    #                 out = '\n'.join(outp)
    #         else:
    #             self.logger.info('single command')
    #             self.logger.info('sending command {}'.format(command))
    #             out = my_session.send_command(command)
    #             self.logger.info('got output {}'.format(out))
    #         return out
