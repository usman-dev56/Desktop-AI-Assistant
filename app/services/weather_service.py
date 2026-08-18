"""
Weather service.

Fetches live weather information
from OpenWeatherMap.
"""

from __future__ import annotations

import requests

from app.config import Config
from app.utils.logger import logger


class WeatherService:
    """Handles live weather information."""

    BASE_URL = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    def get_weather(self, city: str) -> str:
        """
        Get current weather for a city.

        Args:
            city: City name.

        Returns:
            Human-readable weather information.
        """

        city = city.strip()

        if not city:
            return "Please tell me the city name."

        if not Config.WEATHER_API_KEY:
            logger.error(
                "Weather API key is not configured."
            )

            return (
                "Weather service is not configured."
            )

        params = {
            "q": city,
            "appid": Config.WEATHER_API_KEY,
            "units": "metric",
        }

        try:

            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=10,
            )

            response.raise_for_status()

            data = response.json()

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            description = data["weather"][0][
                "description"
            ]

            country = data["sys"]["country"]

            logger.info(
                "Weather fetched successfully: %s, %s",
                city,
                country,
            )

            return (
                f"The weather in {city} is "
                f"{description}, with a temperature "
                f"of {temperature:.1f} degrees Celsius. "
                f"It feels like {feels_like:.1f} degrees, "
                f"with {humidity} percent humidity."
            )

        except requests.HTTPError as error:

            logger.error(
                "Weather API HTTP error: %s",
                error,
            )

            if response.status_code == 404:
                return (
                    f"I couldn't find weather information "
                    f"for {city}."
                )

            return (
                "The weather service returned an error."
            )

        except requests.RequestException as error:

            logger.error(
                "Weather API request failed: %s",
                error,
            )

            return (
                "I couldn't connect to the weather service."
            )

        except (KeyError, TypeError, ValueError) as error:

            logger.error(
                "Invalid weather API response: %s",
                error,
            )

            return (
                "I received an invalid response "
                "from the weather service."
            )

        except Exception as error:

            logger.exception(
                "Unexpected weather error: %s",
                error,
            )

            return (
                "Something went wrong while getting "
                "the weather."
            )