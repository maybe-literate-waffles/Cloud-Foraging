import requests as rq

base_url = "https://api.open-meteo.com/v1/"


def get_weather_data():
    query = "forecast?latitude=40.8244&longitude=140.74&hourly=temperature_2m&forecast_days=1&timezone=Asia%2FTokyo"
    full_url = f"{base_url}{query}"
    response = rq.get(full_url)
    return response.json()


weather = get_weather_data()

print(f"{weather}")
