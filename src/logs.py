from logging import Logger, StreamHandler, getLogger, Formatter
from logging.handlers import TimedRotatingFileHandler
import sys
import os

from settings import Settings

class Logs:

    _logger: Logger = None

    @classmethod
    def Init(cls):
        cls._logger = getLogger(__name__)

        if Settings.LOG_FILE_OUT:
            filehandler = TimedRotatingFileHandler(os.path.join(Settings.LOG_FILEPATH, Settings.LOG_FILENAME_BASE))
            filehandler.when = "MIDNIGHT"
            filehandler.encoding = "UTF-8"
            filehandler.setLevel(Settings.LOG_FILE_LEVEL)
            filehandler.setFormatter(Formatter(Settings.LOG_FORMAT, Settings.LOG_DATETIME_FORMAT))

            cls._logger.addHandler(filehandler)

        if Settings.LOG_STD_ERR:
            stderrhandler = StreamHandler(sys.stderr)
            stderrhandler.setLevel(Settings.LOG_STD_ERR)
            stderrhandler.setFormatter(Formatter(Settings.LOG_FORMAT, Settings.LOG_DATETIME_FORMAT))

            cls._logger.addHandler(stderrhandler)


    @classmethod
    def GetLogger(cls) -> Logger:
        return cls._logger
