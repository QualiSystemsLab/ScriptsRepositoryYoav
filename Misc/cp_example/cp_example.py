import cloudshell_cli_handler



cs_cli = cloudshell_cli_handler.CreateSession(
    username='admin',
    password='P@ssw0rd1234',
    host='13.69.60.5'
)
outp = cs_cli.send_clish_terminal_command('show version')
pass