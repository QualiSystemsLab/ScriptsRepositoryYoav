from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.teardown.default_teardown_orchestrator import DefaultTeardownWorkflow
from teardown_extra_commands import extra_teardown_commands

sandbox = Sandbox()
teardown_instance = extra_teardown_commands(sandbox.id)

DefaultTeardownWorkflow().register(sandbox)

sandbox.workflow.before_teardown_started(teardown_instance.before_started)

sandbox.workflow.add_to_teardown(teardown_instance.during_teardown)

sandbox.execute_teardown()