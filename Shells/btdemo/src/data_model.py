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


class Btdemo(object):
    def __init__(self, name):
        """
        
        """
        self.attributes = {}
        self.resources = {}
        self._cloudshell_model_name = 'Btdemo'
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
        :rtype Btdemo
        """
        result = Btdemo(name=context.resource.name)
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
        return 'Btdemo'

    @property
    def my_property(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.my_property'] if 'Btdemo.my_property' in self.attributes else None

    @my_property.setter
    def my_property(self, value='fast'):
        """
        Some attribute description
        :type value: str
        """
        self.attributes['Btdemo.my_property'] = value

    @property
    def chipset(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Chipset'] if 'Btdemo.Chipset' in self.attributes else None

    @chipset.setter
    def chipset(self, value):
        """
        Description of the chipset used by this broadband media appliance
        :type value: str
        """
        self.attributes['Btdemo.Chipset'] = value

    @property
    def subscriber_id(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Subscriber ID'] if 'Btdemo.Subscriber ID' in self.attributes else None

    @subscriber_id.setter
    def subscriber_id(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.Subscriber ID'] = value

    @property
    def account_number(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Account Number'] if 'Btdemo.Account Number' in self.attributes else None

    @account_number.setter
    def account_number(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.Account Number'] = value

    @property
    def user(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.User'] if 'Btdemo.User' in self.attributes else None

    @user.setter
    def user(self, value):
        """
        User with administrative privileges
        :type value: str
        """
        self.attributes['Btdemo.User'] = value

    @property
    def password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.Password'] if 'Btdemo.Password' in self.attributes else None

    @password.setter
    def password(self, value):
        """
        
        :type value: string
        """
        self.attributes['Btdemo.Password'] = value

    @property
    def enable_password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.Enable Password'] if 'Btdemo.Enable Password' in self.attributes else None

    @enable_password.setter
    def enable_password(self, value):
        """
        The enable password is required by some CLI protocols such as Telnet and is required according to the device configuration.
        :type value: string
        """
        self.attributes['Btdemo.Enable Password'] = value

    @property
    def power_management(self):
        """
        :rtype: bool
        """
        return self.attributes['Btdemo.Power Management'] if 'Btdemo.Power Management' in self.attributes else None

    @power_management.setter
    def power_management(self, value=True):
        """
        Used by the power management orchestration, if enabled, to determine whether to automatically manage the device power status. Enabled by default.
        :type value: bool
        """
        self.attributes['Btdemo.Power Management'] = value

    @property
    def sessions_concurrency_limit(self):
        """
        :rtype: float
        """
        return self.attributes['Btdemo.Sessions Concurrency Limit'] if 'Btdemo.Sessions Concurrency Limit' in self.attributes else None

    @sessions_concurrency_limit.setter
    def sessions_concurrency_limit(self, value='1'):
        """
        The maximum number of concurrent sessions that the driver will open to the device. Default is 1 (no concurrency).
        :type value: float
        """
        self.attributes['Btdemo.Sessions Concurrency Limit'] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Version'] if 'Btdemo.Version' in self.attributes else None

    @version.setter
    def version(self, value=''):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.Version'] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Serial Number'] if 'Btdemo.Serial Number' in self.attributes else None

    @serial_number.setter
    def serial_number(self, value=''):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.Serial Number'] = value

    @property
    def tr069_user(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.TR069 User'] if 'Btdemo.TR069 User' in self.attributes else None

    @tr069_user.setter
    def tr069_user(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.TR069 User'] = value

    @property
    def tr069_password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.TR069 Password'] if 'Btdemo.TR069 Password' in self.attributes else None

    @tr069_password.setter
    def tr069_password(self, value):
        """
        
        :type value: string
        """
        self.attributes['Btdemo.TR069 Password'] = value

    @property
    def snmp_read_community(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.SNMP Read Community'] if 'Btdemo.SNMP Read Community' in self.attributes else None

    @snmp_read_community.setter
    def snmp_read_community(self, value):
        """
        The SNMP Read-Only Community String is like a password. It is sent along with each SNMP Get-Request and allows (or denies) access to device.
        :type value: string
        """
        self.attributes['Btdemo.SNMP Read Community'] = value

    @property
    def snmp_write_community(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.SNMP Write Community'] if 'Btdemo.SNMP Write Community' in self.attributes else None

    @snmp_write_community.setter
    def snmp_write_community(self, value):
        """
        The SNMP Write Community String is like a password. It is sent along with each SNMP Set-Request and allows (or denies) chaning MIBs values.
        :type value: string
        """
        self.attributes['Btdemo.SNMP Write Community'] = value

    @property
    def snmp_v3_user(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.SNMP V3 User'] if 'Btdemo.SNMP V3 User' in self.attributes else None

    @snmp_v3_user.setter
    def snmp_v3_user(self, value):
        """
        Relevant only in case SNMP V3 is in use.
        :type value: str
        """
        self.attributes['Btdemo.SNMP V3 User'] = value

    @property
    def snmp_v3_password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.SNMP V3 Password'] if 'Btdemo.SNMP V3 Password' in self.attributes else None

    @snmp_v3_password.setter
    def snmp_v3_password(self, value):
        """
        Relevant only in case SNMP V3 is in use.
        :type value: string
        """
        self.attributes['Btdemo.SNMP V3 Password'] = value

    @property
    def snmp_v3_private_key(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.SNMP V3 Private Key'] if 'Btdemo.SNMP V3 Private Key' in self.attributes else None

    @snmp_v3_private_key.setter
    def snmp_v3_private_key(self, value):
        """
        Relevant only in case SNMP V3 is in use.
        :type value: str
        """
        self.attributes['Btdemo.SNMP V3 Private Key'] = value

    @property
    def snmp_version(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.SNMP Version'] if 'Btdemo.SNMP Version' in self.attributes else None

    @snmp_version.setter
    def snmp_version(self, value=''):
        """
        The version of SNMP to use. Possible values are v1, v2c and v3.
        :type value: str
        """
        self.attributes['Btdemo.SNMP Version'] = value

    @property
    def enable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes['Btdemo.Enable SNMP'] if 'Btdemo.Enable SNMP' in self.attributes else None

    @enable_snmp.setter
    def enable_snmp(self, value=True):
        """
        If set to True and SNMP isn???t enabled yet in the device the Shell will automatically enable SNMP in the device when Autoload command is called. SNMP must be enabled on the device for the Autoload command to run successfully. True by default.
        :type value: bool
        """
        self.attributes['Btdemo.Enable SNMP'] = value

    @property
    def disable_snmp(self):
        """
        :rtype: bool
        """
        return self.attributes['Btdemo.Disable SNMP'] if 'Btdemo.Disable SNMP' in self.attributes else None

    @disable_snmp.setter
    def disable_snmp(self, value=False):
        """
        If set to True SNMP will be disabled automatically by the Shell after the Autoload command execution is completed. False by default.
        :type value: bool
        """
        self.attributes['Btdemo.Disable SNMP'] = value

    @property
    def console_server_ip_address(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Console Server IP Address'] if 'Btdemo.Console Server IP Address' in self.attributes else None

    @console_server_ip_address.setter
    def console_server_ip_address(self, value):
        """
        The IP address of the console server, in IPv4 format.
        :type value: str
        """
        self.attributes['Btdemo.Console Server IP Address'] = value

    @property
    def console_user(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Console User'] if 'Btdemo.Console User' in self.attributes else None

    @console_user.setter
    def console_user(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.Console User'] = value

    @property
    def console_port(self):
        """
        :rtype: float
        """
        return self.attributes['Btdemo.Console Port'] if 'Btdemo.Console Port' in self.attributes else None

    @console_port.setter
    def console_port(self, value):
        """
        The port on the console server, usually TCP port, which the device is associated with.
        :type value: float
        """
        self.attributes['Btdemo.Console Port'] = value

    @property
    def console_password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.Console Password'] if 'Btdemo.Console Password' in self.attributes else None

    @console_password.setter
    def console_password(self, value):
        """
        
        :type value: string
        """
        self.attributes['Btdemo.Console Password'] = value

    @property
    def cli_connection_type(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.CLI Connection Type'] if 'Btdemo.CLI Connection Type' in self.attributes else None

    @cli_connection_type.setter
    def cli_connection_type(self, value='Auto'):
        """
        The CLI connection type that will be used by the driver. Possible values are Auto, Console, SSH, Telnet and TCP. If Auto is selected the driver will choose the available connection type automatically. Default value is Auto.
        :type value: str
        """
        self.attributes['Btdemo.CLI Connection Type'] = value

    @property
    def cli_tcp_port(self):
        """
        :rtype: float
        """
        return self.attributes['Btdemo.CLI TCP Port'] if 'Btdemo.CLI TCP Port' in self.attributes else None

    @cli_tcp_port.setter
    def cli_tcp_port(self, value):
        """
        TCP Port to user for CLI connection. If kept empty a default CLI port will be used based on the chosen protocol, for example Telnet will use port 23.
        :type value: float
        """
        self.attributes['Btdemo.CLI TCP Port'] = value

    @property
    def backup_location(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Backup Location'] if 'Btdemo.Backup Location' in self.attributes else None

    @backup_location.setter
    def backup_location(self, value):
        """
        Used by the save/restore orchestration to determine where backups should be saved.
        :type value: str
        """
        self.attributes['Btdemo.Backup Location'] = value

    @property
    def backup_type(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Backup Type'] if 'Btdemo.Backup Type' in self.attributes else None

    @backup_type.setter
    def backup_type(self, value='File System'):
        """
        Supported protocols for saving and restoring of configuration and firmware files. Possible values are 'File System' 'FTP' and 'TFTP'. Default value is 'File System'.
        :type value: str
        """
        self.attributes['Btdemo.Backup Type'] = value

    @property
    def backup_user(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.Backup User'] if 'Btdemo.Backup User' in self.attributes else None

    @backup_user.setter
    def backup_user(self, value):
        """
        Username for the storage server used for saving and restoring of configuration and firmware files.
        :type value: str
        """
        self.attributes['Btdemo.Backup User'] = value

    @property
    def backup_password(self):
        """
        :rtype: string
        """
        return self.attributes['Btdemo.Backup Password'] if 'Btdemo.Backup Password' in self.attributes else None

    @backup_password.setter
    def backup_password(self, value):
        """
        Password for the storage server used for saving and restoring of configuration and firmware files.
        :type value: string
        """
        self.attributes['Btdemo.Backup Password'] = value

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

    @property
    def system_name(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.System Name'] if 'CS_BroadbandMediaChassis.System Name' in self.attributes else None

    @system_name.setter
    def system_name(self, value):
        """
        A unique identifier for the device, if exists in the device terminal/os.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.System Name'] = value

    @property
    def vendor(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.Vendor'] if 'CS_BroadbandMediaChassis.Vendor' in self.attributes else None

    @vendor.setter
    def vendor(self, value=''):
        """
        The name of the device manufacture.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.Vendor'] = value

    @property
    def contact_name(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.Contact Name'] if 'CS_BroadbandMediaChassis.Contact Name' in self.attributes else None

    @contact_name.setter
    def contact_name(self, value):
        """
        The name of a contact registered in the device.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.Contact Name'] = value

    @property
    def location(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.Location'] if 'CS_BroadbandMediaChassis.Location' in self.attributes else None

    @location.setter
    def location(self, value=''):
        """
        The device physical location identifier. For example Lab1/Floor2/Row5/Slot4.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.Location'] = value

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.Model'] if 'CS_BroadbandMediaChassis.Model' in self.attributes else None

    @model.setter
    def model(self, value=''):
        """
        The device model. This information is typically used for abstract resource filtering.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.Model'] = value

    @property
    def model_name(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.Model Name'] if 'CS_BroadbandMediaChassis.Model Name' in self.attributes else None

    @model_name.setter
    def model_name(self, value=''):
        """
        The catalog name of the device model. This attribute will be displayed in CloudShell instead of the CloudShell model.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.Model Name'] = value

    @property
    def os_version(self):
        """
        :rtype: str
        """
        return self.attributes['CS_BroadbandMediaChassis.OS Version'] if 'CS_BroadbandMediaChassis.OS Version' in self.attributes else None

    @os_version.setter
    def os_version(self, value=''):
        """
        Version of the Operating System.
        :type value: str
        """
        self.attributes['CS_BroadbandMediaChassis.OS Version'] = value


class GenericMediaPort(object):
    def __init__(self, name):
        """
        
        """
        self.attributes = {}
        self.resources = {}
        self._cloudshell_model_name = 'Btdemo.GenericMediaPort'
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
        :rtype GenericMediaPort
        """
        result = GenericMediaPort(name=context.resource.name)
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
        return 'GenericMediaPort'

    @property
    def media_type(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Media Type'] if 'Btdemo.GenericMediaPort.Media Type' in self.attributes else None

    @media_type.setter
    def media_type(self, value='Ethernet'):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Media Type'] = value

    @property
    def transport_technology(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Transport Technology'] if 'Btdemo.GenericMediaPort.Transport Technology' in self.attributes else None

    @transport_technology.setter
    def transport_technology(self, value):
        """
        Voice Packet Transmistion Type (e.g. SIP/MGCP)
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Transport Technology'] = value

    @property
    def mac_address(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.MAC Address'] if 'Btdemo.GenericMediaPort.MAC Address' in self.attributes else None

    @mac_address.setter
    def mac_address(self, value=''):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.MAC Address'] = value

    @property
    def ipv4_address(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.IPv4 Address'] if 'Btdemo.GenericMediaPort.IPv4 Address' in self.attributes else None

    @ipv4_address.setter
    def ipv4_address(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.IPv4 Address'] = value

    @property
    def ipv6_address(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.IPv6 Address'] if 'Btdemo.GenericMediaPort.IPv6 Address' in self.attributes else None

    @ipv6_address.setter
    def ipv6_address(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.IPv6 Address'] = value

    @property
    def bandwidth(self):
        """
        :rtype: float
        """
        return self.attributes['Btdemo.GenericMediaPort.Bandwidth'] if 'Btdemo.GenericMediaPort.Bandwidth' in self.attributes else None

    @bandwidth.setter
    def bandwidth(self, value):
        """
        The current interface bandwidth, in MB.
        :type value: float
        """
        self.attributes['Btdemo.GenericMediaPort.Bandwidth'] = value

    @property
    def class_of_service(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Class Of Service'] if 'Btdemo.GenericMediaPort.Class Of Service' in self.attributes else None

    @class_of_service.setter
    def class_of_service(self, value):
        """
        The current Class (or type) of Service to this device; Programs, Package or Contract names acceptable
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Class Of Service'] = value

    @property
    def public_ip(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Public IP'] if 'Btdemo.GenericMediaPort.Public IP' in self.attributes else None

    @public_ip.setter
    def public_ip(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Public IP'] = value

    @property
    def core_platform(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Core Platform'] if 'Btdemo.GenericMediaPort.Core Platform' in self.attributes else None

    @core_platform.setter
    def core_platform(self, value):
        """
        The core services platform the port is currently provisioned for.
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Core Platform'] = value

    @property
    def telephone_number(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericMediaPort.Telephone Number'] if 'Btdemo.GenericMediaPort.Telephone Number' in self.attributes else None

    @telephone_number.setter
    def telephone_number(self, value):
        """
        Current phone number assigned to this port, relevant for a phone port.
        :type value: str
        """
        self.attributes['Btdemo.GenericMediaPort.Telephone Number'] = value

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

    @property
    def model_name(self):
        """
        :rtype: str
        """
        return self.attributes['CS_Port.Model Name'] if 'CS_Port.Model Name' in self.attributes else None

    @model_name.setter
    def model_name(self, value=''):
        """
        The catalog name of the device model. This attribute will be displayed in CloudShell instead of the CloudShell model.
        :type value: str
        """
        self.attributes['CS_Port.Model Name'] = value


class GenericPowerPort(object):
    def __init__(self, name):
        """
        
        """
        self.attributes = {}
        self.resources = {}
        self._cloudshell_model_name = 'Btdemo.GenericPowerPort'
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
        :rtype GenericPowerPort
        """
        result = GenericPowerPort(name=context.resource.name)
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
        return 'GenericPowerPort'

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericPowerPort.Model'] if 'Btdemo.GenericPowerPort.Model' in self.attributes else None

    @model.setter
    def model(self, value):
        """
        The device model. This information is typically used for abstract resource filtering.
        :type value: str
        """
        self.attributes['Btdemo.GenericPowerPort.Model'] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericPowerPort.Serial Number'] if 'Btdemo.GenericPowerPort.Serial Number' in self.attributes else None

    @serial_number.setter
    def serial_number(self, value):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericPowerPort.Serial Number'] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericPowerPort.Version'] if 'Btdemo.GenericPowerPort.Version' in self.attributes else None

    @version.setter
    def version(self, value):
        """
        The firmware version of the resource.
        :type value: str
        """
        self.attributes['Btdemo.GenericPowerPort.Version'] = value

    @property
    def port_description(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericPowerPort.Port Description'] if 'Btdemo.GenericPowerPort.Port Description' in self.attributes else None

    @port_description.setter
    def port_description(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes['Btdemo.GenericPowerPort.Port Description'] = value

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

    @property
    def model_name(self):
        """
        :rtype: str
        """
        return self.attributes['CS_PowerPort.Model Name'] if 'CS_PowerPort.Model Name' in self.attributes else None

    @model_name.setter
    def model_name(self, value=''):
        """
        The catalog name of the device model. This attribute will be displayed in CloudShell instead of the CloudShell model.
        :type value: str
        """
        self.attributes['CS_PowerPort.Model Name'] = value


class GenericWifiCard(object):
    def __init__(self, name):
        """
        
        """
        self.attributes = {}
        self.resources = {}
        self._cloudshell_model_name = 'Btdemo.GenericWifiCard'
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
        :rtype GenericWifiCard
        """
        result = GenericWifiCard(name=context.resource.name)
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
        return 'GenericWifiCard'

    @property
    def mac_address(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericWifiCard.MAC Address'] if 'Btdemo.GenericWifiCard.MAC Address' in self.attributes else None

    @mac_address.setter
    def mac_address(self, value=''):
        """
        
        :type value: str
        """
        self.attributes['Btdemo.GenericWifiCard.MAC Address'] = value

    @property
    def chipset(self):
        """
        :rtype: str
        """
        return self.attributes['Btdemo.GenericWifiCard.Chipset'] if 'Btdemo.GenericWifiCard.Chipset' in self.attributes else None

    @chipset.setter
    def chipset(self, value):
        """
        Description of the chipset used by this broadband media appliance
        :type value: str
        """
        self.attributes['Btdemo.GenericWifiCard.Chipset'] = value

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

    @property
    def wifi_protocol(self):
        """
        :rtype: str
        """
        return self.attributes['CS_WiFiCard.WiFi Protocol'] if 'CS_WiFiCard.WiFi Protocol' in self.attributes else None

    @wifi_protocol.setter
    def wifi_protocol(self, value):
        """
        Wi-Fi protocol type (e.g. 802.11n, 802.11ac)
        :type value: str
        """
        self.attributes['CS_WiFiCard.WiFi Protocol'] = value

    @property
    def frequency(self):
        """
        :rtype: str
        """
        return self.attributes['CS_WiFiCard.Frequency'] if 'CS_WiFiCard.Frequency' in self.attributes else None

    @frequency.setter
    def frequency(self, value):
        """
        Values can be 2.5 GHz or 5 GHz
        :type value: str
        """
        self.attributes['CS_WiFiCard.Frequency'] = value



