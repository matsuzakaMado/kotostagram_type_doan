# -*- coding: utf-8 -*-
import logging
import os
import random
from time import sleep

logger = logging.getLogger('sns.utils')

_format = '%(asctime)s [%(name)s] [%(filename)s:%(lineno)s] [%(levelname)s] %(message)s'


def init_loggers():
    logger = logging.getLogger('sns')  # type: logging.Logger
    level = logging.INFO
    if os.getenv('LOG_LEVEL'):
        level = logging.getLevelName(os.getenv('LOG_LEVEL'))
    try:
        logger.setLevel(level)
    except:
        logger.setLevel(logging.INFO)

    # Stream
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(_format))
    logger.addHandler(ch)


def random_sleep(self, min_seconds=0.5, max_seconds=2):
    wait = random.random() * (max_seconds - min_seconds) + min_seconds
    sleep(wait)
