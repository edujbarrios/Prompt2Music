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
    def use_example(self, value: str) -> None:
        if not self.processing:
            self.input_text = value

    @rx.event
    def clear_conversation(self) -> None:
        if self.processing:
            return
        self.input_text = ""
        self.messages = []
        self.error = ""

    def _submit_current_prompt(self):
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

    @rx.event
    def submit_prompt(self):
        """Submit from non-form UI controls."""
        yield from self._submit_current_prompt()

    @rx.event
    def submit_form(self, _form_data: dict[str, str]):
        """Submit from the composer form (Enter or submit button)."""
        yield from self._submit_current_prompt()
