import asyncio
import os
from copy import deepcopy
from pymongo import MongoClient
from datetime import datetime
from loguru import logger
from typing import NoReturn

client_db = MongoClient(os.getenv('MONGO_URI'))
db = client_db.ski_assistant_tg
log = db.client_requests
unique_users = set()
unique_users_list = []
log_update_time = 30 #60 * 60 * 10  # sec * min * h


services_log_null = {
    "_id": 1,
    "time_stamp": datetime.now(),
    "unique_users": unique_users_list,
    "Славське": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Драгобрат": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Буковель": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Пилипець": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Плай": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Яблуниця": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Красія": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Мигове": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
    "Яремче": {"Про курорт": 0, "Погода": 0, "Житло": 0, "web-cams": 0, "Ski-pass": 0, "Потяги": 0},
}

requests_log_day = deepcopy(services_log_null)


@logger.catch
async def download_requests_log() -> dict[str, dict[str, int] | int | datetime]:
    """
    This function retrieves the request log data from the database and returns it as a dictionary.
    :return: dict[str, dict[str, int] | int | datetime]: Dictionary representing the request log data.
    :except: If an exception occurs during the download, the exception data is added to the log file with loguru.
    """
    log_data = log.find_one()
    return log_data


@logger.catch
async def join_logs() -> dict[str, dict[str, int] | int | datetime]:
    """
    Retrieves the last requests from the database, deletes the previous log,
    and creates a new log by merging the current and previous request histories.
    Returns a dictionary with the actual request count for each resort and service.

    :return: dict[str, dict[str, int] | int | datetime]:
            Dictionary with the actual request count for each resort and service
    """
    global unique_users_list
    last_requests = await download_requests_log()
    log.delete_one({"_id": 1})
    new_log = {}
    for resort in requests_log_day:
        if resort not in ("_id", "time_stamp", "unique_users"):
            new_log[resort] = {}
            for service in requests_log_day[resort]:
                new_log[resort][service] = requests_log_day[resort][service] + last_requests[resort][service]
        elif resort == "_id":
            new_log[resort] = 1
        elif resort == "time_stamp":
            new_log[resort] = datetime.now()
        elif resort == "unique_users":
            last_requests[resort].extend(list(unique_users))
            unique_users_list = set(last_requests[resort])
            new_log[resort] = list(unique_users_list)
            print(new_log[resort])
    logger.debug('Merging user request log from DB and current request log')
    return new_log


@logger.catch
async def upload_requests_log() -> NoReturn:
    """
    Uploads the current user request log into the database,
    clears the daily request log, and logs the action.
    """
    global requests_log_day
    new_log = await join_logs()
    log.insert_one(new_log)
    requests_log_day.clear()
    requests_log_day.update(deepcopy(services_log_null))
    logger.success('Request log uploaded to the database')


@logger.catch
async def schedule_log_task() -> NoReturn:
    """
    Creates a scheduled task to upload the current query log to the database.
    The task runs every "log_update_time".
    """
    while True:
        await asyncio.sleep(log_update_time)
        await upload_requests_log()
