
import requests
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather information for a given city."""

    # Step 1: Find city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(
        geo_url,
        params=geo_params,
        timeout=10
    )

    geo_response.raise_for_status()
    geo_data = geo_response.json()
    print(geo_data)

    if not geo_data.get("results"):
        return f"Could not find the city: {city}"

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 2: Fetch current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

    weather_response.raise_for_status()
    weather_data = weather_response.json()

    current = weather_data["current"]

    # Step 3: Return formatted weather information
    return (
        f"Weather in {location['name']}: "
        f"Temperature: {current['temperature_2m']}°C, "
        f"Feels like: {current['apparent_temperature']}°C, "
        f"Humidity: {current['relative_humidity_2m']}%, "
        f"Wind speed: {current['wind_speed_10m']} km/h"
    )


# Test the tool
if __name__ == "__main__":
    result = get_weather.invoke({"city":"Bengaluru"})
    print(result)
