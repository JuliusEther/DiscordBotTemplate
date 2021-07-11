from discord.ext import commands
from settings import Settings

class Core:

	_bot = None
	_logger = None

	@classmethod
	def Init(cls, logger):
		cls._logger = logger
		cls._bot = commands.Bot(command_prefix=Settings.COMMAND_PREFIX)

