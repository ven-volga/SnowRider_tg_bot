import requests
from bs4 import BeautifulSoup

from informations.resorts_info import get_resort


def parse_hotels(resort):
    url = get_resort('hotels_links', resort)
    src = requests.get(url).text
    soup = BeautifulSoup(src, "lxml")
    hotels, prices, guests, urls = [], [], [], []

    hotel_names = soup.find_all("div", class_="hotel-name-block")
    hotel_prices = soup.find_all("div", class_="right-info-column")
    guests_search = soup.find_all(class_="nights_guests_info")
    hotels_urls = soup.find_all(class_="hotel-description-trim")

    for hotel_name in hotel_names:
        hotels.append(hotel_name.find_next("a").text)

    for hotel_price in hotel_prices:
        prices.append(int(hotel_price.find("span").text))

    for guest_search in guests_search:
        guests.append(guest_search.text.strip())

    for hotel_url in hotels_urls:
        urls.append(str(hotel_url.find("a"))[9:-24])

    return hotels, prices, guests, urls


def recommend_hotels(resort):
    parce_info = parse_hotels(resort)
    hotels = parce_info[0]
    prices = parce_info[1]
    guests = parce_info[2]
    urls = parce_info[3]

    hotels_str = ""

    for hotel in range(len(hotels)):
        hotels_str += f"<b>{hotels[hotel]}</b>\nвартість <b>від {prices[hotel]} грн.</b> " \
                      f"({guests[hotel]})\n{urls[hotel]}\n{'-' * 40}\n"
    return hotels_str


def general_hotels_price(resort):
    price_info = parse_hotels(resort)[1]
    average_price = round(sum(price_info) / len(price_info))
    min_price = min(price_info)
    max_price = max(price_info)
    return average_price, min_price, max_price
