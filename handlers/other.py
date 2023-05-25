from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "Hello!":
        await message.answer("Hello my little rider!")
    else:
        await message.answer(message.text)


def register_handler_other(dp: Dispatcher):  # реєстрація хендлерів у файлі
    dp.register_message_handler(echo_send)
    #next handler