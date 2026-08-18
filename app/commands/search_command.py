"""
Search command.

Handles natural-language web search requests.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.browser_service import BrowserService


class SearchCommand(BaseCommand):
    """Handles web search commands."""

    SEARCH_PREFIXES = (
        "search ",
        "google ",
        "look up ",
        "lookup ",
        "find information about ",
        "search for ",
        "search about ",
        "find ",
    )

    TRAILING_WORDS = (
        "please",
        "for me",
    )

    def __init__(self) -> None:

        self.browser = BrowserService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a web search."""

        command = command.lower().strip()

        return command.startswith(
            self.SEARCH_PREFIXES
        )

    def execute(self, command: str) -> str:
        """Perform a web search."""

        command = command.lower().strip()

        query = ""

        # Identify the search prefix.
        for prefix in self.SEARCH_PREFIXES:

            if command.startswith(prefix):

                query = command[len(prefix):].strip()

                break

        # Remove unnecessary leading/trailing words.
        query = self._clean_query(query)

        if not query:

            return "What would you like me to search for?"

        if self.browser.search(query):

            return f"Searching for {query}."

        return "Sorry, I couldn't perform the search."

    @staticmethod
    def _clean_query(query: str) -> str:
        """Clean unnecessary words from the search query."""

        query = query.strip()

        # Handle "search for ..."
        if query.startswith("for "):

            query = query.removeprefix("for").strip()

        # Remove trailing polite phrases.
        for suffix in (
            "for me",
            "please",
        ):

            if query.endswith(suffix):

                query = query[
                    : -len(suffix)
                ].strip()

        return query