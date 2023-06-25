from loguru import logger
from information.resorts_data import get_resort


@logger.catch
async def get_skipass_info(resort: str) -> str:
    """
    Retrieves information about prices for ski-passes at the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about ski-pass prices at the resort)
    :return: A string with information about ski-passes prices at the selected resort.
    """
    ski_pass_data = await get_resort('skipass_info', resort)
    return ski_pass_data
