from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.storage import StorageManagementClient
from msrestazure.azure_active_directory import ServicePrincipalCredentials

from cloudshell.cp.azure.common.singletons import SingletonByArgsMeta
from cloudshell.cp.azure.common.singletons import AbstractComparableInstance


class AzureClientsManager(AbstractComparableInstance):
    __metaclass__ = SingletonByArgsMeta

    def check_params_equality(self, cloud_provider, *args, **kwargs):
        """Check if instance have the same attributes for initializing Azure session as provided in cloud_provider

        :param cloud_provider: AzureCloudProviderResourceModel instance
        :return: (bool) True/False whether attributes are same or not
        """
        subscription_id = self._get_subscription(cloud_provider)
        application_id = self._get_azure_application_id(cloud_provider)
        application_key = self._get_azure_application_key(cloud_provider)
        tenant = self._get_azure_tenant(cloud_provider)

        return all([
            subscription_id == self._subscription_id,
            application_id == self._application_id,
            application_key == self._application_key,
            tenant == self._tenant])

    def __init__(self, cloud_provider):
        """
        :param cloud_provider: AzureCloudProviderResourceModel instance
        :return
        """
        self._subscription_id = self._get_subscription(cloud_provider)
        self._application_id = self._get_azure_application_id(cloud_provider)
        self._application_key = self._get_azure_application_key(cloud_provider)
        self._tenant = self._get_azure_tenant(cloud_provider)
        self._service_credentials = self._get_service_credentials()
        self._compute_client = None
        self._network_client = None
        self._storage_client = None
        self._resource_client = None
        self._subscription_client = None

    def _get_service_credentials(self):
        return ServicePrincipalCredentials(client_id=self._application_id, secret=self._application_key, tenant=self._tenant)

    def _get_subscription(self, cloud_provider_model):
        return cloud_provider_model.azure_subscription_id

    def _get_azure_application_id(self, cloud_provider_model):
        return cloud_provider_model.azure_application_id

    def _get_azure_application_key(self, cloud_provider_model):
        return cloud_provider_model.azure_application_key

    def _get_azure_tenant(self, cloud_provider_model):
        return cloud_provider_model.azure_tenant

    @property
    def compute_client(self):
        if self._compute_client is None:
            with SingletonByArgsMeta.lock:
                if self._compute_client is None:
                    self._compute_client = ComputeManagementClient(self._service_credentials, self._subscription_id)

        return self._compute_client

    @property
    def network_client(self):
        if self._network_client is None:
            with SingletonByArgsMeta.lock:
                if self._network_client is None:
                    self._network_client = NetworkManagementClient(self._service_credentials, self._subscription_id)

        return self._network_client

    @property
    def storage_client(self):
        if self._storage_client is None:
            with SingletonByArgsMeta.lock:
                if self._storage_client is None:
                    self._storage_client = StorageManagementClient(self._service_credentials, self._subscription_id)

        return self._storage_client

    @property
    def resource_client(self):
        if self._resource_client is None:
            with SingletonByArgsMeta.lock:
                if self._resource_client is None:
                    self._resource_client = ResourceManagementClient(self._service_credentials, self._subscription_id)

        return self._resource_client

    @property
    def subscription_client(self):
        if self._subscription_client is None:
            with SingletonByArgsMeta.lock:
                if self._subscription_client is None:
                    self._subscription_client = SubscriptionClient(self._service_credentials)

        return self._subscription_client


class CloudProvider(object):
    def __init__(self):
        self.azure_subscription_id = '2e7282ee-327d-489d-a984-ba05199ce714'
        self.azure_tenant = '2ddf94f6-3085-43a9-8545-d589001de126'
        self.azure_application_key = 'ZrRB6q03jqIODXtEdISs0+36hYzvLk87x5fBh8Wwzbk='
        self.azure_application_id = '271525dd-b4c1-4f7b-8cff-0b4edb0b72b2'


resource_group = '79e8de37-a35b-4121-a37c-195fe6ae4233'
vm_name = 'azurevm-fb17ff68'
clp = CloudProvider()
clients = AzureClientsManager(cloud_provider=clp)
vm = clients.compute_client.virtual_machines.get(resource_group_name=resource_group, vm_name=vm_name)
nic_name = vm.network_profile.network_interfaces[0].id.split('/')[-1]
nic = clients.network_client.network_interfaces.get(resource_group_name=resource_group, network_interface_name=nic_name)
print vm.name
# my actual code:
qq = clients.network_client.public_ip_addresses.get(
    resource_group_name=resource_group,
    public_ip_address_name=vm.name
)
new_domain_name = 'qqqqq'
qq.domain_name_label = new_domain_name
qq.dns_settings.domain_name_label = new_domain_name
qq.dns_settings.fqdn = '{0}.westeurope.cloudapp.azure.com'.format(new_domain_name)
qq.fqdn = '{0}.westeurope.cloudapp.azure.com'.format(new_domain_name)

clients.network_client.public_ip_addresses.create_or_update(
    resource_group_name=resource_group,
    public_ip_address_name=vm.name,
    parameters=qq
)
pass