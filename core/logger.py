import logging
import logging.config
import os
import sys

from logging import FileHandler
from logging.handlers import RotatingFileHandler

FOLDER_LOGS = os.path.join(os.getcwd(), 'logs')

if not os.path.exists(FOLDER_LOGS):
    os.mkdir(FOLDER_LOGS)

ROOT_LOG = 'common.log'
OUTPUT_LOG = 'only_gui.log'

DATEFORMAT = '%Y-%m-%d %H:%M:%S'


ROOT_FORMATTER = logging.Formatter(
    fmt="%(asctime)s > %(filename)s > %(lineno)s > %(levelname)s : %(message)s",
    datefmt=DATEFORMAT
)

CONSOLE_FORMATTER = logging.Formatter(
    fmt="%(asctime)s > %(filename)s > %(lineno)s > %(levelname)s : %(message)s",
    datefmt=DATEFORMAT
)

LOGGER_FORMATTER = logging.Formatter(
    fmt="%(asctime)s > %(module)s > %(levelname)s : %(message)s",
    datefmt=DATEFORMAT
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CONSOLE_FORMATTER)
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def get_file_handler():
    file_handler = RotatingFileHandler(os.path.join(FOLDER_LOGS, ROOT_LOG), maxBytes=4096, encoding='utf-8')
    file_handler.setFormatter(ROOT_FORMATTER)
    file_handler.setLevel(logging.DEBUG)
    return file_handler


def get_current_launch_file_handler():
    file_handler = FileHandler(os.path.join(FOLDER_LOGS, OUTPUT_LOG), mode='w', encoding='utf-8')
    file_handler.setFormatter(LOGGER_FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler


root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(get_console_handler())
root.addHandler(get_file_handler())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(get_current_launch_file_handler())
