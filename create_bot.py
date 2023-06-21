from aiogram import Bot
from aiogram.dispatcher import Dispatcher  # обробка повідомлень в чаті
from dotenv import load_dotenv, find_dotenv  # отримання токена з віртуального оточення
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
import os

load_dotenv(find_dotenv())

log_path = os.getenv("LOG_PATH")
log_file = 'bot.log'
logger.add(log_path + log_file, format='{time:DD.MM.YYYY|H:mm:ss|Z}| {level} |{name}:{function}:{line} - {message}',
           rotation='1 MB', compression='zip', catch=True)

storage = MemoryStorage()

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)
