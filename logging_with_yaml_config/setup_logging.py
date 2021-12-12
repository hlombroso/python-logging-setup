import logging
import logging.config
import os
import sys
import yaml

default_level = logging.DEBUG
default_config_file = "logging_config.yml"
# default_log_filename = "logs.log"
# default_file_format = "%(asctime)s - %(name)-10s - %(levelname)-8s : %(message)s"
# default_console_format = "%(asctime)s %(levelname)-8s : %(message)s"

current_directory = os.path.dirname(__file__)

# load custom config file
custom_config_path = os.path.join(current_directory, "custom_config.yml")
with open(custom_config_path, "r") as config_file:
    custom_config = yaml.safe_load(config_file)


def init_with_basic_config(levelname):
    print("Initializing with basic config")

    logger = logging.getLogger("root")

    consoleFormatter = logging.Formatter(custom_config["default_console_format"])
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(consoleFormatter)
    consoleHandler.setLevel(levelname)

    fileFormatter = logging.Formatter(custom_config["default_file_format"])
    fileHandler = logging.FileHandler(custom_config["default_log_filename"])
    fileHandler.setFormatter(fileFormatter)
    fileHandler.setLevel(levelname)

    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)


def update_filehandler_filename(log_directory, logging_config):
    if log_directory is None:
        log_directory = custom_config["log_directory"]

    if not os.path.isdir(log_directory):
        os.makedirs(log_directory)

    for handler, fileHandler in logging_config["handlers"].items():
        if handler != "consoleHandler":
            fileHandler["filename"] = os.path.join(log_directory, fileHandler["filename"])


def initialize_loggers(levelname=default_level, config_filepath=None, log_directory=None):

    if config_filepath is None:
        config_filepath = os.path.join(current_directory, default_config_file)

    if os.path.isfile(config_filepath):
        try:
            with open(config_filepath, "r") as f:
                logging_config = yaml.safe_load(f)
                update_filehandler_filename(log_directory, logging_config)
                logging.config.dictConfig(logging_config)
                # print(f"Logging successfully configured with the config file {config_filepath}")
        except Exception as e:
            print("Failed to load config file")
            print(f"Error message: {type(e).__name__}, {str(e)}")
            init_with_basic_config(levelname)
    else:
        print(f"Could not find the config file. Path: {config_filepath}")
        init_with_basic_config(levelname)


if __name__ == "__main__":
    initialize_loggers()
