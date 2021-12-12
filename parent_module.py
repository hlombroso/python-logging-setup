import logging
import child_module
from logging_with_yaml_config import setup_logging

setup_logging.initialize_loggers()
logger = logging.getLogger(__name__)

logger.info("starting script")
child_module.log_func()
