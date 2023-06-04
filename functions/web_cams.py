from informations.resorts_data import get_resort


async def get_webcam_url(resort):
    webcam_url = await get_resort('web-cams', resort)
    return webcam_url

