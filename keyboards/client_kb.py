from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

r1 = KeyboardButton("Славське")
r2 = KeyboardButton("Драгобрат")
r3 = KeyboardButton("Буковель")
r4 = KeyboardButton("Пилипець")
r5 = KeyboardButton("Плай")
r6 = KeyboardButton("Яблуниця")
r7 = KeyboardButton("Красія")
r8 = KeyboardButton("Мигове")
r9 = KeyboardButton("Яремче")

kb_resorts = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # заміщає стандартну клавіатуру

kb_resorts.row(r1, r2, r3)
kb_resorts.row(r4, r5, r6)
kb_resorts.row(r7, r8, r9)


s1 = KeyboardButton("Про курорт")
s2 = KeyboardButton("Веб-камери")
s3 = KeyboardButton("Погода")
s4 = KeyboardButton("Житло")
s5 = KeyboardButton("Потяги")
s6 = KeyboardButton("Ski-pass")
s7 = KeyboardButton("До вибору курорту")

kb_service = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_service.row(s1, s2, s3)
kb_service.row(s4, s5, s6)
kb_service.add(s7)

resort_options_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Траси", callback_data="resort_tracks"),
    InlineKeyboardButton(text="Як доїхати", callback_data="how_get_to_resort"),
    InlineKeyboardButton(text="Де поїсти", callback_data="how_get_to_resort"),
    InlineKeyboardButton(text="Що подивитись", callback_data="how_get_to_resort"))

