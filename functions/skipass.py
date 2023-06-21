from loguru import logger
from informations.resorts_data import get_resort


@logger.catch
async def get_skipass_info(resort):
    ski_pass_data = await get_resort('skipass_info', resort)
    return ski_pass_data

