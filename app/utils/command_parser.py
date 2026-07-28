"""
Command parser.

Normalizes spoken commands.
"""

from __future__ import annotations


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
        "me",
        "my",
        "to",
    }

    ALIASES = {

        # ---------------------------
        # Open
        # ---------------------------
        "launch": "open",
        "start": "open",
        "run": "open",

        # ---------------------------
        # Close
        # ---------------------------
        "terminate": "close",
        "kill": "close",
        "end": "close",

        # ---------------------------
        # Window
        # ---------------------------
        "bring": "focus",
        "activate": "focus",
        "switch": "focus",

        "shrink": "minimize",

        "fullscreen": "maximize",
        "full screen": "maximize",

        "normal": "restore",

        # ---------------------------
        # Screenshot
        # ---------------------------
        "screen shot": "screenshot",
        "take screen shot": "take screenshot",
        "capture": "capture screen",

        # ---------------------------
        # Music
        # ---------------------------
        "listen": "play",
        "listen to": "play",

        # ---------------------------
        # Applications
        # ---------------------------
        "note": "notepad",
        "calc": "calculator",
        "paint": "mspaint",

        "vs": "vscode",
        "vs code": "vscode",
        "visual studio code": "vscode",

        "chrome browser": "chrome",
    }

    @classmethod
    def normalize(cls, command: str) -> str:
        """
        Normalize a spoken command.

        Example:
            "Hey Jarvis, please open the Google"
            ->
            "open google"
        """

        command = command.lower().strip()

        words: list[str] = []

        for word in command.split():

            word = word.strip(".,!?")

            if word in cls.WAKE_WORDS:
                continue

            if word in cls.FILLER_WORDS:
                continue

            words.append(word)

        command = " ".join(words)

        # Apply aliases
        for old, new in cls.ALIASES.items():
            command = command.replace(old, new)

        return command.strip()