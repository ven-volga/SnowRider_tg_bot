from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

from data_and_metrics.weather_descriptions import weather_descriptions, weather_icons
from informations.resorts_data import get_resort
import aiohttp

load_dotenv(find_dotenv())  # find api value
api = os.getenv('WEATHER_API')


async def get_current_weather(resort, api=api):
    location = await get_resort('resorts_weather', resort)
    current_weather_info = None

    try:
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

    except Exception as e:
        print(e)
        print("Unexpected result! (Current weather app)")

    return current_weather_info


async def get_future_weather(resort, api=api):
    location = await get_resort('resorts_weather', resort)
    future_weather_info = "<b>На найближчі дні очікується:</b>\n"

    try:
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

    except Exception as e:
        print(e)
        print("Unexpected result! (Future weather app)")

    return future_weather_info
