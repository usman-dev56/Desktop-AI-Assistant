"""
Greeting command.
"""

from __future__ import annotations

from app.commands.base import BaseCommand


class GreetingCommand(BaseCommand):
    """Handles greeting commands."""

    GREETINGS = (
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    )

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a greeting."""

        return command.strip() in self.GREETINGS

    def execute(self, command: str) -> str:
        """Return a friendly greeting."""

        return "Hello! How can I help you?"