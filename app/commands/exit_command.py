"""
Exit command.
"""

from __future__ import annotations

from app.commands.base import BaseCommand


class ExitCommand(BaseCommand):
    """Handles assistant exit commands."""

    KEYWORDS = {
        "exit",
        "quit",
        "stop",
        "shutdown",
        "close program",
        "close assistant",
        "goodbye",
        "bye",
    }

    def can_handle(self, command: str) -> bool:


        return command.strip() in self.KEYWORDS

    def execute(self, command: str) -> str:

        return "Goodbye."