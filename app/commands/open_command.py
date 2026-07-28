"""
Open command.

Handles opening websites and desktop applications.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.browser_service import BrowserService
from app.services.desktop_service import DesktopService


class OpenCommand(BaseCommand):
    """Open websites or desktop applications."""

    def __init__(self) -> None:

        self.browser = BrowserService()
        self.desktop = DesktopService()

    def can_handle(self, command: str) -> bool:

        return command.startswith("open ")

    def execute(self, command: str) -> str:

        target = command.removeprefix("open").strip()

        if not target:
            return "What would you like me to open?"

        # Try desktop apps first
        if self.desktop.open(target):
            return f"Opening {target}."

        # Then websites
        if self.browser.open(target):
            return f"Opening {target}."

        return f"I don't know how to open {target}."