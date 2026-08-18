"""
Weather command.

Handles weather requests.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.weather_service import WeatherService


class WeatherCommand(BaseCommand):
    """Handles weather commands."""

    WEATHER_PREFIXES = (
        "weather",
        "temperature",
        "forecast",
    )

    def __init__(self) -> None:

        self.weather = WeatherService()

    def can_handle(self, command: str) -> bool:

        command = command.lower().strip()

        return command.startswith(
            self.WEATHER_PREFIXES
        )

    def execute(self, command: str) -> str:

        command = command.lower().strip()

        city = ""

        for prefix in self.WEATHER_PREFIXES:

            if command.startswith(prefix):

                city = command[
                    len(prefix):
                ].strip()

                break

        # Handle:
        # "weather in Lahore"
        # "temperature in Lahore"

        if city.startswith("in "):

            city = city.removeprefix(
                "in"
            ).strip()

        if not city:

            return (
                "Which city's weather would "
                "you like to know?"
            )

        return self.weather.get_weather(city)