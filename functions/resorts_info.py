from informations.resorts_data import get_resort


async def get_resort_info(resort: str) -> str:
    resort_data = await get_resort('resorts_info', resort)
    return resort_data


async def how_to_get(resort: str) -> str:
    road_data = await get_resort('how_to_get_info', resort)
    return road_data


async def get_tracks_info(resort: str) -> str:
    tracks_data = await get_resort('tracks_info', resort)
    return tracks_data


async def get_food_info(resort: str) -> list:
    food_data_list = await get_resort('food_info', resort)
    food_data_string = ''
    for restaurant in food_data_list:
        food_data_string += restaurant
    return food_data_string


async def get_attractions_info(resort: str) -> str:
    attractions_data = await get_resort('attractions_info', resort)
    return attractions_data
