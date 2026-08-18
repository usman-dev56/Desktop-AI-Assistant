"""
Command parser.

Normalizes spoken commands.
"""

from __future__ import annotations

import re


class CommandParser:
    """Normalizes voice commands."""

    WAKE_WORDS = {
        "jarvis",
        "hey",
        "hello",
        "ok",
    }

    FILLER_WORDS = {
        "the",
        "a",
        "an",
        "please",
        "could",
        "would",
        "can",
        "you",
        "my",
    }

    ALIASES = {
        # Open
        "launch": "open",
        "start": "open",
        "run": "open",

        # Close
        "terminate": "close",
        "kill": "close",
        "end": "close",

        # Window
        "bring": "focus",
        "activate": "focus",
        "switch": "focus",

        "shrink": "minimize",

        "fullscreen": "maximize",
        "full screen": "maximize",

        "normal": "restore",

        # Screenshot
        "screen shot": "screenshot",
        "take screen shot": "take screenshot",
        "capture": "capture screen",

        # Music
        "listen to": "play",
        "listen": "play",

        # Applications
        "note": "notepad",
        "calc": "calculator",
        "paint": "mspaint",

        "vs code": "vscode",
        "visual studio code": "vscode",

        "chrome browser": "chrome",
    }

    @classmethod
    def normalize(cls, command: str) -> str:
    

        command = command.lower().strip()

        # Remove punctuation
        command = re.sub(r"[.,!?]", "", command)

        # Preserve standalone greetings
        if command in {
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        }:
            return command

        words: list[str] = []

        for word in command.split():

            if word in cls.WAKE_WORDS:
                continue

            if word in cls.FILLER_WORDS:
                continue

            words.append(word)

        command = " ".join(words)

        aliases = sorted(
            cls.ALIASES.items(),
            key=lambda item: len(item[0]),
            reverse=True,
        )

        for old, new in aliases:

            pattern = rf"\b{re.escape(old)}\b"

            command = re.sub(
                pattern,
                new,
                command,
            )

        return command.strip()