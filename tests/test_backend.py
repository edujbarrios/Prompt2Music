import pytest

from prompt2music.backend import structure_music_prompt


def test_structure_music_prompt_uses_backend_formatter() -> None:
    result = structure_music_prompt(
        "synthwave with 808, dark and dreamy, female vocals in English"
    )

    assert "STYLE: Synthwave" in result
    assert "MOOD: Dark, Dreamy" in result
    assert "INSTRUMENTS: 808 Bass" in result
    assert "LANGUAGE: English" in result


def test_structure_music_prompt_rejects_blank_input() -> None:
    with pytest.raises(ValueError, match="musical description"):
        structure_music_prompt("   ")
