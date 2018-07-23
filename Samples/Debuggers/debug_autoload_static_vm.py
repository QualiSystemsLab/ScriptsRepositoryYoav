import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as sch

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'
new_server = 'localhost'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
for a in range(15):
    device_name = 'Device {0}'.format(str(a + 20))
    session.CreateResource(
        resourceFamily='DUT',
        resourceModel='DUT Model',
        resourceName=device_name,
        resourceAddress='1.1.1.1',
        folderFullPath='CPEs'
    )
    session.SetAttributeValue(
        resourceFullPath=device_name,
        attributeName='Ansible Parameters',
        attributeValue='hello'
    )
    session.SetAttributesValues(
        resourcesAttributesUpdateRequests=[api.ResourceAttributesUpdateRequest(
            ResourceFullName=device_name,
            AttributeNamesValues=[api.AttributeNameValue(
                Name='Ansible Playbook URL',
                Value='some attribute value'
            )]

        )]
    )
    # session.AutoLoad(
    #     resourceFullPath=device_name
    # )
pass
