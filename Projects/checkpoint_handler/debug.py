import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

def get_debug_session():
    username = 'yoav.e'
    password = '1111'
    domain = 'Global'
    server = '40.113.155.10'
    resId = '5f4b9ad5-7dbd-43c8-a36d-e5aaf9c7e155'
    dev_helpers.attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
        service_name='FortiWeb'
    )