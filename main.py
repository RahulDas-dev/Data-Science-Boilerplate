import logging
import logging.config
import os

from src.bar import bar

_dir_path = os.path.dirname(os.path.realpath(__file__))
LOGGER_CONFIG_FILE = os.path.join(_dir_path, "logger_config.ini")

if __name__ == "__main__":
    logging.config.fileConfig(LOGGER_CONFIG_FILE, disable_existing_loggers=False)
    bar()
