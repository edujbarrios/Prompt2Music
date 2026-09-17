"""Prompt2Music Reflex application."""

import reflex as rx

BACKEND_REPOSITORY = "https://github.com/edujbarrios/text-to-music-prompt-structurer"
PROJECT_REPOSITORY = "https://github.com/edujbarrios/Prompt2Music"


def index() -> rx.Component:
    """Render the initial Prompt2Music shell."""
    return rx.center(
        rx.vstack(
            rx.heading("Prompt2Music", size="8"),
            rx.text(
                "Turn a musical idea into a structured prompt.",
                color_scheme="gray",
                size="4",
            ),
            rx.text(
                "The interactive chat experience will be added incrementally.",
                color_scheme="gray",
            ),
            rx.hstack(
                rx.link("GitHub", href=PROJECT_REPOSITORY, is_external=True),
                rx.text("·", color_scheme="gray"),
                rx.link(
                    "text-to-music-prompt-structurer",
                    href=BACKEND_REPOSITORY,
                    is_external=True,
                ),
                spacing="3",
                align="center",
            ),
            rx.text(
                "Backend / structuring engine created by Eduardo J. Barrios (@edujbarrios).",
                color_scheme="gray",
                size="2",
                text_align="center",
            ),
            spacing="5",
            align="center",
            max_width="48rem",
            padding="2rem",
        ),
        min_height="100vh",
        width="100%",
    )


app = rx.App()
app.add_page(index, title="Prompt2Music")
