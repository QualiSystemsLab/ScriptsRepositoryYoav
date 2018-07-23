import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

def get_debug_session():
    username = 'admin'
    password = 'admin'
    domain = 'Global'
    server = 'localhost'

    resource_name = 'IxVM 8.40 EA - Ixia Virtual Test Appliance_bd16-a85d'
    resId = 'd2a465f7-a75d-4fdb-8e5c-b97c5031a85d'
    dev_helpers.attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
        resource_name=resource_name
    )