from loguru import logger
from informations.resorts_data import get_resort


@logger.catch
async def get_webcam_url(resort):
    webcam_url = await get_resort('web-cams', resort)
    return webcam_url
