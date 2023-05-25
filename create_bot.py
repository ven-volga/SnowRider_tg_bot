from aiogram import Bot
from aiogram.dispatcher import Dispatcher  # обробка повідомлень в чаті
from dotenv import load_dotenv, find_dotenv  # отримання токена з віртуального оточення
import os

load_dotenv(find_dotenv())  # find token value

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
