from loguru import logger
from informations.resorts_data import get_resort


@logger.catch
async def get_train_info(resort):
    trains_data = await get_resort('trains_messages', resort)
    return trains_data


@logger.catch
async def get_train_url(resort):
    trains_url = await get_resort('trains_urls', resort)
    return trains_url
