import paramiko

class configure_license():
    def __init__(self, hostname, user, password, lic_server_address, port):
        self.hostname = hostname
        self.username = user
        self.password = password
        self.lic_server_address = lic_server_address
        self.port = port

    def send_command(self, command):
        stdin, stdout, stderr = self.t.exec_command('{} \n'.format(command))
        return stdout.read()

    def config_license(self):
        self.t = paramiko.SSHClient()
        self.t.load_system_host_keys()
        self.t.set_missing_host_key_policy(paramiko.WarningPolicy())
        self.t.connect(hostname=self.hostname,
                       port=self.port,
                       username=self.username,
                       password=self.password)
        outp = []
        outp.append(self.send_command('set license-server {}'.format(self.lic_server_address)))
        outp.append(self.send_command('set license-check enable'))
        outp.append(self.send_command('restart-service ixServer'))
