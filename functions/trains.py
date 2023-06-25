from loguru import logger
from information.resorts_data import get_resort


@logger.catch
async def get_train_info(resort: str) -> str:
    """
    Retrieves information about the nearest railway station to the resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about the nearest railway station to the resort)
    :return: A string with information about the nearest railway station to the resort.
    """
    trains_data = await get_resort('trains_messages', resort)
    return trains_data


@logger.catch
async def get_train_url(resort: str) -> str:
    """
    Retrieves a link to a web page with information about train traffic at the nearest railway station to the resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get the URL on the web page with information about train traffic)
    :return: URL on the web page with information about train traffic
    """
    trains_url = await get_resort('trains_urls', resort)
    return trains_url
