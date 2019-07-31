from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_logic import DefaultSetupLogic
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from retrying_qslogger.retrying_qslogger import retry

class custom_provisioning():
    def __init__(self):
        pass


    def provisioning_overrider(self, sandbox, components):
        result = self._provisioning_overrider(sandbox, components)
        return result

    @retry(stop_max_attempt_number=3)
    def _provisioning_overrider(self, sandbox, components):
        """
        :param Sandbox sandbox:
        :return:
        """
        api = sandbox.automation_api

        default_setup_instance = DefaultSetupWorkflow()

        sandbox.logger.info("Executing non-default provisioning")

        reservation_details = api.GetReservationDetails(sandbox.id)

        default_setup_instance._deploy_result = DefaultSetupLogic.deploy_apps_in_reservation(api=api,
                                                                           reservation_details=reservation_details,
                                                                           reservation_id=sandbox.id,
                                                                           logger=sandbox.logger)

        DefaultSetupLogic.validate_all_apps_deployed(deploy_results=default_setup_instance._deploy_result,
                                                     logger=sandbox.logger)

        sandbox.components.refresh_components(sandbox=sandbox)
        return None

