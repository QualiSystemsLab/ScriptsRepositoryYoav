import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

def get_debug_session():
    username = 'yoav.e'
    password = '1111'
    domain = 'Global'
    server = '40.113.155.10'
    resId = '5a1a7178-697a-4273-a99e-f85e4a734654'
    dev_helpers.attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
        service_name='FortiWeb'
    )