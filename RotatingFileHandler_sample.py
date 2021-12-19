# https://www.kite.com/python/docs/logging.handlers.RotatingFileHandler

import logging
import logging.handlers
import glob

# Set up logger with appropriate handler
LOG_FILENAME = "rotate_file"
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)
my_logger.addHandler(handler)

# Rolling over to simulate log exceeding maxBytes size
handler.doRollover()

# Retrieve created files
logfiles = glob.glob("%s*" % LOG_FILENAME)

# Print files
for filename in logfiles:
    print(filename)
