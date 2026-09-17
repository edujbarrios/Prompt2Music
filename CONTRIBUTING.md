# Contributing to Prompt2Music

Thanks for helping improve Prompt2Music.

## Development setup

Prompt2Music requires Python 3.10 or newer. The recommended workflow uses `uv`.

```bash
uv sync --extra dev
uv run reflex run
```

If you are not using `uv`, install the dependencies from `requirements.txt` and the development tools from `pyproject.toml`.

## Before opening a pull request

Run:

```bash
uv run ruff check .
uv run pytest
```

Keep pull requests focused on one clear objective and avoid unrelated refactors.

## Backend engine

Prompt2Music is a web interface. Musical analysis and prompt structuring belong in the separate `text-to-music-prompt-structurer` project maintained by Eduardo J. Barrios (@edujbarrios):

https://github.com/edujbarrios/text-to-music-prompt-structurer

Do not duplicate the engine logic in this repository. Improvements to detection or formatting should generally be contributed to the backend library instead.
