import asyncio
from logging import Logger

from discord.ext.commands import Bot

from settings import Settings

class Worker:

	_logger:Logger = None
	_bot = None

	@classmethod
	async def Init(cls, bot:Bot , logger:Logger):
		cls._logger = logger
		cls._bot = bot
		await cls._EventLoop()


	@classmethod
	async def _EventLoop(cls):

		while True:
			# something work
			await asyncio.sleep(Settings.WORKER_EVENTLOOP_INTERVAL_SECONDS)

