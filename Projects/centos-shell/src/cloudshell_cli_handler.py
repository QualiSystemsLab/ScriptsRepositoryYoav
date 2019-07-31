from cloudshell.cli.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.command_mode import CommandMode

class CreateSession():

    def __init__(self, host, username, password, logger=None):
        self.cli = CLI()
        self.logger = logger
        # the mode is the termination string - code will expect a"$" sign in this case to mark an end of input.
        self.mode = CommandMode(r'$')
        # enable_action_map = {"[Pp]assword for {}".format(username): lambda session, logger: session.send_line(password, logger)}
        # self.elevated_mode = CommandMode(r'(?:(?!\)).)#\s*$', enter_command='sudo su', exit_command='exit', enter_action_map=enable_action_map)
        # self.mode.add_child_node(self.elevated_mode)
        # self.elevated_mode.add_parent_mode(self.mode)
        self.session_types = [SSHSession(host=host,
                                         username=username,
                                         password=password)]

        # self.session = self.cli.get_session(command_mode=self.elevated_mode, new_sessions=self.session_types)
        self.session = self.cli.get_session(command_mode=self.mode, new_sessions=self.session_types)


    def send_terminal_command(self, command):
        outp = []
        out = None
        with self.session as my_session:
            if isinstance(command, list):
                for single_command in command:
                    single_command = '{command}'.format(command=single_command)
                    # self.logger.info('sending command {}'.format(single_command))
                    current_outp = my_session.send_command(single_command)
                    outp.append(current_outp)
                    # self.logger.info('got output {}'.format(current_outp))
                    out = '\n'.join(outp)
            else:
                command = '{command}'.format(command=command)
                out = my_session.send_command(command)
            return out

    def send_admin_termianl_command(self):
        pass
