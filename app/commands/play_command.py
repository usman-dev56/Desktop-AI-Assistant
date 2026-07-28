"""
Play command.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.music_service import MusicService


class PlayCommand(BaseCommand):
    """Handles play commands."""

    def __init__(self) -> None:

        self.music = MusicService()

    def can_handle(self, command: str) -> bool:

        return command.startswith("play ")

    def execute(self, command: str) -> str:

        query = command.removeprefix("play").strip()

        if not query:

            return "What would you like me to play?"

        if self.music.play(query):

            return f"Playing {query}."

        return "Sorry, I couldn't play that."