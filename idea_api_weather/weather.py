import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import timedelta
import pandas as pd


def rain_alert(rain_prob):
    if rain_prob > 60:
        return True
    else:
        return False


def get_today_weather():

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        # Ho Chi Minh city location
        "latitude": 10.823, "longitude": 106.6296,
        "hourly": ["temperature_2m", "apparent_temperature",
                   "precipitation_probability", "uv_index"],
        "timezone": "auto",
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()
    hourly_precipitation_probability = hourly.Variables(2).ValuesAsNumpy()
    hourly_uv_index = hourly.Variables(3).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    ), "temperature_2m": hourly_temperature_2m, "apparent_temperature": hourly_apparent_temperature,
        "precipitation_probability": hourly_precipitation_probability, "uv_index": hourly_uv_index}

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    hourly_dataframe['date'] = hourly_dataframe['date'] + timedelta(hours=7)
    hourly_dataframe['date_hour'] = hourly_dataframe['date'].apply(lambda x: x.hour)

    return hourly_dataframe