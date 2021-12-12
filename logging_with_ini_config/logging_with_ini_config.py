import logging
import logging.config

# set up logging
logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)
logger = logging.getLogger("dev")

# log something
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
