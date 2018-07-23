import json
import os
# try if 7.1 , except if 6.4
try:
    import cloudshell.helpers.scripts.cloudshell_scripts_helpers as helpers_71
    import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers_71
except:
    pass
try:
    import qualipy.scripts.cloudshell_scripts_helpers as helpers_64
    import qualipy.scripts.cloudshell_dev_helpers as dev_helpers_64
except:
    pass

def create_cs_session(debug):
    if debug == 'yes':
        try:
            dev_helpers_71.attach_to_cloudshell_as("admin", "admin", "Global",
                                                   reservation_id='59b547e3-6e9e-49d3-906f-2e28582ac98b',
                                                   server_address='q1.cisco.com')
        except:
            dev_helpers_64.attach_to_cloudshell_as("admin", "admin", "Global",
                                                   reservation_id='6376f07e-6d30-4b2b-811c-2eee0c77832b',
                                                   server_address='q1.cisco.com')

    try:
        session = helpers_71.get_api_session()
        helpers = helpers_71
    except:
        session = helpers_64.get_api_session()
        helpers = helpers_64
    return session, helpers