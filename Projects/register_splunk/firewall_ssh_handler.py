import paramiko


class configure_firewall():
    def __init__(self, hostname, user, password, splunk_address, port=22):
        self.hostname = hostname
        self.username = user
        self.password = password
        self.splunk_address = splunk_address
        self.port = port
        self.terminal = paramiko.SSHClient()
        self.terminal.load_system_host_keys()
        self.terminal.set_missing_host_key_policy(paramiko.WarningPolicy())
        self.terminal.connect(hostname=self.hostname,
                       port=self.port,
                       username=self.username,
                       password=self.password)
        self.channel = self.terminal.invoke_shell()

    def __del__(self):
        print ('tidying up the place')
        self.terminal.close()

    def send_command(self, command):
        stdin, stdout, stderr = self.terminal.exec_command('{} \n'.format(command))
        return stdout.read()

    def config_license(self):
        outp = []
        outp.append(self.send_command('\r\n'))
        outp.append(self.send_command('config log syslogd setting\r\n'))
        outp.append(self.send_command('set status enable\r\n'))
        outp.append(self.send_command('set server {}\r\n'.format(self.splunk_address)))
        outp.append(self.send_command('end\r\n'))
        return outp
