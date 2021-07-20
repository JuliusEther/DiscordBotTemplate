from discord import Intents

class Settings:
	TOKEN = ""
	COMMAND_PREFIX = "!"
	WORKER_EVENTLOOP_INTERVAL_SECONDS = 10.0

	BOT_INTENTS = Intents.default()

	LOG_FILE_OUT = True
	LOG_FILE_LEVEL = "INFO"
	LOG_FILEPATH = "./logs/"
	LOG_FILENAME_BASE = "bot.log"

	LOG_STD_ERR = True
	LOG_STD_ERR = "INFO"
	
	LOG_FORMAT = r"%(asctime)s.%(msecs)03d [%(levelname)-8s] (%(filename)s:%(lineno)s): %(message)s"
	LOG_DATETIME_FORMAT = r"%Y-%m-%d %H:%M:%S"

	EXTENSIONS = [
		"cogs.greetings"
	]