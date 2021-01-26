import logging
from logging.handlers import RotatingFileHandler
import os
import sys
from conf import PROCESS_NAME
from directory_config import DirectoryConfig

DEFAULT_LOG_LEVEL = logging.INFO

# default max log file size = 20 MB
MAX_LOG_FILE_SIZE = 20 * 1024 * 1024
BACK_UP_COUNT = 3

FMT = logging.Formatter("%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s")

_global_dict = {}


def set_global_value(key, value):
    _global_dict[key] = value


def get_global_value(key, default_value=None):
    return _global_dict.get(key, default_value)


def get_logger(logger_name=PROCESS_NAME):
    existed_logger = get_global_value(logger_name)
    if existed_logger is not None:
        return existed_logger
    # log to stdout
    # https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FMT)
    logging.getLogger(logger_name).addHandler(console_handler)

    logger = logging.getLogger(logger_name)
    set_global_value(logger_name, logger)

    if os.getenv('DEBUG') == '1':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(DEFAULT_LOG_LEVEL)

    log_dir = DirectoryConfig.LOG_DIR
    if not logger_name.endswith('.log'):
        logger_name += '.log'
    log_path = os.path.join(log_dir, logger_name)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    file_handler = RotatingFileHandler(log_path, maxBytes=MAX_LOG_FILE_SIZE, backupCount=BACK_UP_COUNT)
    file_handler.setFormatter(FMT)
    logger.addHandler(file_handler)
    return logger


def enable_debug():
    lg = get_logger()
    lg.setLevel(logging.DEBUG)


def get_statistic_logger():
    return get_logger('statistics')


logger = get_logger()
