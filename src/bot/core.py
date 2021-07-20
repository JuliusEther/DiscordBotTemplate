import asyncio
from logging import Logger

from discord.ext.commands import Bot

from settings import Settings

class Core:

	_bot:Bot = None
	_logger:Logger = None

	@classmethod
	def Init(cls, logger:Logger):
		cls._logger = logger
		cls._bot = Bot(command_prefix=Settings.COMMAND_PREFIX, intents=Settings.BOT_INTENTS)
		cls.LoadExtensions()
		cls.Process()


	@classmethod
	def Process(cls):
		loop = asyncio.get_event_loop()
		try:
			loop.run_until_complete(cls._bot.start(Settings.TOKEN))
		except KeyboardInterrupt:
			loop.run_until_complete(cls._bot.close())
		finally:
			loop.close()

	@classmethod
	def LoadExtensions(cls):
		for ext in Settings.EXTENSIONS:
			cls._bot.load_extension(ext)


	@classmethod
	def GetLogger(cls) -> Logger:
		return cls._logger
