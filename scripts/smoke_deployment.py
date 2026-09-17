"""Smoke-check a running Prompt2Music deployment using only the standard library."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request


def fetch(url: str) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "Prompt2Music-Smoke/1.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check a Prompt2Music deployment")
    parser.add_argument("base_url", help="Deployment origin, e.g. https://prompt2music.vercel.app")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")

    try:
        health_status, _ = fetch(f"{base_url}/_health")
        home_status, home_body = fetch(f"{base_url}/")
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"Deployment request failed: {exc}", file=sys.stderr)
        return 1

    if health_status != 200:
        print(f"Unexpected /_health status: {health_status}", file=sys.stderr)
        return 1

    if home_status != 200:
        print(f"Unexpected / status: {home_status}", file=sys.stderr)
        return 1

    if "Prompt2Music" not in home_body:
        print("Homepage does not contain Prompt2Music branding", file=sys.stderr)
        return 1

    print(f"Prompt2Music deployment is healthy: {base_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
