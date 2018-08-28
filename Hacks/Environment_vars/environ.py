import cloudshell.api.cloudshell_api as api
from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
import cloudshell.helpers.scripts.cloudshell_scripts_helpers
username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

import os

def print_all_env_vars():
    environ = os.environ.data
    for k in environ:
        print 'Key: {0} , Value:{1}'.format(k, environ.get(k))


if __name__ == "__main__":
    attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id='4e7c8134-5689-4162-887c-01a3aef86fc8'
    )
    print_all_env_vars()
