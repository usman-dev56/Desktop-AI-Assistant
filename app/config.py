"""
Application configuration.

Loads settings from the .env file.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Config:
    """Application configuration."""

    # ------------------------------------------------------------------
    # Assistant
    # ------------------------------------------------------------------

    ASSISTANT_NAME: str = os.getenv("ASSISTANT_NAME", "Jarvis")
    WAKE_WORD: str = os.getenv("WAKE_WORD", "jarvis").lower()

    # ------------------------------------------------------------------
    # Voice
    # ------------------------------------------------------------------

    VOICE_NAME: str = os.getenv(
        "VOICE_NAME",
        "en-US-GuyNeural",
    )

    VOICE_RATE: int = int(
        os.getenv("VOICE_RATE", "180")
    )

    VOICE_VOLUME: float = float(
        os.getenv("VOICE_VOLUME", "1.0")
    )

    # ------------------------------------------------------------------
    # Speech Recognition
    # ------------------------------------------------------------------

    ENERGY_THRESHOLD: int = int(
        os.getenv("ENERGY_THRESHOLD", "300")
    )

    DYNAMIC_ENERGY: bool = (
        os.getenv("DYNAMIC_ENERGY", "True").lower() == "true"
    )

    PAUSE_THRESHOLD: float = float(
        os.getenv("PAUSE_THRESHOLD", "0.8")
    )

    LISTEN_TIMEOUT: int = int(
        os.getenv("LISTEN_TIMEOUT", "5")
    )

    PHRASE_TIME_LIMIT: int = int(
        os.getenv("PHRASE_TIME_LIMIT", "8")
    )

    # ------------------------------------------------------------------
    # API Keys
    # ------------------------------------------------------------------

    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    NEWS_API_KEY: str | None = os.getenv("NEWS_API_KEY")
    WEATHER_API_KEY: str | None = os.getenv("WEATHER_API_KEY")

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    LOG_LEVEL: str = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )