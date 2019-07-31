import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

resid = '704d62e3-2797-4ed7-ab63-c8c23b52e1a0'

username = 'admin'
password = 'admin'
server = '192.168.85.15'
domain = 'Global'

dev_help.attach_to_cloudshell_as(
    user=username,
    password=password,
    domain=domain,
    reservation_id=resid,
    server_address=server
)
session = script_help.get_api_session()

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


all_locations = []
all_resources = session.FindResources(resourceFamily='Compute Server')
for r in all_resources.Resources:
    all_locations.append(session.GetAttributeValue(
        resourceFullPath=r.Name,
        attributeName='Location'
    ).Value
    )
list_no_dups = f7(all_locations)
pass