"""
Date command.

Handles natural-language requests for the current date.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.date_service import DateService


class DateCommand(BaseCommand):
    """Handles date-related requests."""

    DATE_PHRASES = (
        "what is the date",
        "what's the date",
        "whats the date",
        "tell me the date",
        "tell me today's date",
        "tell me todays date",
        "current date",
        "the current date",
        "today's date",
        "todays date",
        "what day is it",
        "what day is today",
        "which day is today",
        "today",
    )

    def __init__(self) -> None:

        self.service = DateService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is asking for the date."""

        command = command.lower().strip()

        if any(
            phrase in command
            for phrase in self.DATE_PHRASES
        ):
            return True

        return command in {
            "date",
            "today",
            "current date",
        }

    def execute(self, command: str) -> str:
        """Return the current date."""

        return self.service.get_date()