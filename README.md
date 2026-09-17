# Prompt2Music

Prompt2Music is an open-source web interface for turning free-form musical ideas into structured text-to-music prompts.

The project is built with [Reflex](https://reflex.dev/) as a small, public, chat-style application written primarily in Python.

> **Project status:** MVP. The chat flow, backend integration, copy action, keyboard submission, examples, public metadata, tests, CI, and production container setup are in place.

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

## How it works

1. Write a musical idea in natural language.
2. Press **Enter** or use the **Send** button. Use **Shift+Enter** for a new line.
3. Prompt2Music passes the text to `text-to-music-prompt-structurer`.
4. The backend returns the structured result through `format_prompt()`.
5. The result appears as the assistant message and can be copied directly.
6. Submit another idea to continue the conversation.

Example input:

```text
neo soul with piano, warm breathy female alto vocals in Spanish, nostalgic, 92 bpm
```

No external AI provider is required for the core transformation.

## Tech stack

- Python 3.10+
- Reflex
- `text-to-music-prompt-structurer` as the structuring backend
- pytest for tests
- Ruff for linting
- GitHub Actions for CI
- Caddy + Redis in the optional production container

## Local development

The recommended workflow uses [`uv`](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/edujbarrios/Prompt2Music.git
cd Prompt2Music
uv sync --extra dev
uv run reflex run
```

The development frontend is normally available at `http://localhost:3000`.

Before opening a pull request:

```bash
uv run ruff check .
uv run pytest
uv run reflex compile
```

## Production

Reflex can run the application directly in production mode:

```bash
reflex run --env prod
```

Prompt2Music also includes a production `Dockerfile` based on Reflex's single-container deployment pattern. The container builds the optimized frontend, serves static assets through Caddy, and proxies Reflex backend routes to the Python service.

Build the image:

```bash
docker build -t prompt2music .
```

Run it locally on port `8080`:

```bash
docker run --rm -p 8080:8080 prompt2music
```

For a platform that expects another port, pass the build argument:

```bash
docker build --build-arg PORT=10000 -t prompt2music .
docker run --rm -p 10000:10000 prompt2music
```

When a deployment serves the frontend and backend from the same HTTPS origin, no external API URL is required. If they are hosted separately, build with an explicit `API_URL`:

```bash
docker build \
  --build-arg API_URL=https://api.example.com \
  -t prompt2music .
```

The app remains provider agnostic. It can also be deployed through Reflex Cloud using the standard `reflex deploy` workflow.

## Project structure

```text
Prompt2Music/
├── .github/
│   └── workflows/
│       └── ci.yml
├── assets/
│   ├── favicon.svg
│   └── robots.txt
├── prompt2music/
│   ├── __init__.py
│   ├── backend.py
│   ├── prompt2music.py
│   └── state.py
├── tests/
├── Caddyfile
├── Dockerfile
├── rxconfig.py
├── pyproject.toml
├── requirements.txt
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

The codebase stays intentionally small. Prompt parsing and musical detection belong in the backend library rather than being reimplemented here.

## Privacy

Prompt2Music does not persist conversations in the MVP and does not send prompts to third-party AI services. Prompt transformation happens through the Python backend library.

## Open source

Prompt2Music is open source under the **Mozilla Public License 2.0 (MPL-2.0)**.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Independence notice

Prompt2Music is an independent open-source project. It is not affiliated with, endorsed by, or connected to Suno, Udio, or any other text-to-music platform.

## Author

Created by **Eduardo J. Barrios (@edujbarrios)**.

Backend library: https://github.com/edujbarrios/text-to-music-prompt-structurer
