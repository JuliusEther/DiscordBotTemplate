import asyncio
from logging import Logger

from discord.ext.commands import Bot

from bot.worker import Worker
from settings import Settings

class Core:

	_bot:Bot = None
	_logger:Logger = None

	@classmethod
	def Init(cls, logger:Logger):
		cls._logger = logger
		cls._bot = Bot(command_prefix=Settings.COMMAND_PREFIX)
		
		cls.Process()


	@classmethod
	def Process(cls):

		loop = asyncio.get_event_loop()
		futures = asyncio.gather(
			Worker.Init(cls._bot, cls._logger)
		)

		loop.run_until_complete(futures)
		
