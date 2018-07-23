from cloudshell.core.logger import qs_logger

logger = qs_logger._create_logger(
    log_group='a',
    log_category='b',
    log_file_prefix='c'
)
logger.error(
    msg = 'bla'
)
pass