"""
Browser service.
"""

from __future__ import annotations

import urllib.parse
import webbrowser

from app.core.data_manager import data_manager
from app.utils.logger import logger


class BrowserService:
    """Handles browser operations."""

    DISPLAY_NAMES = {
        "google": "Google",
        "youtube": "YouTube",
        "github": "GitHub",
        "linkedin": "LinkedIn",
        "facebook": "Facebook",
    }

    def __init__(self) -> None:
        """Initialize browser service."""

        self.websites = data_manager.load("websites.json")

        logger.info("Browser service initialized.")

    def open(self, website: str) -> tuple[bool, str | None]:
        """
        Open a website in the default browser.

        Returns:
            tuple:
                (True, Display Name) -> Success
                (False, None) -> Failed
        """

        website = website.lower().strip()

        url = self.websites.get(website)

        if url is None:
            logger.warning("Unknown website: %s", website)
            return False, None

        try:
            webbrowser.open(url)

            display_name = self.DISPLAY_NAMES.get(
                website,
                website.title(),
            )

            logger.info(
                "Opened website: %s",
                display_name,
            )

            return True, display_name

        except Exception as error:
            logger.exception(
                "Failed to open website '%s': %s",
                website,
                error,
            )

            return False, None

    def search(self, query: str) -> bool:
        """
        Search the web using Google.

        Args:
            query: Search query.

        Returns:
            True if the browser search was opened.
        """

        query = query.strip()

        if not query:
            logger.warning("Empty search query.")
            return False

        encoded_query = urllib.parse.quote_plus(query)

        url = (
            "https://www.google.com/search?q="
            f"{encoded_query}"
        )

        try:
            webbrowser.open(url)

            logger.info(
                "Web search opened for: %s",
                query,
            )

            return True

        except Exception as error:
            logger.exception(
                "Failed to perform web search: %s",
                error,
            )

            return False