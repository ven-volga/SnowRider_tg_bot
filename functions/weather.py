from datetime import datetime
from loguru import logger
from information.weather_descriptions import weather_descriptions, weather_icons
from information.resorts_data import get_resort
import aiohttp
import os

weather_api: str = os.getenv('WEATHER_API')


@logger.catch
async def get_current_weather(resort: str, api=weather_api) -> str:
    location = await get_resort('resorts_weather', resort)

    async with aiohttp.ClientSession() as session:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=" \
              f"{location[0]}&lon={location[1]}&appid={api}&units=metric"
        async with session.get(url, ssl=False) as response:
            current_data = await response.json()

    real_temp = current_data["main"]["temp"]
    feels_temp = current_data["main"]["feels_like"]
    humidity = current_data["main"]["humidity"]
    pressure = current_data["main"]["pressure"]
    wind = current_data["wind"]["speed"]
    description = current_data["weather"][0]["description"]
    icon = current_data["weather"][0]["icon"]
    sunrise = datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M')
    day = (datetime.fromtimestamp(current_data['sys']['sunset']) - datetime.fromtimestamp(
        current_data['sys']['sunrise']))

    current_weather_info = \
        f"<b>Зараз у {resort} - " \
        f"{weather_descriptions[description] if weather_descriptions[description] else description}</b> " \
        f"{weather_icons[icon] if weather_icons[icon] else ''}\n" \
        f"Tемпература повітря: {round(real_temp)}°C\n" \
        f"<i>(по відчуттям: {round(feels_temp)}°C)</i>\n" \
        f"Швидкість вітру: {wind} м/c\nВологість повітря: {humidity}%\n" \
        f"Атмосферний тиск: {pressure} мм.рт.ст.\n" \
        f"Схід сонця: {sunrise}\n" \
        f"Захід сонця: {sunset}\n" \
        f"Тривалість дня: {day}"

    return current_weather_info


@logger.catch
async def get_future_weather(resort: str, api=weather_api) -> str:
    location = await get_resort('resorts_weather', resort)
    future_weather_info = "<b>На найближчі дні очікується:</b>\n"

    async with aiohttp.ClientSession() as session:
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat=" \
              f"{location[0]}&lon={location[1]}&appid={api}&units=metric"
        async with session.get(url, ssl=False) as response:
            future_data = await response.json()

    for i in range(len(future_data["list"])):
        if future_data['list'][i]['dt_txt'][-8:] == "12:00:00":
            future_weather_info += \
                f"<b><i>{datetime.fromtimestamp(future_data['list'][i]['dt']).strftime('%d.%m.%Y')}:</i></b>\n " \
                f"{round(future_data['list'][i]['main']['temp'])}°C | " \
                f"{weather_descriptions[future_data['list'][i]['weather'][0]['description']].capitalize()} | " \
                f"Вітер: {future_data['list'][i]['wind']['speed']} м/с\n"

    return future_weather_info
