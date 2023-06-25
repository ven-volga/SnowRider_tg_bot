from aiogram import types, Dispatcher
from create_bot import bot
from information.text_content import unknown_command_text
from keyboards import kb_resorts


async def unknown_command(message: types.Message) -> None:
    """
    Handles unknown commands by sending a message with predefined text
    and a reply keyboard containing resorts.

    :param message: The incoming message.
    """
    await bot.send_message(message.chat.id, unknown_command_text, reply_markup=kb_resorts, parse_mode='html')


def register_handler_other(dp: Dispatcher) -> None:
    """
    Registers the message handler for the other commands.

    :param dp: The Dispatcher instance.
    """
    dp.register_message_handler(unknown_command)
