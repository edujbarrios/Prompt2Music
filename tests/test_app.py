from prompt2music.prompt2music import (
    BACKEND_REPOSITORY,
    PAGE_DESCRIPTION,
    PAGE_META,
    PAGE_TITLE,
    PROJECT_REPOSITORY,
    app,
    index,
)


def test_project_links_point_to_edujbarrios_repositories() -> None:
    assert BACKEND_REPOSITORY == "https://github.com/edujbarrios/text-to-music-prompt-structurer"
    assert PROJECT_REPOSITORY == "https://github.com/edujbarrios/Prompt2Music"


def test_public_page_metadata_is_defined() -> None:
    assert PAGE_TITLE.startswith("Prompt2Music")
    assert "text-to-music-prompt-structurer" in PAGE_DESCRIPTION
    assert {"name": "robots", "content": "index, follow"} in PAGE_META


def test_reflex_app_is_created() -> None:
    assert app is not None


def test_index_component_builds() -> None:
    assert index() is not None
