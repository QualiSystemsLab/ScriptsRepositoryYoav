from cloudshell.cli.cli import CLI
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.command_mode import CommandMode

class CreateSessionSimpleCase():

    def create_my_session(self):

        cli = CLI()
        mode = CommandMode(r'%\s*$#') # for example r'%\s*$'
        ip_address = '192.16.42.235'
        user_name = 'root'
        password = 'Password1'

        session_types = [SSHSession(host=ip_address,
                                    username=user_name,
                                    password=password)]

        with cli.get_session(session_types, mode) as default_session:
            out = default_session.send_command('my command')
            print(out)


a = CreateSessionSimpleCase()
a.create_my_session()
pass