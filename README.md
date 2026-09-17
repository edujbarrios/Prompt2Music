# Prompt2Music

Open-source web app for turning free-form musical ideas into structured text-to-music prompts.

**Website:** https://prompt2music.vercel.app

Prompt2Music is designed for **non-technical users, including people with no programming knowledge**. The web interface makes the underlying prompt-structuring engine usable without installing Python, writing code, or working from the command line.

## How it works

Prompt2Music is the **web interface**. Prompt structuring is provided by [`text-to-music-prompt-structurer`](https://github.com/edujbarrios/text-to-music-prompt-structurer), an open-source Python library created and maintained by **Eduardo J. Barrios (@edujbarrios)**.

The web app is the accessible, no-code way to use the project. Developers can use the Python library directly when they want to integrate the structuring engine into their own tools or workflows.

The app uses the library directly through `MusicPromptEngine` and `format_prompt`; it does not duplicate the parsing logic and does not require an external AI provider.

## Features

- Chat-style interface built with Reflex
- Designed for users with zero programming knowledge
- Structured music prompts from natural-language descriptions
- Copy-to-clipboard output
- Keyboard-friendly and responsive UI
- No persisted conversations in the MVP

## Run locally

```bash
git clone https://github.com/edujbarrios/Prompt2Music.git
cd Prompt2Music
uv sync --extra dev
uv run reflex run
```

Quality checks:

```bash
uv run ruff check .
uv run pytest
uv run reflex compile
```

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

Prompt2Music is licensed under the **Mozilla Public License 2.0 (MPL-2.0)**.

## Project scope

Prompt2Music is an independent open-source project. It is not affiliated with or endorsed by any text-to-music platform.
