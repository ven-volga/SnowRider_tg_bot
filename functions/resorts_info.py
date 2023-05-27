from informations.resorts_data import get_resort


def get_resort_info(resort):
    return get_resort('resorts_info', resort)


def how_to_get(resort):
    return get_resort('how_to_get_info', resort)
