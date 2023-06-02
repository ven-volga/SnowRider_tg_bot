from aiogram import types, Dispatcher


# TODO write welcome message to unknown command
async def echo_send(message: types.Message):
    if message.text == "Hello!":
        await message.answer("Hello my little rider!")
    else:
        await message.answer(message.text)


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
