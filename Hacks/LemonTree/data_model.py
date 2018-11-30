from cloudshell.shell.core.driver_context import ResourceCommandContext, AutoLoadDetails, AutoLoadAttribute, \
    AutoLoadResource
from collections import defaultdict


class LegacyUtils(object):
    def __init__(self):
        self._datamodel_clss_dict = self.__generate_datamodel_classes_dict()

    def migrate_autoload_details(self, autoload_details, context):
        model_name = context.resource.model
        root_name = context.resource.name
        root = self.__create_resource_from_datamodel(model_name, root_name)
        attributes = self.__create_attributes_dict(autoload_details.attributes)
        self.__attach_attributes_to_resource(attributes, '', root)
        self.__build_sub_resoruces_hierarchy(root, autoload_details.resources, attributes)
        return root

    def __create_resource_from_datamodel(self, model_name, res_name):
        return self._datamodel_clss_dict[model_name](res_name)

    def __create_attributes_dict(self, attributes_lst):
        d = defaultdict(list)
        for attribute in attributes_lst:
            d[attribute.relative_address].append(attribute)
        return d

    def __build_sub_resoruces_hierarchy(self, root, sub_resources, attributes):
        d = defaultdict(list)
        for resource in sub_resources:
            splitted = resource.relative_address.split('/')
            parent = '' if len(splitted) == 1 else resource.relative_address.rsplit('/', 1)[0]
            rank = len(splitted)
            d[rank].append((parent, resource))

        self.__set_models_hierarchy_recursively(d, 1, root, '', attributes)

    def __set_models_hierarchy_recursively(self, dict, rank, manipulated_resource, resource_relative_addr, attributes):
        if rank not in dict: # validate if key exists
            pass

        for (parent, resource) in dict[rank]:
            if parent == resource_relative_addr:
                sub_resource = self.__create_resource_from_datamodel(
                    resource.model.replace(' ', ''),
                    resource.name)
                self.__attach_attributes_to_resource(attributes, resource.relative_address, sub_resource)
                manipulated_resource.add_sub_resource(
                    self.__slice_parent_from_relative_path(parent, resource.relative_address), sub_resource)
                self.__set_models_hierarchy_recursively(
                    dict,
                    rank + 1,
                    sub_resource,
                    resource.relative_address,
                    attributes)

    def __attach_attributes_to_resource(self, attributes, curr_relative_addr, resource):
        for attribute in attributes[curr_relative_addr]:
            setattr(resource, attribute.attribute_name.lower().replace(' ', '_'), attribute.attribute_value)
        del attributes[curr_relative_addr]

    def __slice_parent_from_relative_path(self, parent, relative_addr):
        if parent is '':
            return relative_addr
        return relative_addr[len(parent) + 1:] # + 1 because we want to remove the seperator also

    def __generate_datamodel_classes_dict(self):
        return dict(self.__collect_generated_classes())

    def __collect_generated_classes(self):
        import sys, inspect
        return inspect.getmembers(sys.modules[__name__], inspect.isclass)


class Checkpoint(object):
    def __init__(self, name):
        """
        
        """
        self.attributes = {}
        self.resources = {}
        self._cloudshell_model_name = 'Checkpoint'
        self._name = name

    def add_sub_resource(self, relative_path, sub_resource):
        self.resources[relative_path] = sub_resource

    @classmethod
    def create_from_context(cls, context):
        """
        Creates an instance of NXOS by given context
        :param context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :return:
        :rtype Checkpoint
        """
        result = Checkpoint(name=context.resource.name)
        for attr in context.resource.attributes:
            result.attributes[attr] = context.resource.attributes[attr]
        return result

    def create_autoload_details(self, relative_path=''):
        """
        :param relative_path:
        :type relative_path: str
        :return
        """
        resources = [AutoLoadResource(model=self.resources[r].cloudshell_model_name,
            name=self.resources[r].name,
            relative_address=self._get_relative_path(r, relative_path))
            for r in self.resources]
        attributes = [AutoLoadAttribute(relative_path, a, self.attributes[a]) for a in self.attributes]
        autoload_details = AutoLoadDetails(resources, attributes)
        for r in self.resources:
            curr_path = relative_path + '/' + r if relative_path else r
            curr_auto_load_details = self.resources[r].create_autoload_details(curr_path)
            autoload_details = self._merge_autoload_details(autoload_details, curr_auto_load_details)
        return autoload_details

    def _get_relative_path(self, child_path, parent_path):
        """
        Combines relative path
        :param child_path: Path of a model within it parent model, i.e 1
        :type child_path: str
        :param parent_path: Full path of parent model, i.e 1/1. Might be empty for root model
        :type parent_path: str
        :return: Combined path
        :rtype str
        """
        return parent_path + '/' + child_path if parent_path else child_path

    @staticmethod
    def _merge_autoload_details(autoload_details1, autoload_details2):
        """
        Merges two instances of AutoLoadDetails into the first one
        :param autoload_details1:
        :type autoload_details1: AutoLoadDetails
        :param autoload_details2:
        :type autoload_details2: AutoLoadDetails
        :return:
        :rtype AutoLoadDetails
        """
        for attribute in autoload_details2.attributes:
            autoload_details1.attributes.append(attribute)
        for resource in autoload_details2.resources:
            autoload_details1.resources.append(resource)
        return autoload_details1

    @property
    def cloudshell_model_name(self):
        """
        Returns the name of the Cloudshell model
        :return:
        """
        return 'Checkpoint'

    @property
    def cloud(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.Cloud'] if 'Checkpoint.Cloud' in self.attributes else None

    @cloud.setter
    def cloud(self, value='azure'):
        """
        Cloud provider to use
        :type value: str
        """
        self.attributes['Checkpoint.Cloud'] = value

    @property
    def admin_username(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.Admin Username'] if 'Checkpoint.Admin Username' in self.attributes else None

    @admin_username.setter
    def admin_username(self, value):
        """
        User with administrative privileges
        :type value: str
        """
        self.attributes['Checkpoint.Admin Username'] = value

    @property
    def admin_password(self):
        """
        :rtype: string
        """
        return self.attributes['Checkpoint.Admin Password'] if 'Checkpoint.Admin Password' in self.attributes else None

    @admin_password.setter
    def admin_password(self, value):
        """
        
        :type value: string
        """
        self.attributes['Checkpoint.Admin Password'] = value

    @property
    def admin_password_plain(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.Admin Password Plain'] if 'Checkpoint.Admin Password Plain' in self.attributes else None

    @admin_password_plain.setter
    def admin_password_plain(self, value):
        """
        
        :type value: str
        """
        self.attributes['Checkpoint.Admin Password Plain'] = value

    @property
    def nic1_address(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.NIC1_Address'] if 'Checkpoint.NIC1_Address' in self.attributes else None

    @nic1_address.setter
    def nic1_address(self, value):
        """
        
        :type value: str
        """
        self.attributes['Checkpoint.NIC1_Address'] = value

    @property
    def nic2_address(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.NIC2_Address'] if 'Checkpoint.NIC2_Address' in self.attributes else None

    @nic2_address.setter
    def nic2_address(self, value):
        """
        
        :type value: str
        """
        self.attributes['Checkpoint.NIC2_Address'] = value

    @property
    def address(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.Address'] if 'Checkpoint.Address' in self.attributes else None

    @address.setter
    def address(self, value):
        """
        Address for remote access
        :type value: str
        """
        self.attributes['Checkpoint.Address'] = value

    @property
    def role(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.Role'] if 'Checkpoint.Role' in self.attributes else None

    @role.setter
    def role(self, value):
        """
        role for this service
        :type value: str
        """
        self.attributes['Checkpoint.Role'] = value

    @property
    def vm_name(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.VM Name'] if 'Checkpoint.VM Name' in self.attributes else None

    @vm_name.setter
    def vm_name(self, value):
        """
        this VM Name
        :type value: str
        """
        self.attributes['Checkpoint.VM Name'] = value

    @property
    def status(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.status'] if 'Checkpoint.status' in self.attributes else None

    @status.setter
    def status(self, value):
        """
        deployed , pending or error
        :type value: str
        """
        self.attributes['Checkpoint.status'] = value

    @property
    def public_address(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.public Address'] if 'Checkpoint.public Address' in self.attributes else None

    @public_address.setter
    def public_address(self, value):
        """
        Public Address for remote access
        :type value: str
        """
        self.attributes['Checkpoint.public Address'] = value

    @property
    def router_facing_address(self):
        """
        :rtype: str
        """
        return self.attributes['Checkpoint.router facing Address'] if 'Checkpoint.router facing Address' in self.attributes else None

    @router_facing_address.setter
    def router_facing_address(self, value):
        """
        Public Address for remote access
        :type value: str
        """
        self.attributes['Checkpoint.router facing Address'] = value

    @property
    def name(self):
        """
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        
        :type value: str
        """
        self._name = value

    @property
    def cloudshell_model_name(self):
        """
        :rtype: str
        """
        return self._cloudshell_model_name

    @cloudshell_model_name.setter
    def cloudshell_model_name(self, value):
        """
        
        :type value: str
        """
        self._cloudshell_model_name = value



