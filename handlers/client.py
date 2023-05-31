from aiogram import types, Dispatcher
from create_bot import bot
from functions.trains import get_train_url, get_train_info
from informations.resorts_data import get_resort
from informations.text_content import *
from keyboards import kb_resorts, kb_service
from functions.hotels import recommend_hotels, general_hotels_price
from functions.resorts_info import get_resort_info, how_to_get
from functions.weather import get_current_weather, get_future_weather
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ResortState(StatesGroup):
    ChoosingResort = State()


async def command_start(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.chat.id,
                           welcome_text.format(first_name=message.from_user.first_name,
                                               last_name=message.from_user.last_name),
                           reply_markup=kb_resorts, parse_mode='html')


async def command_resorts(message: types.Message, state: FSMContext):
    await state.finish()
    await state.update_data(resort=message.text)
    await bot.send_message(message.chat.id, choose_resort_text.format(resort=message.text),
                           reply_markup=kb_service, parse_mode='html')


async def command_hotels(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')
        hotels_price_info = await general_hotels_price(resort)

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


async def command_recommends(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    resort = data.get('resort')

    hotels_url = await get_resort('hotels_links', resort)
    url_kb = InlineKeyboardMarkup(row_width=1)
    url_btn = InlineKeyboardButton(text="На сайт Hotels24.ua", url=hotels_url)
    url_kb.add(url_btn)

    top_hotels = await recommend_hotels(resort)
    await callback.message.answer(top_hotels, reply_markup=url_kb, parse_mode='html')
    await callback.answer()


async def command_resorts_info(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')

        if resort:
            how_to_get_kb = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=f"Як доїхати до {resort}", callback_data="how_get_to_resort"))

            resort_info = await get_resort_info(resort)
            await bot.send_message(message.chat.id, resort_info, reply_markup=how_to_get_kb, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def callback_how_to_get_handler(query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    resort = data.get('resort')

    how_to_get_info = await how_to_get(resort)
    await bot.send_message(query.message.chat.id, how_to_get_info,
                           reply_markup=kb_service, parse_mode='html')


async def command_weather(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')

        if resort:
            weather_kb = InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text=f"Погода на найближчі дні",
                                     callback_data="future_weather_output"))

            current_weather = await get_current_weather(resort)
            await bot.send_message(message.chat.id, current_weather,
                                   reply_markup=weather_kb, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def callback_future_weather_handler(query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    resort = data.get('resort')

    future_weather = await get_future_weather(resort)
    await bot.send_message(query.message.chat.id, future_weather,
                           reply_markup=kb_service, parse_mode='html')


async def command_equipment(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')

        if resort:
            await bot.send_message(message.chat.id, fish_text.format(resort=resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_skipass(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')

        if resort:
            await bot.send_message(message.chat.id, fish_text.format(resort=resort),
                                   reply_markup=kb_service, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def command_trains(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        resort = data.get('resort')

        if resort:
            train_url = await get_train_url(resort)
            trains_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(
                text=f"До розкладу руху", url=train_url))

            train_info = await get_train_info(resort)
            await bot.send_message(message.chat.id, train_info,
                                   reply_markup=trains_kb, parse_mode='html')
        else:
            raise KeyError()
    except Exception as e:
        await handle_exception(e, message)


async def handle_exception(exception, message):
    if isinstance(exception, KeyError):
        await bot.send_message(message.chat.id, except_key_error_text, reply_markup=kb_resorts, parse_mode='html')
    else:
        pass


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, lambda message: message.text in ("/start", "help", "info",
                                                                                "До вибору курорту"))
    dp.register_message_handler(command_resorts, lambda message: message.text in
                                                                 ("Славське", "Драгобрат", "Буковель", "Пилипець",
                                                                  "Плай", "Яблуниця", "Красія", "Мигове", "Яремче"))
    dp.register_message_handler(command_hotels, lambda message: "Житло" in message.text)
    dp.register_message_handler(command_resorts_info, lambda message: "Про курорт" in message.text)
    dp.register_message_handler(command_weather, lambda message: "Погода" in message.text)
    dp.register_message_handler(command_equipment, lambda message: "Споряга" in message.text)
    dp.register_message_handler(command_skipass, lambda message: "Ski-pass" in message.text)
    dp.register_message_handler(command_trains, lambda message: "Потяги" in message.text)
    dp.register_callback_query_handler(command_recommends, text='recommend_hotels')
    dp.register_callback_query_handler(callback_future_weather_handler, text='future_weather_output')
    dp.register_callback_query_handler(callback_how_to_get_handler, text='how_get_to_resort')
