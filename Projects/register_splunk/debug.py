import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

def get_debug_session():
    username = 'admin'
    password = 'admin'
    domain = 'Global'
    server = 'localhost'
    resId = 'a6fd4d88-5882-4049-8402-3514631e1be7'
    dev_helpers.attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
    )