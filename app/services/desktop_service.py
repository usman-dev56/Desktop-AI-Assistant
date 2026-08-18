"""
Desktop service.

Handles desktop applications.
"""

from __future__ import annotations

import subprocess

import psutil

from app.core.data_manager import data_manager
from app.utils.logger import logger


class DesktopService:
    """Desktop application service."""

    def __init__(self) -> None:
        self.apps = data_manager.load("apps.json")

        logger.info("Desktop service initialized.")

    def open(self, app_name: str) -> bool:
        """
        Open desktop application.
        """

        app_name = app_name.lower().strip()

        app = self.apps.get(app_name)

        if not app:
            logger.warning(
                "Unknown application: %s",
                app_name,
            )
            return False

        try:
            subprocess.Popen(app["open"])

            logger.info(
                "Opened application: %s",
                app_name,
            )

            return True

        except Exception:
            logger.exception(
                "Failed to open %s",
                app_name,
            )

            return False

    def close(self, app_name: str) -> bool:
        """
        Close desktop application.

        Returns:
            True if the application was found and closed.
            False if the application was not running.
        """

        app_name = app_name.lower().strip()

        app = self.apps.get(app_name)

        if not app:
            logger.warning(
                "Unknown application: %s",
                app_name,
            )
            return False

        process_name = app["process"].lower()

        closed = False

        for process in psutil.process_iter(
            ["pid", "name"]
        ):

            try:
                name = process.info["name"]

                if not name:
                    continue

                if name.lower() == process_name:

                    process.terminate()

                    try:
                        process.wait(timeout=3)

                    except psutil.TimeoutExpired:
                        process.kill()

                    closed = True

                    logger.info(
                        "Closed application: %s",
                        app_name,
                    )

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
            ):
                continue

        if not closed:

            logger.warning(
                "%s is not running.",
                app_name,
            )

        return closed