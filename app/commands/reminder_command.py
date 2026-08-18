"""
Reminder command.

Handles timed reminder commands.
"""

from __future__ import annotations

import re

from app.commands.base import BaseCommand
from app.services.reminder_service import ReminderService
from app.speech.speaker import Speaker
from app.utils.logger import logger


class ReminderCommand(BaseCommand):
    """Handles timed reminder commands."""

    PATTERNS = (
        r"remind me in (\d+) seconds?(?: to (.+))?",
        r"remind me in (\d+) minutes?(?: to (.+))?",
        r"set a reminder in (\d+) seconds?(?: to (.+))?",
        r"set a reminder in (\d+) minutes?(?: to (.+))?",
    )

    def __init__(self, speaker: Speaker) -> None:
        self.reminder = ReminderService()
        self.speaker = speaker

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a reminder request."""

        return (
            command.startswith("remind me in ")
            or command.startswith("set a reminder in ")
        )

    def execute(self, command: str) -> str:
        """Schedule a timed reminder."""

        command = command.strip().lower()

        for pattern in self.PATTERNS:

            match = re.fullmatch(pattern, command)

            if not match:
                continue

            amount = int(match.group(1))
            message = match.group(2)

            if "minute" in pattern:
                seconds = amount * 60

                time_text = (
                    f"{amount} minute"
                    if amount == 1
                    else f"{amount} minutes"
                )

            else:
                seconds = amount

                time_text = (
                    f"{amount} second"
                    if amount == 1
                    else f"{amount} seconds"
                )

            if not message:
                message = "Your reminder is complete."

            success = self.reminder.set_reminder(
                seconds=seconds,
                message=message,
                callback=self._reminder_callback,
            )

            if success:

                logger.info(
                    "Reminder command accepted: %s",
                    command,
                )

                return (
                    f"Okay. I will remind you in "
                    f"{time_text}."
                )

            return "I couldn't set that reminder."

        return (
            "Please tell me how long the reminder "
            "should be."
        )

    def _reminder_callback(self, message: str) -> None:
        """Speak the reminder when the timer finishes."""

        logger.info(
            "Reminder alert: %s",
            message,
        )

        self.speaker.speak(
            f"Reminder. {message}"
        )