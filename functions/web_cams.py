from loguru import logger
from information.resorts_data import get_resort


@logger.catch
async def get_webcam_url(resort: str) -> str:
    webcam_url = await get_resort('web-cams', resort)
    return webcam_url
