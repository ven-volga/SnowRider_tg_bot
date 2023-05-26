from aiogram import types, Dispatcher
from create_bot import bot
from informations.resorts_info import get_resort
from informations.text_content import *
from keyboards import kb_resorts, kb_service
from functions.parce_hotels24 import recommend_hotels, general_hotels_price
from functions.resorts_info import get_resort_info
from functions.weather import get_current_weather, get_future_weather
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

resort = None


async def command_start(message: types.Message):
    global resort
    resort = None
    await bot.send_message(message.chat.id,
                           welcome_text.format(first_name=message.from_user.first_name,
                                               last_name=message.from_user.last_name),
                           reply_markup=kb_resorts, parse_mode='html')


async def command_resorts(message: types.Message):
    global resort
    resort = message.text
    await bot.send_message(message.chat.id, choose_resort_text.format(resort=resort),
                           reply_markup=kb_service, parse_mode='html')


async def command_hotels(message: types.Message):
    try:
        hotels_price_info = general_hotels_price(resort)
        if resort:
            await bot.send_message(message.chat.id, hotels_info_text.format(resort=resort), parse_mode='html')

            hotels_kb = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=f"Переглянути пропозиції", callback_data='recommend_hotels'))

            await bot.send_message(message.chat.id, hotels_price_text.format(
                resort=resort, average=hotels_price_info[0], min=hotels_price_info[1], max=hotels_price_info[2]),
                                   reply_markup=hotels_kb, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_recommends(callback: types.CallbackQuery):
    url_kb = InlineKeyboardMarkup(row_width=1)
    url_btn = InlineKeyboardButton(text="На сайт Hotels24.ua", url=get_resort('hotels_links', resort))
    url_kb.add(url_btn)

    await callback.message.answer(f"{recommend_hotels(resort)}", reply_markup=url_kb, parse_mode='html')
    await callback.answer()


async def command_resorts_info(message: types.Message):
    try:
        if resort:
            await bot.send_message(message.chat.id, get_resort_info(resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_weather(message: types.Message):
    try:
        if resort:
            weather_kb = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=f"Погода на найближчі дні", callback_data="future_weather_output"))

            await bot.send_message(message.chat.id, get_current_weather(resort),
                                   reply_markup=weather_kb, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def callback_weather_handler(query: types.CallbackQuery):
    data = query.data
    message = query.message
    if data == "future_weather_output":
        await bot.send_message(message.chat.id, get_future_weather(resort), reply_markup=kb_service, parse_mode='html')


async def command_equipment(message: types.Message):
    try:
        if resort:
            await bot.send_message(message.chat.id, fish_text.format(resort=resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_skipass(message: types.Message):
    try:
        if resort:
            await bot.send_message(message.chat.id, fish_text.format(resort=resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_trains(message: types.Message):
    try:
        if resort:
            await bot.send_message(message.chat.id, fish_text.format(resort=resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def handle_exception(exception, message):
    if isinstance(exception, KeyError):
        await bot.send_message(message.chat.id, except_key_error_text, reply_markup=kb_resorts, parse_mode='html')
    else:
        pass


def register_handler_client(dp: Dispatcher):  # реєстрація хендлерів у файлі
    dp.register_message_handler(command_start, lambda message: message.text in ["/start", "help", "info", "Назад"])
    dp.register_message_handler(command_resorts,
                                lambda message:
                                message.text in ("Славське", "Драгобрат", "Буковель", "Пилипець", "Плай", "Яблуниця",
                                                 "Красія", "Мигове", "Яремче")
                                )

    dp.register_message_handler(command_hotels, lambda message: "Житло" in message.text)
    dp.register_message_handler(command_resorts_info, lambda message: "Про курорт" in message.text)
    dp.register_message_handler(command_weather, lambda message: "Погода" in message.text)
    dp.register_message_handler(command_equipment, lambda message: "Екіп" in message.text)
    dp.register_message_handler(command_skipass, lambda message: "Ski-pass" in message.text)
    dp.register_message_handler(command_trains, lambda message: "Поїзди" in message.text)
    dp.register_callback_query_handler(command_recommends, text='recommend_hotels')
    dp.register_callback_query_handler(callback_weather_handler)
