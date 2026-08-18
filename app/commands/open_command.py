"""
Open command.

Handles opening websites and desktop applications
using natural-language commands.
"""

from __future__ import annotations

import threading

from app.commands.base import BaseCommand
from app.services.browser_service import BrowserService
from app.services.desktop_service import DesktopService


class OpenCommand(BaseCommand):
    """Open websites or desktop applications."""

    OPEN_PHRASES = (
        "open ",
        "launch ",
        "start ",
        "run ",
    )

    TRAILING_WORDS = (
        "for me",
        "for",
        "please",
    )

    def __init__(self) -> None:
        self.browser = BrowserService()
        self.desktop = DesktopService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command represents an open request."""

        command = command.lower().strip()

        return command.startswith(self.OPEN_PHRASES)

    def execute(self, command: str) -> str:
        """Open the requested application or website."""

        command = command.lower().strip()

        target = ""

        # Remove the opening phrase.
        for phrase in self.OPEN_PHRASES:

            if command.startswith(phrase):
                target = command[len(phrase):].strip()
                break

        # Remove unnecessary trailing words.
        for suffix in self.TRAILING_WORDS:

            if target.endswith(suffix):
                target = target[: -len(suffix)].strip()

        if not target:
            return "What would you like me to open?"

        # ----------------------------------------------------------
        # Desktop application
        # ----------------------------------------------------------

        app = self.desktop.apps.get(target)

        if app:

            threading.Thread(
                target=self.desktop.open,
                args=(target,),
                daemon=True,
            ).start()

            return f"Opening {target}."

        # ----------------------------------------------------------
        # Website
        # ----------------------------------------------------------

        success, display_name = self.browser.open(target)

        if success:

            return f"Opening {display_name or target}."

        return f"I don't know how to open {target}."