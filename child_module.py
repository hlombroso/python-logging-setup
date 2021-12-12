import logging

# logging.basicConfig(level=logging.DEBUG, filename="log.log", format="%(asctime)s | %(name)s | %(levelname)s : %(message)s")

logger = logging.getLogger(__name__)


def log_func():
    logger.error("Child module executing")
