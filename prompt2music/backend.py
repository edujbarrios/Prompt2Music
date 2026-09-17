"""Adapter around the text-to-music prompt structuring backend."""

from text_to_music_prompt_structurer import MusicPromptEngine, format_prompt

_ENGINE = MusicPromptEngine()


def structure_music_prompt(text: str) -> str:
    """Turn free-form musical text into the backend's formatted prompt output."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("A musical description is required.")

    prompt = _ENGINE.process(cleaned)
    return format_prompt(prompt)
