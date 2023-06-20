import asyncio
from aiogram import executor
from create_bot import dp
from data_and_metrics.client_requests import schedule_log_task, upload_requests_log
from handlers import client, admin, other
from informations.resorts_data import get_db_data
from loguru import logger


async def on_startup(_: dp):
    logger.info('Bot is online!')
    await get_db_data()
    schedule_task = asyncio.create_task(schedule_log_task())
    await schedule_task


async def on_shutdown(_: dp):
    await upload_requests_log()
    logger.info('Bot is shutdown!\n')


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(on_startup(dp))
        executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)
    finally:
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
