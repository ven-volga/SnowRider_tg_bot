import asyncio
import os
from copy import deepcopy
from typing import Any

from pymongo import MongoClient
from datetime import datetime

client_db = MongoClient(os.getenv('MONGO_URI'))
db = client_db.ski_assistant_tg
log = db.client_requests

services_log_null = {
    "_id": 1,
    "time_stamp": datetime.now(),
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


async def download_requests_log() -> dict:
    log_data = log.find_one()
    return log_data


async def join_logs() -> dict:
    last_requests = await download_requests_log()
    log.delete_one({"_id": 1})
    new_log = {}
    for resort in requests_log_day:
        if resort not in ("_id", "time_stamp"):
            new_log[resort] = {}
            for service in requests_log_day[resort]:
                new_log[resort][service] = requests_log_day[resort][service] + last_requests[resort][service]
        elif resort == "_id":
            new_log[resort] = 1
        elif resort == "time_stamp":
            new_log[resort] = datetime.now()
    return new_log


async def upload_requests_log() -> None:
    global requests_log_day
    new_log = await join_logs()
    log.insert_one(new_log)
    requests_log_day.clear()
    requests_log_day.update(deepcopy(services_log_null))


async def schedule_log_task() -> Any:
    while True:
        await asyncio.sleep(60 * 60 * 24)
        await upload_requests_log()
