from quali_utils.quali_packaging import PackageEditor
from quali_api import QualiAPISession
from cloudshell_api import CloudShellAPIHandler

# constants
cloudshell_data = {
    'username': 'admin',
    'password': 'admin',
    'domain': 'Global',
    'host': 'localhost'
}
my_path = r'c:\temp\stam_package.zip'
blueprint_name = "el Zilcho"


cs_api = CloudShellAPIHandler(cloudshell_data)
dut_possible_names = cs_api.get_all_possible_values_for_attribute_on_resource(
    resource_model='AP',
    attribute_name='DutName'
)
quali_utils_session = PackageEditor()
quali_api_session = QualiAPISession(
    host=cloudshell_data.get('host'),
    username=cloudshell_data.get('username'),
    password=cloudshell_data.get('password'),
    domain=cloudshell_data.get('domain')
)
quali_api_session.ExportPackage(blueprint_name, my_path)
quali_utils_session.load(my_path)
quali_utils_session.add_attribute_to_abstract(
    topology_name=blueprint_name,
    abstract_path='atahall',
    attribute_name='DutName',
    possible_values=dut_possible_names,
    default_value='atahall-3',
    required='true',
    publish='false'

)
quali_api_session.ImportPackage(my_path)
pass