from cloudshell.cli.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.command_mode import CommandMode

class CreateSession():

    def __init__(self, host, username, password):
        self.cli = CLI()
        self.mode = CommandMode(r'#')# for example r'%\s*$'
        self.clish_mode = CommandMode(r'>', enter_command='clish', exit_command='exit')# for example r'%\s*$'
        self.mode.add_child_node(self.clish_mode)

        self.session_types = [SSHSession(host=host,
                                         username=username,
                                         password=password)]

        self.session = self.cli.get_session(command_mode=self.mode,
                                            new_sessions=self.session_types)

    def send_terminal_command(self, command):
        with self.session as my_session:
            out = my_session.send_command(command)
            return out

    def send_clish_terminal_command(self, commands):
        outp = []
        with self.cli.get_session(command_mode=self.mode, new_sessions=self.session_types) as session:
            with session.enter_mode(self.clish_mode) as clish_session:
                for command in commands:
                    outp.append(clish_session.send_command(command))
        return '\n'.join(outp)


    def config_license(self):
        outp = []
        outp.append(self.send_terminal_command('\r\n'))
        outp.append(self.send_terminal_command('config log syslogd setting\r\n'))
        outp.append(self.send_terminal_command('set status enable\r\n'))
        outp.append(self.send_terminal_command('set server {}\r\n'.format(self.splunk_address)))
        outp.append(self.send_terminal_command('end\r\n'))
        return outp
