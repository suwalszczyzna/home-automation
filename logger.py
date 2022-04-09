import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from celery import signals
from celery.signals import after_setup_logger

import config

FORMATTER = logging.Formatter(config.logging_format)
LOG_FILE = config.log_filepath


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    # logger.addHandler(get_file_handler())
    return logger


@signals.celeryd_init.connect
def setup_log_format(sender, conf, **kwargs):
    conf.worker_log_format = config.logging_format.strip().format(sender)
    conf.worker_task_log_format = config.logging_format.format(sender)
