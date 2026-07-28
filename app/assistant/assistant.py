"""
Main Assistant class.
"""

from __future__ import annotations

from app.config import Config
from app.speech.listener import Listener
from app.speech.speaker import Speaker
from app.assistant.command_processor import CommandProcessor
from app.utils.logger import logger


class Assistant:
    """Main application coordinator."""

    def __init__(self) -> None:

        logger.info("Initializing Assistant...")

        self.listener = Listener()
        self.speaker = Speaker()
        self.processor = CommandProcessor()

        self.running = True

        logger.info("Assistant initialized successfully.")

    def run(self) -> None:
        """Main application loop."""

        self.speaker.speak(
            f"Hello. {Config.ASSISTANT_NAME} is ready."
        )

        logger.info("Assistant started.")

        try:

            while self.running:

                text = self.listener.listen()

                if not text:
                    continue

                response = self.processor.process(text)

                if response is None:
                    continue


                self.speaker.speak(response)

                if response.lower().startswith("goodbye"):
                    self.running = False

        except KeyboardInterrupt:

            logger.info("Keyboard interrupt received.")

            self.speaker.speak("Goodbye.")

        except Exception:

            logger.exception("Unexpected assistant error.")

        finally:

            self.running = False

            self.speaker.cleanup()

            logger.info("Assistant shutting down.")