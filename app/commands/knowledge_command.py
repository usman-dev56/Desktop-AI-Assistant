"""
Knowledge command.

Handles general knowledge questions.
"""

from __future__ import annotations

from app.commands.base import BaseCommand
from app.services.knowledge_service import KnowledgeService


class KnowledgeCommand(BaseCommand):
    """Handles general knowledge questions."""

    QUESTION_PREFIXES = (
        "who ",
        "what ",
        "where ",
        "when ",
        "why ",
        "how ",
        "tell me about ",
        "explain ",
    )

    def __init__(self) -> None:
        self.knowledge = KnowledgeService()

    def can_handle(self, command: str) -> bool:
        """Check whether the command is a knowledge question."""

        return command.startswith(self.QUESTION_PREFIXES)

    def execute(self, command: str) -> str:
        """Answer the knowledge question."""

        return self.knowledge.answer(command)