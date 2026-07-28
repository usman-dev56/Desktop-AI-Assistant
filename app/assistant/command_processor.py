"""
Command Processor.

Processes spoken commands and routes them
to the appropriate command handler.
"""

from __future__ import annotations

from app.commands.router import CommandRouter
from app.utils.command_parser import CommandParser
from app.utils.logger import logger


class CommandProcessor:
    """Processes user commands."""

    def __init__(self) -> None:
        self.router = CommandRouter()

    def process(self, command: str) -> str:
        """
        Process a spoken command.

        Args:
            command: Raw command from speech recognition.

        Returns:
            Response string.
        """

        if not command:
            return "I didn't hear anything."

        # Normalize command
        command = CommandParser.normalize(command)

        logger.info("Normalized command: %s", command)

        if not command:
            return "Yes?"

        # Route command
        response = self.router.handle(command)

        logger.info("Response: %s", response)

        return response