"""Prompt2Music Reflex application."""

import reflex as rx

from prompt2music.state import ChatState

BACKEND_REPOSITORY = "https://github.com/edujbarrios/text-to-music-prompt-structurer"
PROJECT_REPOSITORY = "https://github.com/edujbarrios/Prompt2Music"

EXAMPLE_PROMPTS = (
    "neo soul with piano, warm breathy female alto vocals in Spanish, nostalgic, 92 bpm",
    "dark dreamy synthwave with 808 bass and female vocals in English",
    "smooth jazz in C# minor with saxophone and piano, intimate and mysterious",
)


def header() -> rx.Component:
    """Render the compact project header."""
    return rx.hstack(
        rx.link(
            rx.heading("Prompt2Music", size="5", weight="medium"),
            href="/",
            color="inherit",
            text_decoration="none",
        ),
        rx.spacer(),
        rx.link("GitHub", href=PROJECT_REPOSITORY, is_external=True, color_scheme="gray"),
        width="100%",
        max_width="52rem",
        padding_x="1.25rem",
        padding_y="1rem",
        align="center",
    )


def intro() -> rx.Component:
    """Render the concise product introduction and example prompts."""
    return rx.vstack(
        rx.heading("Turn an idea into a music prompt.", size="7", text_align="center"),
        rx.text(
            "Describe the track you have in mind. Prompt2Music structures the musical "
            "direction using the open-source backend library created by Eduardo J. Barrios.",
            color_scheme="gray",
            size="3",
            text_align="center",
            max_width="38rem",
        ),
        rx.flex(
            *[
                rx.button(
                    example,
                    variant="soft",
                    color_scheme="gray",
                    size="1",
                    on_click=ChatState.use_example(example),
                    white_space="normal",
                    height="auto",
                    text_align="left",
                )
                for example in EXAMPLE_PROMPTS
            ],
            gap="0.5rem",
            wrap="wrap",
            justify="center",
            width="100%",
            padding_top="0.5rem",
        ),
        spacing="3",
        align="center",
        padding_top="8vh",
        padding_bottom="2rem",
    )


def message_bubble(message: dict[str, str]) -> rx.Component:
    """Render one user or assistant message."""
    is_user = message["role"] == "user"

    return rx.box(
        rx.vstack(
            rx.text(
                message["content"],
                white_space="pre-wrap",
                overflow_wrap="anywhere",
                font_family=rx.cond(is_user, "inherit", "monospace"),
                size="3",
            ),
            rx.cond(
                message["role"] == "assistant",
                rx.button(
                    "Copy",
                    variant="ghost",
                    size="1",
                    on_click=rx.set_clipboard(message["content"]),
                    align_self="flex-end",
                    aria_label="Copy structured prompt",
                ),
                rx.fragment(),
            ),
            spacing="2",
            align="stretch",
            width="100%",
        ),
        background=rx.cond(is_user, "var(--gray-3)", "var(--gray-2)"),
        border="1px solid var(--gray-5)",
        border_radius="1rem",
        padding="1rem 1.1rem",
        max_width=rx.cond(is_user, "82%", "92%"),
        align_self=rx.cond(is_user, "flex-end", "flex-start"),
    )


def conversation() -> rx.Component:
    """Render the current conversation."""
    return rx.vstack(
        rx.foreach(ChatState.messages, message_bubble),
        rx.cond(
            ChatState.processing,
            rx.hstack(
                rx.spinner(size="2"),
                rx.text("Structuring your prompt…", color_scheme="gray", size="2"),
                spacing="2",
                align="center",
                align_self="flex-start",
            ),
            rx.fragment(),
        ),
        spacing="4",
        align="stretch",
        width="100%",
    )


def composer() -> rx.Component:
    """Render the keyboard-friendly message composer."""
    return rx.form(
        rx.vstack(
            rx.text_area(
                name="prompt",
                value=ChatState.input_text,
                on_change=ChatState.set_input_text,
                placeholder="Describe the music you imagine…",
                disabled=ChatState.processing,
                enter_key_submit=~ChatState.processing,
                max_length=2000,
                rows="2",
                auto_height=True,
                resize="none",
                size="3",
                width="100%",
                min_height="4rem",
                max_height="12rem",
                aria_label="Describe the music you imagine",
            ),
            rx.hstack(
                rx.text(
                    "Enter to send · Shift+Enter for a new line · prompts are not persisted",
                    color_scheme="gray",
                    size="1",
                ),
                rx.spacer(),
                rx.button(
                    "Send",
                    type="submit",
                    disabled=ChatState.processing,
                    size="2",
                    aria_label="Structure music prompt",
                ),
                width="100%",
                align="center",
            ),
            spacing="2",
            width="100%",
        ),
        on_submit=ChatState.submit_form,
        width="100%",
        background="var(--color-panel-solid)",
        border="1px solid var(--gray-5)",
        border_radius="1rem",
        padding="0.75rem",
        box_shadow="0 8px 30px rgba(0, 0, 0, 0.06)",
    )


def footer() -> rx.Component:
    """Render backend attribution and project links."""
    return rx.flex(
        rx.text("Powered by ", color_scheme="gray", size="1"),
        rx.link(
            "text-to-music-prompt-structurer",
            href=BACKEND_REPOSITORY,
            is_external=True,
            size="1",
        ),
        rx.text(" by Eduardo J. Barrios (@edujbarrios)", color_scheme="gray", size="1"),
        wrap="wrap",
        justify="center",
        width="100%",
        padding_y="1.25rem",
    )


def index() -> rx.Component:
    """Render the Prompt2Music chat interface."""
    return rx.box(
        rx.vstack(
            header(),
            rx.vstack(
                intro(),
                conversation(),
                composer(),
                width="100%",
                max_width="48rem",
                padding_x="1.25rem",
                spacing="5",
                flex="1",
            ),
            footer(),
            min_height="100vh",
            width="100%",
            align="center",
            spacing="0",
        ),
        background="var(--gray-1)",
        color="var(--gray-12)",
        min_height="100vh",
    )


app = rx.App()
app.add_page(index, title="Prompt2Music | Structure music prompts")
