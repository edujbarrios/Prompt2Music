from rxconfig import resolve_deploy_url


def test_resolve_deploy_url_prefers_production_hostname() -> None:
    assert resolve_deploy_url(
        {
            "VERCEL_PROJECT_PRODUCTION_URL": "prompt2music.vercel.app",
            "VERCEL_URL": "prompt2music-git-feature.vercel.app",
        }
    ) == "https://prompt2music.vercel.app"


def test_resolve_deploy_url_uses_preview_hostname() -> None:
    assert resolve_deploy_url({"VERCEL_URL": "prompt2music-preview.vercel.app"}) == (
        "https://prompt2music-preview.vercel.app"
    )


def test_resolve_deploy_url_preserves_explicit_scheme() -> None:
    assert resolve_deploy_url({"VERCEL_URL": "https://example.com/"}) == "https://example.com"


def test_resolve_deploy_url_is_none_outside_vercel() -> None:
    assert resolve_deploy_url({}) is None
