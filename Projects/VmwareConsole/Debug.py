# debug
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers
import vmwareConsole

resid = 'cd43acfe-15a1-4503-91df-b9416ff43fd6'
Resource_Name = 'ALinkedClone_d196-3fd6'
dev_helpers.attach_to_cloudshell_as(
    user='admin',
    password='admin',
    domain='Global',
    reservation_id=resid,
    server_address='localhost',
    resource_name=Resource_Name,
)
q = vmwareConsole.vmware_console()
q.main()
pass