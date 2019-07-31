from cloudshell.api.cloudshell_api import CloudShellAPISession

class CloudShellAPIHandler():
    def __init__(self, cloudshell_data):
        self.session = CloudShellAPISession(
            host=cloudshell_data.get('host'),
            username=cloudshell_data.get('username'),
            password=cloudshell_data.get('password'),
            domain=cloudshell_data.get('domain')
        )

    def get_all_possible_values_for_attribute_on_resource(self, resource_model, attribute_name):
        attribute_values = []
        all_resources_from_model = self.session.FindResources(resourceModel=resource_model).Resources
        for resource in all_resources_from_model:
            resource_details = self.session.GetResourceDetails(resource.Name)
            attr_value = filter(lambda x:x.Name == attribute_name, resource_details.ResourceAttributes)[0]
            if attr_value not in attribute_values:
                attribute_values.append(attr_value.Value)
        return attribute_values

