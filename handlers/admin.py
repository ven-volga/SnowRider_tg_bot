from aiogram import types, Dispatcher
from create_bot import bot
from data_and_metrics.client_requests import download_requests_log


async def parce_log_data():
    log_string = ""
    log_data = await download_requests_log()
    for keys in log_data:
        if keys == "time_stamp":
            log_string += f"<b><i>Log on: {log_data[keys].strftime('%d %B %G %H:%M')}</i></b>\n\n"
        elif keys != "_id":
            log_string += f"<b>{keys}</b>: {str(log_data[keys])[1:-1]}\n\n"
    return log_string


async def command_get_log_data(message: types.Message):
    if message.from_user.id == 574267783:
        log_data = await parce_log_data()
        await bot.send_message(message.chat.id, log_data, parse_mode='html')
    else:
        await bot.send_message(message.chat.id, "You must be my admin", parse_mode='html')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(command_get_log_data, lambda message: "show_me_log" in message.text)
