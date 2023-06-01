import asyncio
from aiogram import executor
from create_bot import dp
from data_and_metrics.client_requests import schedule_log_task, upload_requests_log
from handlers import client, other, admin
from datetime import datetime
from informations.resorts_data import get_db_data


async def on_startup(_: dp):
    print("Bot is online! Started at", datetime.now().strftime('%d %B %G %H:%M:%S'))
    await get_db_data()
    schedule_task = asyncio.create_task(schedule_log_task())  # Запуск відкладеної функції у асинхронній петлі
    await schedule_task  # Очікування завершення відкладеної задачі


async def on_shutdown(_: dp):
    await upload_requests_log()


# імпорт функцій з модулів client, admin, other
client.register_handler_client(dp)
admin.register_handler_admin(dp)
# other.register_handler_other(dp)

# Запуск бота з використанням асинхронної петлі asyncio
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
