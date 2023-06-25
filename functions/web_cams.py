from loguru import logger
from information.resorts_data import get_resort


@logger.catch
async def get_webcam_url(resort: str) -> str:
    """
    Retrieves a link to a web page with webcams on the resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get the URL on the web page with webcams)
    :return: URL on the web page with webcams on the resort
    """
    webcam_url = await get_resort('web-cams', resort)
    return webcam_url
