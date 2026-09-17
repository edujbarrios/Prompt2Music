"""Reflex configuration with deployment-aware Vercel defaults."""

from __future__ import annotations

import os
from collections.abc import Mapping

import reflex as rx


def resolve_deploy_url(env: Mapping[str, str] | None = None) -> str | None:
    """Return the public Vercel origin when running in a Vercel deployment."""
    environment = os.environ if env is None else env
    hostname = environment.get("VERCEL_PROJECT_PRODUCTION_URL") or environment.get("VERCEL_URL")
    if not hostname:
        return None
    if hostname.startswith(("http://", "https://")):
        return hostname.rstrip("/")
    return f"https://{hostname.rstrip('/')}"


deploy_url = resolve_deploy_url()

config = rx.Config(
    app_name="prompt2music",
    **({"deploy_url": deploy_url} if deploy_url else {}),
)
