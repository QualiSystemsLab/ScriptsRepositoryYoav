from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.teardown.default_teardown_orchestrator import DefaultTeardownWorkflow
import blueprint_commands

sandbox = Sandbox()

DefaultTeardownWorkflow().register(sandbox)

sandbox.workflow.add_to_teardown(blueprint_commands.restore_test_switch, None)

sandbox.execute_teardown()
