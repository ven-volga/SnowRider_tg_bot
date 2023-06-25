import os
from typing import NoReturn

from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from loguru import logger

load_dotenv(find_dotenv())

client_db = MongoClient(os.getenv('MONGO_URI'))
db = client_db.ski_assistant_tg
data = db.resorts_content

db_data: dict | None = None


@logger.catch
async def get_db_data() -> NoReturn:
    """
    Download all resorts information and save it in the global variable db_data.
    Add information about this operation in the log.
    """
    global db_data
    db_data = data.find_one()
    logger.success('Data from database loaded successfully')


@logger.catch
async def get_resort(service: str, resort_name: str) -> str | list:
    """
    Retrieves information for a specified resort and service.

    :param service: The name of the bot service command.
    :param resort_name: The name of the resort.
    :return: The requested information for the specified resort and service.
    """
    resort = db_data[service][resort_name]
    return resort
