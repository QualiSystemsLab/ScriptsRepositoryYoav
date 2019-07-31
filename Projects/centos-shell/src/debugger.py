from cloudshell_cli_handler import CreateSession

instance = CreateSession(
    host='192.168.65.51',
    username='quali',
    password='Password1'
)
instance.send_terminal_command('cd /')
qq = instance.send_terminal_command('ls')
list_of_dirs = qq.split('\n')[0].split('  ')
new_list_of_dirs = []
for d in list_of_dirs:
    new_list_of_dirs.append('ls {}'.format(d))
zz = instance.send_terminal_command(new_list_of_dirs)
print zz
pass
