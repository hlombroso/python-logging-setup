import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log", format="%(asctime)s | %(name)s | %(levelname)s:%(message)s")
logger = logging.getLogger(__name__)

logger.info("starting script")
