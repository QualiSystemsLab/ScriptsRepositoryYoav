from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.storage import StorageManagementClient
from msrestazure.azure_active_directory import ServicePrincipalCredentials

from cloudshell.cp.azure.common.singletons import SingletonByArgsMeta
from cloudshell.cp.azure.common.singletons import AbstractComparableInstance

from cloudshell.api.cloudshell_api import CloudShellAPISession

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
    def __init__(self, azure_subscription_id, azure_tenant, azure_application_key, azure_application_id ):
        self.azure_subscription_id = azure_subscription_id
        self.azure_tenant = azure_tenant
        self.azure_application_key = azure_application_key
        self.azure_application_id = azure_application_id



# Cloudshell debug
user = 'yoav.e'
password = '1234'
server = '40.91.201.107'
azure_cp_name = 'azure'
session = CloudShellAPISession(host=server, username=user, password=password, domain='Global')
# vnet =[attr.Value for attr in azcp.ResourceAttributes if attr.Name == ''][0]
vnet = 'CloudShell-Sandbox-VNet'



resource_group = '531679c2-eca6-4c4b-97d7-f217d544624d'
# vm_name = 'apache-web-server-9883d10f'


azcp = session.GetResourceDetails(azure_cp_name)
clp = CloudProvider(
    azure_application_id=[attr.Value for attr in azcp.ResourceAttributes if attr.Name == 'Azure Application ID'][0],
    azure_subscription_id=[attr.Value for attr in azcp.ResourceAttributes if attr.Name == 'Azure Subscription ID'][
        0],
    azure_tenant=[attr.Value for attr in azcp.ResourceAttributes if attr.Name == 'Azure Tenant ID'][0],
    azure_application_key=session.DecryptPassword(
        [attr.Value for attr in azcp.ResourceAttributes if attr.Name == 'Azure Application Key'][0]).Value,
)
clients = AzureClientsManager(cloud_provider=clp)

# my actual code:



