
import requests
from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass
class WeatherData:
    """Stores weather data."""
    main: str
    description: str
    icon: str
    temperature: float

def config_api():
    """
    Configures the API by loading the API key from the environment variables.

    Returns:
        str: The API key.
        None: If the API key is not available.
    """
    load_dotenv()
    try:
        api_key = os.getenv("API_KEY")
        if api_key is None:
            raise ValueError("API_Key is not available. Check your API_Key.")
    except Exception as e:
        print("[ERROR] -->", e)
        return None
    return api_key

def get_latitude_and_longitude(city_name, state_code, country_code, API_key):
    """
    Gets latitude and longitude coordinates for a given location.

    Args:
        city_name (str): The name of the city.
        state_code (str): The state code.
        country_code (str): The country code.
        API_key (str): The API key.

    Returns:
        tuple: A tuple containing latitude and longitude.
    """
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    data = response[0]
    latitude, longitude = data.get("lat"), data.get("lon")
    return latitude, longitude

def get_current_weather(lat, lon, API_key):
    """
    Gets the current weather data for a given latitude and longitude.

    Args:
        lat (float): The latitude.
        lon (float): The longitude.
        API_key (str): The API key.

    Returns:
        WeatherData: An object containing weather data.
    """
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    data = WeatherData(
        main=response.get("weather")[0].get("main"),
        description=response.get("weather")[0].get("description"),
        icon=response.get("weather")[0].get("icon"),
        temperature=response.get("main").get("temp")
    )
    return data

def main(city_name, state_code, country_name):
    """
    Main function to get the current weather for a given location.

    Args:
        city_name (str): The name of the city.
        state_code (str): The state code.
        country_name (str): The name of the country.

    Returns:
        WeatherData: An object containing weather data.
    """
    api_key = config_api()
    lat, lon = get_latitude_and_longitude(city_name, state_code, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data



if __name__ == "__main__":
    main()