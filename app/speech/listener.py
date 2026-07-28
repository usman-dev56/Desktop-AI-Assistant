"""
Speech Recognition service.
"""

from __future__ import annotations

import speech_recognition as sr

from app.config import Config
from app.utils.logger import logger


class Listener:
    """Handles microphone input and speech recognition."""

    def __init__(self) -> None:
        """Initialize speech recognizer."""

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.recognizer.energy_threshold = Config.ENERGY_THRESHOLD
        self.recognizer.pause_threshold = Config.PAUSE_THRESHOLD
        self.recognizer.dynamic_energy_threshold = Config.DYNAMIC_ENERGY

        logger.info("Calibrating microphone...")

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1,
                )

            logger.info("Microphone calibrated successfully.")

        except Exception as error:
            logger.exception(
                "Microphone calibration failed: %s",
                error,
            )

        logger.info("Speech recognizer initialized.")

    def listen(self) -> str | None:
        """
        Listen once and return recognized text.

        Returns:
            Recognized text or None.
        """

        try:
            with self.microphone as source:

                logger.info("Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=Config.LISTEN_TIMEOUT,
                    phrase_time_limit=Config.PHRASE_TIME_LIMIT,
                )

            text = self.recognizer.recognize_google(audio)

            text = text.lower().strip()

            logger.info("Recognized: %s", text)

            return text

        except sr.WaitTimeoutError:
            logger.warning("Listening timeout.")

        except sr.UnknownValueError:
            logger.warning("Could not understand speech.")

        except sr.RequestError as error:
            logger.error(
                "Speech Recognition API Error: %s",
                error,
            )

        except KeyboardInterrupt:
            logger.info("Listener interrupted.")
            raise

        except OSError as error:
            logger.error(
                "Microphone error: %s",
                error,
            )

        except TimeoutError as error:
            logger.error(
                "Network timeout: %s",
                error,
            )

        except ConnectionError as error:
            logger.error(
                "Connection error: %s",
                error,
            )

        except Exception as error:
            logger.exception(
                "Unexpected listener error: %s",
                error,
            )

        return None