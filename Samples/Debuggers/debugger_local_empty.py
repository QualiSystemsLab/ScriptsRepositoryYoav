import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

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

