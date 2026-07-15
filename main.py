import requests as rq
import datetime as dt
import time as tm
import psycopg
import signal as sg
from zoneinfo import ZoneInfo

base_url = "https://api.open-meteo.com/v1/"

running = True


def handle_exit(signum, frame):
    global running
    running = False


def get_weather_data():
    query = "forecast?latitude=40.8244&longitude=140.74&current=temperature_2m&timezone=Asia%2FTokyo"
    full_url = f"{base_url}{query}"
    response = rq.get(full_url)
    return response.json()


def clean_up(weather):
    clean_weath = {}
    time = dt.datetime.now(ZoneInfo("Asia/Tokyo")).time().strftime("%H:%M:%S")

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
        "time": time,
    }

    return clean_weath


def data_func():
    weather = get_weather_data()
    clean_data = clean_up(weather)

    return clean_data


def create(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_data(
                w_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                temperature REAL,
                unit TEXT, 
                latitude REAL,
                longitude REAL,
                timezone TEXT,
                time TEXT
                );
    """)


def insert(cur, *args):
    temp, unit, lati, longi, tmzn, time = args
    cur.execute(
        t"INSERT INTO weather_data (temperature, unit, latitude, longitude, timezone, time) VALUES({temp}, {unit}, {lati}, {longi}, {tmzn}, {time});"
    )


time = 0

sg.signal(sg.SIGINT, handle_exit)

with psycopg.connect("dbname=projects user=literate-waffle") as conn:
    while running:
        clean_data = data_func()
        data_list = list(clean_data.values())

        with conn.cursor() as cur:
            create(cur)
            insert(cur, *data_list)

        conn.commit()
        tm.sleep(5)
        print("Exiting script...")
