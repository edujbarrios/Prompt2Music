from prompt2music.prompt2music import (
    BACKEND_REPOSITORY,
    PROJECT_REPOSITORY,
    app,
    index,
)


def test_project_links_point_to_edujbarrios_repositories() -> None:
    assert BACKEND_REPOSITORY == "https://github.com/edujbarrios/text-to-music-prompt-structurer"
    assert PROJECT_REPOSITORY == "https://github.com/edujbarrios/Prompt2Music"


def test_reflex_app_is_created() -> None:
    assert app is not None


def test_index_component_builds() -> None:
    assert index() is not None
