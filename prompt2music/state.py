"""Reflex state for the Prompt2Music conversation."""

import logging
from typing import TypedDict

import reflex as rx

from prompt2music.backend import structure_music_prompt

logger = logging.getLogger(__name__)


class ChatMessage(TypedDict):
    role: str
    content: str


class ChatState(rx.State):
    """Per-user state for the Prompt2Music chat experience."""

    input_text: str = ""
    messages: list[ChatMessage] = []  # noqa: RUF012 - Reflex state var declaration.
    processing: bool = False
    error: str = ""

    @rx.event
    def set_input_text(self, value: str) -> None:
        self.input_text = value

    @rx.event
    def clear_conversation(self) -> None:
        if self.processing:
            return
        self.input_text = ""
        self.messages = []
        self.error = ""

    @rx.event
    def submit_prompt(self):
        """Process the current composer text and append the backend response."""
        text = self.input_text.strip()
        if not text or self.processing:
            return

        self.messages.append({"role": "user", "content": text})
        self.input_text = ""
        self.processing = True
        self.error = ""
        yield

        try:
            structured = structure_music_prompt(text)
        except Exception:
            logger.exception("Prompt structuring failed")
            self.error = "We couldn't structure that prompt. Please try again."
            self.messages.append({"role": "assistant", "content": self.error})
        else:
            self.messages.append({"role": "assistant", "content": structured})
        finally:
            self.processing = False
