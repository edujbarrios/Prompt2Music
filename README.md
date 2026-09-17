# Prompt2Music

Prompt2Music is an open-source web interface for turning free-form musical ideas into structured text-to-music prompts.

The project is being built with [Reflex](https://reflex.dev/) as a small, public, chat-style application written primarily in Python.

> **Project status:** early development. The Reflex baseline and backend integration are in place; the conversational UI is being added incrementally through pull requests.

## Backend

Prompt2Music is powered by [`text-to-music-prompt-structurer`](https://github.com/edujbarrios/text-to-music-prompt-structurer), an open-source Python library created and maintained by **Eduardo J. Barrios (@edujbarrios)**.

The library provides the musical analysis and prompt structuring engine used by this application. **Prompt2Music is the web interface; `text-to-music-prompt-structurer` is the backend / structuring engine.**

Prompt2Music does not duplicate the engine logic. The application uses the library directly as a Python dependency so improvements to the structuring engine remain centralized in the backend project.

The integration is intentionally thin:

```python
from text_to_music_prompt_structurer import MusicPromptEngine, format_prompt

engine = MusicPromptEngine()
prompt = engine.process(user_text)
result = format_prompt(prompt)
```

## Intended experience

The completed MVP will provide a minimal chat-like workflow:

1. Write a musical idea in natural language.
2. Submit it from the conversation composer.
3. Prompt2Music passes the text to `text-to-music-prompt-structurer`.
4. The structured result is returned as the assistant response.
5. Copy the resulting prompt or submit another idea.

No external AI provider is required for the core transformation.

## Tech stack

- Python 3.10+
- Reflex
- `text-to-music-prompt-structurer` as the structuring backend
- pytest for tests
- Ruff for linting

## Local development

The recommended workflow uses [`uv`](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/edujbarrios/Prompt2Music.git
cd Prompt2Music
uv sync --extra dev
uv run reflex run
```

The development frontend is normally available at `http://localhost:3000`.

## Project structure

```text
Prompt2Music/
├── prompt2music/
│   ├── __init__.py
│   ├── backend.py
│   └── prompt2music.py
├── tests/
├── rxconfig.py
├── pyproject.toml
├── requirements.txt
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

The codebase will stay intentionally small. Prompt parsing and musical detection belong in the backend library rather than being reimplemented here.

## Privacy direction

The MVP is designed not to persist conversations and not to send prompts to third-party AI services. Prompt transformation happens through the local Python backend library.

## Open source

Prompt2Music is open source under the **Mozilla Public License 2.0 (MPL-2.0)**.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Independence notice

Prompt2Music is an independent open-source project. It is not affiliated with, endorsed by, or connected to Suno, Udio, or any other text-to-music platform.

## Author

Created by **Eduardo J. Barrios (@edujbarrios)**.

Backend library: https://github.com/edujbarrios/text-to-music-prompt-structurer
