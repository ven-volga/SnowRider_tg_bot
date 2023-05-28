import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client_db = MongoClient(os.getenv('MONGO_URI'))
db = client_db.ski_assistant_tg
data = db.resorts_content

db_data: dict | None = None


def get_db_data():
    global db_data
    db_data = data.find_one()
    print("Data from database saved in value")


async def get_resort(service, resort_name):
    resort = db_data[service][resort_name]
    print("Data from value", service, resort_name)
    return resort
