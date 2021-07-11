import asyncio

from settings import Settings

class Worker:

	_logger = None
	_bot = None

	@classmethod
	async def Init(cls, bot, logger):
		cls._logger = logger
		cls._bot = bot
		await cls._EventLoop()


	@classmethod
	async def _EventLoop(cls):

		while True:
			# something work
			await asyncio.sleep(Settings.WORKER_EVENTLOOP_INTERVAL_SECONDS)

