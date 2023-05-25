import requests
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv, find_dotenv  # отримання api з віртуального оточення
import os

load_dotenv(find_dotenv())  # find api value

api = os.getenv('wether_api')

resorts_coordinates = {
    "Славське": [48.8473, 23.4459],
    "Драгобрат": [48.2496, 24.2496],
    "Буковель": [48.3653, 24.4004],
    "Пилипець": [48.6677, 23.3519],
    "Плай": [48.9033, 23.2928],
    "Яблуниця": [48.3054, 24.4703],
    "Красія": [48.9379, 22.7074],
    "Мигове": [48.1575, 25.379],
    "Яремче": [48.4583, 24.5519]
}


# TODO insert and script weather description dict

def get_current_weather(resort, api=api):
    location = resorts_coordinates[resort]
    current_weather_info = None

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&appid={api}&units=metric&lang=ua")
        current_data = r.json()

        real_temp = current_data["main"]["temp"]
        feels_temp = current_data["main"]["feels_like"]
        humidity = current_data["main"]["humidity"]
        pressure = current_data["main"]["pressure"]
        wind = current_data["wind"]["speed"]
        description = current_data["weather"][0]["description"].capitalize()
        sunrise = datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M:%S')
        day = (datetime.fromtimestamp(current_data['sys']['sunset']) - datetime.fromtimestamp(
            current_data['sys']['sunrise']))

        current_weather_info = f"<b>Зараз у {resort} - {description}.</b>\n" \
                               f"Tемпература повітря: {real_temp}°C\n<i>(по відчуттям: {feels_temp}°C)</i>\n" \
                               f"Швидкість вітру: {wind} м/c\nВологість повітря: {humidity}%\n" \
                               f"Атмосферний тиск: {pressure} мм.рт.ст.\n" \
                               f"Схід сонця: {sunrise}\n" \
                               f"Захід сонця: {sunset}\n" \
                               f"Тривалість дня: {day}"
    except Exception as ex:
        print(ex)
        print("Unexpected result!")

    return current_weather_info


def get_future_weather(resort, api=api):
    location = resorts_coordinates[resort]
    future_weather_info = "<b>На найближчі дні очікується:</b>\n"

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={location[0]}&lon={location[1]}&appid={api}&units=metric&lang=ua")

        future_data = r.json()
        for i in range(len(future_data["list"])):
            if future_data['list'][i]['dt_txt'][-8:] == "12:00:00":
                future_weather_info += f"{datetime.fromtimestamp(future_data['list'][i]['dt']).strftime('%d.%m')}: " \
                                       f"{round(future_data['list'][i]['main']['temp'])}°C | " \
                                       f"{future_data['list'][i]['weather'][0]['description'].capitalize()} | " \
                                       f"Вітер: {future_data['list'][i]['wind']['speed']} м/с\n"
    except Exception as ex:
        print(ex)
        print("Unexpected result!")

    return future_weather_info
