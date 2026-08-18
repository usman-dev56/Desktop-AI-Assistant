"""
Time command.

Handles natural-language requests for the current time.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.time_service import TimeService


class TimeCommand(BaseCommand):
    """Handles time-related requests."""

    TIME_PHRASES = (
        "what time is it",
        "what's the time",
        "whats the time",
        "tell me the time",
        "tell me what time it is",
        "current time",
        "the current time",
        "know the time",
        "do you know the time",
        "time right now",
        "time now",
    )

    def __init__(self) -> None:

        self.service = TimeService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is asking for the time."""

        command = command.lower().strip()

        # Direct phrase matching
        if any(
            phrase in command
            for phrase in self.TIME_PHRASES
        ):
            return True

        # Keep support for simple command:
        # "time"
        return command in {
            "time",
            "tell time",
            "current time",
        }

    def execute(self, command: str) -> str:
        """Return the current time."""

        return self.service.get_time()