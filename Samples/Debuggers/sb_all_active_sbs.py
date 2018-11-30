import cloudshell.api.cloudshell_api as api
import json
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help
from cloudshell.workflow.orchestration.sandbox import Sandbox

resid = 'dd6d6491-fa99-44f0-9f52-0576434ff3e0'

username = 'admin'
password = 'Itbabyl0n'
server = '40.118.18.233'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

qq = session.GetCurrentReservations()
for q in qq.Reservations:
    print q.Id
pass