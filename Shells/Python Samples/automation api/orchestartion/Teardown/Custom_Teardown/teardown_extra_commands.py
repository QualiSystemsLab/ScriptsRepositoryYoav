from cloudshell.core.logger import qs_logger
from cloudshell.workflow.orchestration.sandbox import Sandbox


class extra_teardown_commands():
    def __init__(self, resid):
        self.logger = qs_logger.get_qs_logger(
            log_group=resid,
            log_category='BT_custom_teardown',
            log_file_prefix='BT_Teardown'
        )

    def before_started(self, sandbox, compononets):
        try:
            self.logger.info('did this before teardown')
        except Exception as e:
            self.logger.error('couldn\'t do that. reason :{}'.format(e.message))

    def during_teardown(self, sandbox, compononets):
        try:
            self.logger.info('did this during teardown')
        except Exception as e:
            self.logger.error('couldn\'t do that. reason :{}'.format(e.message))





