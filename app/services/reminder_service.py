"""
Reminder service.

"""

from __future__ import annotations

import threading

from app.utils.logger import logger


class ReminderService:
    """Handles timed reminders."""

    def __init__(self) -> None:
        logger.info("Reminder service initialized.")

    def set_reminder(
        self,
        seconds: int,
        message: str,
        callback,
    ) -> bool:
        """
        Schedule a reminder without blocking the assistant.

        Args:
            seconds: Delay before the reminder.
            message: Reminder message.
            callback: Function called when reminder is triggered.

        Returns:
            True if reminder was scheduled successfully.
        """

        if seconds <= 0:
            return False

        if not message:
            message = "Your reminder is complete."

        thread = threading.Thread(
            target=self._wait_and_trigger,
            args=(seconds, message, callback),
            daemon=True,
        )

        thread.start()

        logger.info(
            "Reminder scheduled for %s seconds: %s",
            seconds,
            message,
        )

        return True

    def _wait_and_trigger(
        self,
        seconds: int,
        message: str,
        callback,
    ) -> None:
        """Wait and trigger the reminder."""

        try:
            threading.Event().wait(seconds)

            logger.info(
                "Reminder triggered: %s",
                message,
            )

            callback(message)

        except Exception:
            logger.exception(
                "Reminder execution failed."
            )