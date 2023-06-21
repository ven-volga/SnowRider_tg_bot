from aiogram import Bot
from aiogram.dispatcher import Dispatcher  # обробка повідомлень в чаті
from dotenv import load_dotenv, find_dotenv  # отримання токена з віртуального оточення
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
import os

logger.add('./logs/bot.log', format='{time:DD.MM.YYYY | H:mm:ss | Z} {level} {message}',
           rotation='1 MB', compression='zip', catch=True)

storage = MemoryStorage()

load_dotenv(find_dotenv())  # find token value

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)
