import os
from loguru import logger

welcome_photo_path = os.getenv('WELCOME_PHOTO_PATH')

photo_name = {
            'Славське': 'slavske.jpeg',
            'Драгобрат': 'dragobrat.jpeg',
            'Буковель': 'bukovel.jpeg',
            'Пилипець': 'pylypec.jpeg',
            'Плай': 'play.jpeg',
            'Яблуниця': 'yablunitca.jpeg',
            'Красія': 'krasiya.jpeg',
            'Мигове': 'migove.jpeg',
            'Яремче': 'yaremche.jpeg',
}


@logger.catch
async def welcome_photo(resort: str) -> str:
    """
    Forms the path to the welcome photo of the resort.

    :param resort: The name of the resort from the client's request
                   (used as a dictionary key to get the photo name)
    :return: The absolute path to the resort photo.
    """
    photo_path = welcome_photo_path + photo_name[resort]
    return photo_path
