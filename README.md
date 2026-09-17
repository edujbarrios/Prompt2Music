# Prompt2Music

Prompt2Music is an open-source web app that turns free-form musical ideas into structured text-to-music prompts.

## Backend

Prompt2Music is the **web interface**. The prompt structuring engine is [`text-to-music-prompt-structurer`](https://github.com/edujbarrios/text-to-music-prompt-structurer), an open-source Python library created and maintained by **Eduardo J. Barrios (@edujbarrios)**.

The application uses the library directly and does not duplicate its musical parsing logic:

```python
from text_to_music_prompt_structurer import MusicPromptEngine, format_prompt

engine = MusicPromptEngine()
result = format_prompt(engine.process(user_text))
```

No external AI provider is required for the core transformation.

## Features

- Chat-style interface built with Reflex
- Structured prompt generation through `text-to-music-prompt-structurer`
- Copy-to-clipboard responses
- Keyboard submission and example prompts
- Responsive and accessible UI
- No persisted conversations in the MVP

## Local development

```bash
git clone https://github.com/edujbarrios/Prompt2Music.git
cd Prompt2Music
uv sync --extra dev
uv run reflex run
```

Before opening a pull request:

```bash
uv run ruff check .
uv run pytest
uv run reflex compile
```

## Privacy

Prompt2Music does not persist conversations in the MVP and does not send prompts to third-party AI services. Prompt transformation is performed by the Python backend library.

## Open source

Prompt2Music is licensed under the **Mozilla Public License 2.0 (MPL-2.0)**.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Independence notice

Prompt2Music is an independent open-source project. It is not affiliated with, endorsed by, or connected to Suno, Udio, or any other text-to-music platform.

## Author

Created by **Eduardo J. Barrios (@edujbarrios)**.

Backend library: https://github.com/edujbarrios/text-to-music-prompt-structurer
