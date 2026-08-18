"""
Window command.

Handles natural-language window management commands.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.window_service import WindowService


class WindowCommand(BaseCommand):
    """Handles window management commands."""

    ACTIONS = {
        "focus": (
            "focus ",
            "bring ",
            "activate ",
            "switch to ",
        ),
        "minimize": (
            "minimize ",
            "shrink ",
        ),
        "maximize": (
            "maximize ",
            "fullscreen ",
            "full screen ",
        ),
        "restore": (
            "restore ",
            "normal ",
        ),
    }

    TRAILING_WORDS = (
        "for me",
        "for",
        "please",
        "window",
    )

    def __init__(self) -> None:

        self.window = WindowService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a window operation."""

        command = command.lower().strip()

        for phrases in self.ACTIONS.values():

            if command.startswith(phrases):
                return True

        return False

    def execute(self, command: str) -> str:
        """Execute the requested window operation."""

        command = command.lower().strip()

        action = None
        target = ""

        # Identify the action and extract the target.
        for action_name, phrases in self.ACTIONS.items():

            for phrase in phrases:

                if command.startswith(phrase):

                    action = action_name
                    target = command[len(phrase):].strip()

                    break

            if action:
                break

        if not action:
            return "Unknown window command."

        # Remove unnecessary trailing words.
        for suffix in self.TRAILING_WORDS:

            if target.endswith(suffix):

                target = target[: -len(suffix)].strip()

        if not target:

            return f"Which window should I {action}?"

        # Execute window operation.
        match action:

            case "focus":

                success = self.window.focus(target)

            case "minimize":

                success = self.window.minimize(target)

            case "maximize":

                success = self.window.maximize(target)

            case "restore":

                success = self.window.restore(target)

            case _:

                return "Unknown window command."

        if success:

            return f"{action.capitalize()}d {target}."

        return f"I couldn't {action} {target}."