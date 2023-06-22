from aiogram import types, Dispatcher
from create_bot import bot
from information.text_content import unknown_command_text
from keyboards import kb_resorts


async def unknown_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, unknown_command_text, reply_markup=kb_resorts, parse_mode='html')


def register_handler_other(dp: Dispatcher) -> None:
    dp.register_message_handler(unknown_command)
