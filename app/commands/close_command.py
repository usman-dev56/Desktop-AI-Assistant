"""
Close command.

Handles natural-language requests to close
desktop applications.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.desktop_service import DesktopService


class CloseCommand(BaseCommand):
    """Handles closing desktop applications."""

    CLOSE_PHRASES = (
        "close ",
        "shut down ",
        "shutdown ",
        "terminate ",
        "kill ",
        "end ",
    )

    TRAILING_WORDS = (
        "for me",
        "please",
    )

    def __init__(self) -> None:

        self.desktop = DesktopService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a close request."""

        command = command.lower().strip()

        return command.startswith(self.CLOSE_PHRASES)

    def execute(self, command: str) -> str:
        """Close the requested desktop application."""

        command = command.lower().strip()

        target = ""

        # Find and remove the close phrase.
        for phrase in self.CLOSE_PHRASES:

            if command.startswith(phrase):

                target = command[len(phrase):].strip()

                break

        # Remove unnecessary trailing words.
        for suffix in self.TRAILING_WORDS:

            if target.endswith(suffix):

                target = target[: -len(suffix)].strip()

        if not target:

            return "What would you like me to close?"

        if self.desktop.close(target):

            return f"{target.capitalize()} closed."

        return f"{target.capitalize()} is not running."