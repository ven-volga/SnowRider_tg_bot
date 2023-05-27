import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os
from informations.resorts_data import get_resort

load_dotenv(find_dotenv())  # find api value

api = os.getenv('WEATHER_API')


# TODO insert and script weather description dict

def get_current_weather(resort, api=api):
    location = get_resort('resorts_weather', resort)
    current_weather_info = None

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat="
            f"{location[0]}&lon={location[1]}&appid={api}&units=metric&lang=ua")
        current_data = r.json()

        real_temp = current_data["main"]["temp"]
        feels_temp = current_data["main"]["feels_like"]
        humidity = current_data["main"]["humidity"]
        pressure = current_data["main"]["pressure"]
        wind = current_data["wind"]["speed"]
        description = current_data["weather"][0]["description"].capitalize()
        sunrise = datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M')
        day = (datetime.fromtimestamp(current_data['sys']['sunset']) - datetime.fromtimestamp(
            current_data['sys']['sunrise']))

        current_weather_info = f"<b>Зараз у {resort} - {description}.</b>\n" \
                               f"Tемпература повітря: {round(real_temp)}°C\n" \
                               f"<i>(по відчуттям: {round(feels_temp)}°C)</i>\n" \
                               f"Швидкість вітру: {wind} м/c\nВологість повітря: {humidity}%\n" \
                               f"Атмосферний тиск: {pressure} мм.рт.ст.\n" \
                               f"Схід сонця: {sunrise}\n" \
                               f"Захід сонця: {sunset}\n" \
                               f"Тривалість дня: {day}"
    except Exception as e:
        print(e)
        print("Unexpected result! (Weather app)")

    return current_weather_info


def get_future_weather(resort, api=api):
    location = get_resort('resorts_weather', resort)
    future_weather_info = "<b>На найближчі дні очікується:</b>\n"

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat="
            f"{location[0]}&lon={location[1]}&appid={api}&units=metric&lang=ua")

        future_data = r.json()
        for i in range(len(future_data["list"])):
            if future_data['list'][i]['dt_txt'][-8:] == "12:00:00":
                future_weather_info += f"{datetime.fromtimestamp(future_data['list'][i]['dt']).strftime('%d.%m')}: " \
                                       f"{round(future_data['list'][i]['main']['temp'])}°C | " \
                                       f"{future_data['list'][i]['weather'][0]['description'].capitalize()} | " \
                                       f"Вітер: {future_data['list'][i]['wind']['speed']} м/с\n"
    except Exception as e:
        print(e)
        print("Unexpected result! (Weather app)")

    return future_weather_info
