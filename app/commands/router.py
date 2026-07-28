"""
Command router.
"""

from __future__ import annotations

from app.commands.exit_command import ExitCommand
from app.commands.time_command import TimeCommand
from app.commands.date_command import DateCommand
from app.commands.open_command import OpenCommand
from app.commands.play_command import PlayCommand
from app.commands.close_command import CloseCommand
from app.commands.window_command import WindowCommand
from app.commands.screenshot_command import ScreenshotCommand


class CommandRouter:
    """Routes commands to the correct handler."""

    def __init__(self) -> None:

        self.commands = [
            ExitCommand(),
            TimeCommand(),
            DateCommand(),
            OpenCommand(),
            PlayCommand(),
            CloseCommand(),
            WindowCommand(),
            ScreenshotCommand(),
        ]

    def handle(self, command: str) -> str:

        for handler in self.commands:

            if handler.can_handle(command):
                return handler.execute(command)

        return "Sorry, I don't understand that command."