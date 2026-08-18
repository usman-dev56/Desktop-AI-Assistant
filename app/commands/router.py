"""
Command router.
"""

from __future__ import annotations

from app.commands.exit_command import ExitCommand
from app.commands.greeting_command import GreetingCommand
from app.commands.time_command import TimeCommand
from app.commands.date_command import DateCommand
from app.commands.search_command import SearchCommand
from app.commands.open_command import OpenCommand
from app.commands.play_command import PlayCommand
from app.commands.close_command import CloseCommand
from app.commands.window_command import WindowCommand
from app.commands.screenshot_command import ScreenshotCommand
from app.commands.weather_command import WeatherCommand


class CommandRouter:
    """Routes normalized commands to command handlers."""

    def __init__(self) -> None:

        self.commands = [
            ExitCommand(),
            GreetingCommand(),
            TimeCommand(),
            DateCommand(),
            SearchCommand(),
            OpenCommand(),
            PlayCommand(),
            CloseCommand(),
            WindowCommand(),
            ScreenshotCommand(),
            WeatherCommand(),
        ]

    def handle(self, command: str) -> str:
        """Find and execute the appropriate command."""

        for handler in self.commands:

            if handler.can_handle(command):
                return handler.execute(command)

        return "Sorry, I don't understand that command."