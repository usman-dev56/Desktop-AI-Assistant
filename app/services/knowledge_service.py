"""
Knowledge service.

Handles general knowledge questions.
"""

from __future__ import annotations

import requests

from app.utils.logger import logger


class KnowledgeService:
    """Handles general knowledge questions."""

    BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def answer(self, question: str) -> str:
        """
        Answer a general knowledge question using Wikipedia.

        Args:
            question: User's question.

        Returns:
            Human-readable answer.
        """

        question = question.strip()

        if not question:
            return "What would you like to know?"

        # Remove common question prefixes.
        search_term = question

        prefixes = (
            "who is ",
            "who was ",
            "what is ",
            "what was ",
            "where is ",
            "where was ",
            "when was ",
            "when did ",
            "tell me about ",
            "explain ",
        )

        for prefix in prefixes:
            if search_term.startswith(prefix):
                search_term = search_term.removeprefix(prefix).strip()
                break

        if not search_term:
            return "Please tell me what you would like to know."

        try:
            response = requests.get(
                f"{self.BASE_URL}{search_term.replace(' ', '_')}",
                timeout=8,
                headers={
                    "User-Agent": "Jarvis-AI-Desktop-Assistant/1.0"
                },
            )

            if response.status_code == 404:
                logger.warning(
                    "Knowledge article not found: %s",
                    search_term,
                )
                return (
                    f"I couldn't find reliable information "
                    f"about {search_term}."
                )

            response.raise_for_status()

            data = response.json()

            extract = data.get("extract")

            if not extract:
                return (
                    f"I couldn't find enough information "
                    f"about {search_term}."
                )

            logger.info(
                "Knowledge answer found for: %s",
                search_term,
            )

            return extract

        except requests.RequestException as error:

            logger.error(
                "Knowledge service request failed: %s",
                error,
            )

            return (
                "I couldn't connect to the knowledge service "
                "right now."
            )

        except (KeyError, TypeError, ValueError) as error:

            logger.error(
                "Invalid knowledge service response: %s",
                error,
            )

            return (
                "I received an invalid response "
                "from the knowledge service."
            )

        except Exception as error:

            logger.exception(
                "Unexpected knowledge service error: %s",
                error,
            )

            return (
                "Something went wrong while answering "
                "your question."
            )