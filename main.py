import requests as rq
import datetime as dt
import time as tm

base_url = "https://api.open-meteo.com/v1/"


def get_weather_data():
    query = "forecast?latitude=40.8244&longitude=140.74&current=temperature_2m&timezone=Asia%2FTokyo"
    full_url = f"{base_url}{query}"
    response = rq.get(full_url)
    return response.json()


def clean_up(weather):
    clean_weath = {}

    temp = weather["current"]["temperature_2m"]
    temp_unit = weather["current_units"]["temperature_2m"]
    lat_cor = weather["latitude"]
    long_cor = weather["longitude"]
    time_zone = weather["timezone_abbreviation"]

    clean_weath = {
        "temperature": temp,
        "unit": temp_unit,
        "latitude": lat_cor,
        "longitude": long_cor,
        "timezone": time_zone,
    }

    return clean_weath


def data_func():
    weather = get_weather_data()
    clean_data = clean_up(weather)

    return clean_data


time = 0

while True:
    clean_data = data_func()
    time = dt.datetime.now().time().strftime("%H:%M:%S")
    tm.sleep(5)
    print(f"{clean_data} and time: {time}")
