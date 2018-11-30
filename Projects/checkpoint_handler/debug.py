import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

def get_debug_session():
    username = 'yoav.e'
    password = '1111'
    domain = 'Global'
    server = '40.113.155.10'
    resId = 'a3abeb7b-794f-485a-ab9a-9d82b97a8beb'
    dev_helpers.attach_to_cloudshell_as(
        user=username,
        password=password,
        domain=domain,
        server_address=server,
        reservation_id=resId,
        service_name='CheckpointMgmt'
    )