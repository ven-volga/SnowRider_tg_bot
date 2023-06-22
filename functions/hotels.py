from bs4 import BeautifulSoup
from information.resorts_data import get_resort
from loguru import logger
import aiohttp


@logger.catch
async def parse_hotels(resort: str) -> tuple[list[str], list[int], list[str], list[str]]:
    hotels, prices, guests, urls = [], [], [], []
    async with aiohttp.ClientSession() as session:
        url = await get_resort('hotels_links', resort)
        async with session.get(url, ssl=False) as response:
            src = await response.text()

    soup = BeautifulSoup(src, "lxml")

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


@logger.catch
async def recommend_hotels(resort: str) -> str:
    parce_info = await parse_hotels(resort)
    hotels = parce_info[0]
    prices = parce_info[1]
    guests = parce_info[2]
    urls = parce_info[3]

    hotels_str = ''

    for hotel in range(len(hotels)):
        hotels_str += f'<b>{hotels[hotel]}</b>\nвартість <b>від {prices[hotel]} грн.</b> ' \
                      f'({guests[hotel]})\n{urls[hotel]}\n{"-" * 40}\n'
    return hotels_str


@logger.catch
async def general_hotels_price(resort: str) -> tuple[int, int, int]:
    price_data = await parse_hotels(resort)
    price_info = price_data[1]
    average_price = round(sum(price_info) / len(price_info))
    min_price = min(price_info)
    max_price = max(price_info)
    return average_price, min_price, max_price
