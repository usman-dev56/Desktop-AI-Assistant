"""
Play command.

Handles natural-language music requests.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.music_service import MusicService


class PlayCommand(BaseCommand):
    """Handles music playback commands."""

    PLAY_PHRASES = (
        "play ",
        "listen to ",
        "listen ",
        "start playing ",
        "start play ",
    )

    TRAILING_WORDS = (
        "for me",
        "please",
    )

    def __init__(self) -> None:

        self.music = MusicService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a music request."""

        command = command.lower().strip()

        return command.startswith(self.PLAY_PHRASES)

    def execute(self, command: str) -> str:
        """Play the requested song."""

        command = command.lower().strip()

        query = ""

        # Find and remove the play phrase.
        for phrase in self.PLAY_PHRASES:

            if command.startswith(phrase):

                query = command[len(phrase):].strip()

                break

        # Remove unnecessary trailing words.
        for suffix in self.TRAILING_WORDS:

            if query.endswith(suffix):

                query = query[: -len(suffix)].strip()

        if not query:

            return "What would you like me to play?"

        if self.music.play(query):

            return f"Playing {query}."

        return f"Sorry, I couldn't find {query}."