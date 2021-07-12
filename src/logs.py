from logging import Logger, StreamHandler, getLogger
from logging.handlers import TimedRotatingFileHandler
import sys

from settings import Settings

class Logs:

    _logger: Logger = None

    @classmethod
    def Init(cls):
        cls._logger = getLogger(__name__)

        if Settings.LOG_FILE_OUT:
            filehandler = TimedRotatingFileHandler(f"{Settings.LOG_FILEPATH}/{Settings.LOG_FILENAME_BASE}")
            filehandler.when = "MIDNIGHT"
            filehandler.encoding = "UTF-8"
            filehandler.setLevel(Settings.LOG_FILE_LEVEL)

            cls._logger.addHandler(filehandler)

        if Settings.LOG_STD_ERR:
            stderrhandler = StreamHandler(sys.stderr)
            stderrhandler.setLevel(Settings.LOG_STD_ERR)

            cls._logger.addHandler(stderrhandler)


    @classmethod
    def GetLogger(cls) -> Logger:
        return cls._logger
