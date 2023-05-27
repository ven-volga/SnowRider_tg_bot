from informations.resorts_data import get_resort


def get_train_info(resort):
    return get_resort('trains_messages', resort)


def get_train_url(resort):
    return get_resort('trains_urls', resort)
