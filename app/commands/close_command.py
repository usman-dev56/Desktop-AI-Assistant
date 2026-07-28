"""
Close command.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.desktop_service import DesktopService


class CloseCommand(BaseCommand):
    """Close desktop applications."""

    def __init__(self) -> None:

        self.desktop = DesktopService()

    def can_handle(self, command: str) -> bool:

        return command.startswith("close ")

    def execute(self, command: str) -> str:

        target = command.removeprefix(
            "close"
        ).strip()

        if not target:

            return (
                "What would you like me to close?"
            )

        if self.desktop.close(target):

            return f"Closing {target}."

        return (
            f"{target.capitalize()} is not running."
        )