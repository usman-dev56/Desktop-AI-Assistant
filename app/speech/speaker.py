"""
Text-to-Speech service.

Uses Microsoft Edge Neural Voices.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

import edge_tts
import pygame

from app.config import Config
from app.utils.logger import logger


class Speaker:
    """Handles text-to-speech."""

    def __init__(self) -> None:

        self.voice = Config.VOICE_NAME
        self.volume = Config.VOICE_VOLUME

        # Temp directory
        self.temp_dir = (
            Path(__file__).resolve().parent.parent.parent
            / "temp"
        )

        self.temp_dir.mkdir(exist_ok=True)

        self.audio_file = (
            self.temp_dir / "speech.mp3"
        )

        try:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(
                self.volume
            )

            logger.info(
                "Speaker initialized (%s).",
                self.voice,
            )

        except Exception:
            logger.exception(
                "Failed to initialize pygame mixer."
            )

    async def _generate_audio(
        self,
        text: str,
    ) -> None:
        """
        Generate speech audio.
        """

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
        )

        await communicate.save(
            str(self.audio_file)
        )

    def speak(self, text: str) -> None:
        """
        Convert text to speech.
        """

        if not text:
            return

        logger.info(
            "Speaking: %s",
            text,
        )

        try:

            # Stop previous playback
            self.stop()

            # Remove old file
            if self.audio_file.exists():
                self.audio_file.unlink()

            # Generate audio
            asyncio.run(
                self._generate_audio(text)
            )

            # Play audio
            pygame.mixer.music.load(
                str(self.audio_file)
            )

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(20)

        except Exception:
            logger.exception(
                "Speech synthesis failed."
            )

    def stop(self) -> None:
        """
        Stop current playback.
        """

        try:

            if pygame.mixer.get_init():

                pygame.mixer.music.stop()

                pygame.mixer.music.unload()

        except Exception:
            pass

    def set_volume(
        self,
        volume: float,
    ) -> None:
        """
        Set playback volume.
        """

        self.volume = max(
            0.0,
            min(1.0, volume),
        )

        if pygame.mixer.get_init():

            pygame.mixer.music.set_volume(
                self.volume
            )

    def cleanup(self) -> None:
        """
        Cleanup resources.
        """

        try:

            self.stop()

            if self.audio_file.exists():

                self.audio_file.unlink()

            if pygame.mixer.get_init():

                pygame.mixer.quit()

            logger.info(
                "Speaker cleaned up."
            )

        except Exception:
            logger.exception(
                "Cleanup failed."
            )