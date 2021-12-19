from logging_with_yaml_config import setup_logging
import logging

setup_logging.initialize_loggers()
errorLogger = logging.getLogger("error")
logger = logging.getLogger("prod")


def report_error():
    errorLogger.error("error message")


# log something
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
report_error()

try:
    pass
except Exception as e:
    logger.error(e, exc_info=True)
