from aiogram import types, Dispatcher
from create_bot import dp, bot
from informations.resorts_info import resorts_info
from keyboards import kb_resorts, kb_service
from functions.parce_hotels24 import parse_hotels, recommend_hotels, average_price
from functions.resorts_info import get_resort_info
from functions.weather import get_current_weather, get_future_weather
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

resort = None


async def command_start(message: types.Message):
    global resort
    resort = None
    await bot.send_message(message.chat.id,
                           f"Привіт, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, маю на меті "
                           f"допомоги тобі визначитись де катати в цьому році.\n️ <b>Тисни на курорт і обирай, "
                           f"що цікавить </b>⬇️",
                           reply_markup=kb_resorts, parse_mode='html')


async def command_resorts(message: types.Message):
    global resort
    resort = message.text
    await bot.send_message(message.chat.id, f"А я катав {resort}, неперевершено!\n"
                                            f"<b>Про що розповісти?</b>", reply_markup=kb_service, parse_mode='html')


async def command_hotels(message: types.Message):
    await bot.send_message(message.chat.id, f"<b>Шукаю інфо по житлу у {resort}.</b>\n"
                                            f"А поки я обробляю для тебе інформацію поміркуй... "
                                            f"Хто краще, сноубордист чи лижник 😉", parse_mode='html')

    # TODO use function average, min, max in bot answer
    prices = parse_hotels(resort)[1]

    hotels_kb = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=f"Переглянути пропозиції", callback_data='recommend_hotels'))

    await bot.send_message(message.chat.id,
                           f"Середня вартість проживання (1 ніч на 2 особи) у {resort} "
                           f"складає: {sum(prices) / len(prices)} грн.\n\n"
                           f"Мінімальна ціна з рекомендованих - {min(prices)} грн.\n"
                           f"Максимальна ціна з рекомендованих - {max(prices)} грн.\n\n",
                           reply_markup=hotels_kb, parse_mode='html')


async def command_recommends(callback: types.CallbackQuery):
    url_kb = InlineKeyboardMarkup(row_width=1)
    url_btn = InlineKeyboardButton(text="На сайт Hotels24.ua", url=resorts_info['hotels_links'][resort])
    url_kb.add(url_btn)

    await callback.message.answer(f"{recommend_hotels(resort)}", reply_markup=url_kb, parse_mode='html')
    await callback.answer()


async def command_resorts_info(message: types.Message):
    await bot.send_message(message.chat.id, get_resort_info(resort), reply_markup=kb_service,
                           parse_mode='html')


async def command_weather(message: types.Message):
    await bot.send_message(message.chat.id, get_current_weather(resort),
                           reply_markup=kb_service, parse_mode='html')

    await bot.send_message(message.chat.id, get_future_weather(resort),
                           reply_markup=kb_service, parse_mode='html')


async def command_equipment(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Інфо по екіпу в {resort} буде доступно, як тільки відбудеться старт сезону! "
                           f"Знаю, у мене вже теж ноги сверблять, потерпи поки випаде сніг і ми запизд*чимо окупантів!",
                           reply_markup=kb_service, parse_mode='html')


async def command_skipass(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Інфо по скіпасам в {resort} буде доступно, як тільки відбудеться старт сезону! "
                           f"Знаю, у мене вже теж ноги сверблять, потерпи поки випаде сніг і ми запизд*чимо окупантів!",
                           reply_markup=kb_service, parse_mode='html')


async def command_trains(message: types.Message):
    await bot.send_message(message.chat.id, f"В процесі, скоро інфо, як дістатися до {resort}", reply_markup=kb_service,
                           parse_mode='html')


def register_handler_client(dp: Dispatcher):  # реєстрація хендлерів у файлі
    dp.register_message_handler(command_start, lambda message: message.text in ["/start", "help", "info", "Назад"])
    dp.register_message_handler(command_resorts,
                                lambda message: message.text in ["Славське", "Драгобрат", "Буковель", "Пилипець",
                                                                 "Плай", "Яблуниця",
                                                                 "Красія", "Мигове", "Яремче"])
    dp.register_message_handler(command_hotels, lambda message: "Житло" in message.text)
    dp.register_message_handler(command_resorts_info, lambda message: "Про курорт" in message.text)
    dp.register_message_handler(command_weather, lambda message: "Погода" in message.text)
    dp.register_message_handler(command_equipment, lambda message: "Спорядження" in message.text)
    dp.register_message_handler(command_skipass, lambda message: "Ski-pass" in message.text)
    dp.register_message_handler(command_trains, lambda message: "Поїзди" in message.text)
    dp.register_callback_query_handler(command_recommends, text='recommend_hotels')
