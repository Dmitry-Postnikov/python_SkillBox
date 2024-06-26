import logging
import sys

from different_levels import DifferentLevels

class ASCII(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return str.isascii(record.msg)

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
           "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "filters": {
        "isascii": {
            "()": ASCII
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": "sys.stdout",
            "filters": ["isascii"]
        },
        "multilevelfile": {
            "()": DifferentLevels,
            "level": "DEBUG",
            "formatter": "base",
            "filters": ["isascii"]
        },
        "time_rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "base",
            "when": "h",
            "interval": 10,
            "backupCount": 1,
            "filename": "utils.log",
            "filters": ["isascii"]
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["multilevelfile"]
        },
        "utils": {
            "level": "INFO",
            "handlers": ["time_rotating"]
        }
    }
}