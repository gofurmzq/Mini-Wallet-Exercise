import logging
from logging import Formatter

from functools import lru_cache

_log_format = Formatter(f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
class MyFilter(object):
    def __init__(self, level):
        self.__level = level
    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

@lru_cache()
def get_logger():
    logger = logging.getLogger('Wallet-logger')

    return logger


logger = get_logger()
