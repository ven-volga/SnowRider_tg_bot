import os

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


async def welcome_photo(resort: str) -> str:
    photo_path = welcome_photo_path + photo_name[resort]
    return photo_path
