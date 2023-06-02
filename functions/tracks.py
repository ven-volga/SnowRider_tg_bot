from informations.resorts_data import get_resort


async def get_tracks_info(resort):
    tracks_data = await get_resort('tracks_info', resort)
    return tracks_data

