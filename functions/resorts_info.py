from loguru import logger
from information.resorts_data import get_resort


@logger.catch
async def get_resort_info(resort: str) -> str:
    """
    Obtains general information about the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about the resort)
    :return: A string with information about the selected resort.
    """
    resort_data = await get_resort('resorts_info', resort)
    return resort_data


@logger.catch
async def how_to_get(resort: str) -> str:
    """
    Retrieves information on how to get to the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information on how to get to the resort)
    :return: A string with information on how to get to the selected resort.
    """
    road_data = await get_resort('how_to_get_info', resort)
    return road_data


@logger.catch
async def get_tracks_info(resort: str) -> str:
    """
    Retrieves information about tracks at the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about tracks at the resort)
    :return: A string with information about tracks at the selected resort.
    """
    tracks_data = await get_resort('tracks_info', resort)
    return tracks_data


@logger.catch
async def get_food_info(resort: str) -> str:
    """
    Retrieves information about restaurants and cafes at the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about restaurants and cafes at the resort)
    :return: A string with information about restaurants and cafes at the selected resort.
    """
    food_data_list = await get_resort('food_info', resort)
    food_data_string = ''
    for restaurant in food_data_list:
        food_data_string += restaurant
    return food_data_string


@logger.catch
async def get_attractions_info(resort: str) -> str:
    """
    Retrieves information about attractions at the selected resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get information about attractions at the resort)
    :return: A string with information about attractions at the selected resort.
    """
    attractions_data = await get_resort('attractions_info', resort)
    return attractions_data
