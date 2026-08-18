"""
Screenshot command.


"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.screenshot_service import ScreenshotService


class ScreenshotCommand(BaseCommand):
    """Handles screenshot commands."""

    SCREENSHOT_PHRASES = (
        "screenshot",
        "take screenshot",
        "take a screenshot",
        "capture screen",
        "capture screenshot",
        "capture the screen",
        "capture my screen",
    )

    def __init__(self) -> None:

        self.service = ScreenshotService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a screenshot request."""

        command = command.lower().strip()

        return command.startswith(
            self.SCREENSHOT_PHRASES
        )

    def execute(self, command: str) -> str:
        """Capture and save a screenshot."""

        path = self.service.capture()

        if path:

            return "Screenshot saved successfully."

        return "Sorry, I couldn't take a screenshot."