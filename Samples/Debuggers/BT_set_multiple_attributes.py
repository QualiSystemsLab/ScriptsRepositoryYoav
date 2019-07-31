from cloudshell.api.cloudshell_api import CloudShellAPISession, ResourceAttributesUpdateRequest, AttributeNameValue


username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

session = CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)
res_id = '111'

attr_changes = []
a = ResourceAttributesUpdateRequest(
    ResourceFullName='resource_name',
    AttributeNamesValues=
    [AttributeNameValue(
        Name='Name',
        Value='value'
                       ),
    AttributeNameValue(
            Name='Name_2',
            Value='value_2'
                       )
    ]
)
attr_changes.append(a)
session.SetAttributesValues(
    resourcesAttributesUpdateRequests=attr_changes

)

