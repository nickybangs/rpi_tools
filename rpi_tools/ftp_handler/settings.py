import os
from pathlib import Path

HOME = Path(os.environ["HOME"])

FTP_PATH = Path("/media/pi/FTP")
LOG_FILENAME = "/home/pi/.local/.logs/ftp_handler.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(lineno)d " "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "logfile": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": LOG_FILENAME,
            "formatter": "default",
            "backupCount": 2,
        }
    },
    "loggers": {
        "ftp_handler": {
            "level": "DEBUG",
            "handlers": [
                "logfile",
            ],
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["logfile"]
    },
}
