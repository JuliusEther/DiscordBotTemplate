import asyncio

from discord.ext import commands

from bot.worker import Worker
from settings import Settings

class Core:

	_bot = None
	_logger = None

	@classmethod
	def Init(cls, logger):
		cls._logger = logger
		cls._bot = commands.Bot(command_prefix=Settings.COMMAND_PREFIX)
		
		cls.Process()


	@classmethod
	def Process(cls):

		loop = asyncio.get_event_loop()
		futures = asyncio.gather(
			Worker.Init(cls._bot, cls._logger)
		)

		loop.run_until_complete(futures)
		
