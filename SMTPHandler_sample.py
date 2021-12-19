# https://www.nullpo.io/2018/11/12/python-logging-mail/

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

sender = "emailuser@localhost"
pwd = "pass123"

smtpHandler = logging.handlers.SMTPHandler(
    mailhost=("localhost", 25),
    fromaddr="noreply@example.com",
    toaddrs="recipient@example.com",
    subject="alert!",
    credentials=(sender, pwd),
    secure=(),
)

smtpHandler.setLevel(logging.DEBUG)
logger.addHandler(smtpHandler)
logger.debug("here is the test logging for u.")
