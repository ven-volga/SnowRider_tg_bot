from aiogram.utils import executor  # start bot to online
from create_bot import dp


async def on_startup(_):  # when bot started (connect to database)
    print("Bot is online!")


from handlers import client, other

# імпорт функцій з модулів client, admin, other
client.register_handler_client(dp)
# admin.register_handler_admin(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # start bot and ignore offline messages
