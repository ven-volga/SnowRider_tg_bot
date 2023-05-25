from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
s2 = KeyboardButton("Погода")
s3 = KeyboardButton("Житло")
s4 = KeyboardButton("Спорядження")
s5 = KeyboardButton("Ski-pass")
s6 = KeyboardButton("Поїзди")
s7 = KeyboardButton("Назад")

kb_service = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_service.row(s1, s2, s3)
kb_service.row(s4, s5, s6)
kb_service.add(s7)
