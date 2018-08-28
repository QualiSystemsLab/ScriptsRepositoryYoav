from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from os import listdir
from os.path import isfile, join
import blueprint_commands

# Michael

sandbox = Sandbox()
# connectL1Routes(sandbox, None)

# loadNetworkingDevicesConfig(sandbox, None)

#
DefaultSetupWorkflow().register(sandbox)

def myfunction(sandbox , components):
    pass


sandbox.workflow.add_to_connectivity(blueprint_commands.connectL1Routes)
# sandbox.workflow.add_to_preparation(blueprint_commands.Deploy_DHCP_First)
# sandbox.workflow.add_to_preparation(blueprint_commands.solve_abstract_tgn)
# sandbox.workflow.add_to_provisioning(myfunction)


# model = sandbox.components.get_resources_by_model("GG")
# sandbox.workflow.add_to_configuration(blueprint_commands.loadNetworkingDevicesConfig, None)
# sandbox.workflow.add_to_configuration(blueprint_commands.restore_base_switch, None)
# sandbox.workflow.add_to_configuration(blueprint_commands.restore_test_switch, None)

#
#
sandbox.execute_setup()
#






