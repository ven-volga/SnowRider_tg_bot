welcome_photo_path = {
            'Славське': './data_and_metrics/welcome_photos/slavske.jpeg',
            'Драгобрат': './data_and_metrics/welcome_photos/dragobrat.jpeg',
            'Буковель': './data_and_metrics/welcome_photos/bukovel.jpeg',
            'Пилипець': './data_and_metrics/welcome_photos/pylypec.jpeg',
            'Плай': './data_and_metrics/welcome_photos/play.jpeg',
            'Яблуниця': './data_and_metrics/welcome_photos/yablunitca.jpeg',
            'Красія': './data_and_metrics/welcome_photos/krasiya.jpeg',
            'Мигове': './data_and_metrics/welcome_photos/migove.jpeg',
            'Яремче': './data_and_metrics/welcome_photos/yaremche.jpeg',
}


async def welcome_photo(resort: str) -> str:
    photo_path = welcome_photo_path[resort]
    return photo_path
