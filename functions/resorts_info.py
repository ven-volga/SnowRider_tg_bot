from informations.resorts_data import get_resort


async def get_resort_info(resort):
    resort_data = await get_resort('resorts_info', resort)
    return resort_data


async def how_to_get(resort):
    road_data = await get_resort('how_to_get_info', resort)
    return road_data


async def get_tracks_info(resort):
    tracks_data = await get_resort('tracks_info', resort)
    return tracks_data
