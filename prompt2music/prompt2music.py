"""Prompt2Music Reflex application."""

import reflex as rx

from prompt2music.state import ChatState

BACKEND_REPOSITORY = "https://github.com/edujbarrios/text-to-music-prompt-structurer"
PROJECT_REPOSITORY = "https://github.com/edujbarrios/Prompt2Music"
PAGE_TITLE = "Prompt2Music | Structure music prompts"
PAGE_DESCRIPTION = (
    "Turn free-form musical ideas into structured text-to-music prompts with an open-source "
    "Reflex interface powered by text-to-music-prompt-structurer."
)

EXAMPLE_PROMPTS = (
    "neo soul with piano, warm breathy female alto vocals in Spanish, nostalgic, 92 bpm",
    "dark dreamy synthwave with 808 bass and female vocals in English",
    "smooth jazz in C# minor with saxophone and piano, intimate and mysterious",
)

PAGE_META = [
    {"name": "theme-color", "content": "#111111"},
    {"name": "robots", "content": "index, follow"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": PAGE_TITLE},
    {"property": "og:description", "content": PAGE_DESCRIPTION},
    {"name": "twitter:card", "content": "summary"},
    {"name": "twitter:title", "content": PAGE_TITLE},
    {"name": "twitter:description", "content": PAGE_DESCRIPTION},
]


def header() -> rx.Component:
    """Render the compact project header."""
    return rx.box(
        rx.hstack(
            rx.link(
                rx.heading("Prompt2Music", size="5", weight="medium"),
                href="/",
                color="inherit",
                text_decoration="none",
                aria_label="Prompt2Music home",
            ),
            rx.spacer(),
            rx.button(
                "New chat",
                variant="ghost",
                color_scheme="gray",
                size="1",
                on_click=ChatState.clear_conversation,
                disabled=ChatState.processing,
                aria_label="Clear conversation and start a new chat",
            ),
            rx.link("GitHub", href=PROJECT_REPOSITORY, is_external=True, color_scheme="gray"),
            width="100%",
            max_width="56rem",
            padding_x=["0.85rem", "1.25rem"],
            padding_y=["0.7rem", "0.9rem"],
            gap=["0.35rem", "0.75rem"],
            align="center",
            margin_x="auto",
        ),
        width="100%",
        border_bottom="1px solid var(--gray-4)",
        background="var(--gray-1)",
        position="sticky",
        top="0",
        z_index="20",
    )


def intro() -> rx.Component:
    """Render the empty-state product introduction and example prompts."""
    return rx.vstack(
        rx.text("OPEN SOURCE · NO EXTERNAL AI API", color_scheme="gray", size="1", weight="medium"),
        rx.heading(
            "Turn an idea into a music prompt.",
            size="7",
            text_align="center",
            font_size=["2.15rem", "2.8rem", "3.4rem"],
            line_height=["1.08", "1.05"],
            max_width="44rem",
        ),
        rx.text(
            "Describe the track you have in mind. Prompt2Music structures the musical "
            "direction using the open-source backend library created by Eduardo J. Barrios.",
            color_scheme="gray",
            size="3",
            text_align="center",
            max_width="38rem",
            line_height="1.6",
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
                    min_height="2.5rem",
                    width=["100%", "auto"],
                    text_align="left",
                )
                for example in EXAMPLE_PROMPTS
            ],
            gap="0.6rem",
            flex_direction=["column", "row"],
            align_items="stretch",
            justify_content=["stretch", "center"],
            flex_wrap="wrap",
            width="100%",
            max_width="46rem",
            padding_top=["0.5rem", "0.75rem"],
        ),
        spacing="3",
        align="center",
        width="100%",
        padding_top=["3.5rem", "7vh", "10vh"],
        padding_bottom=["1.25rem", "2rem"],
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
                line_height="1.6",
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
        border_radius=["0.9rem", "1rem"],
        padding=["0.85rem 0.9rem", "1rem 1.1rem"],
        max_width=rx.cond(is_user, "88%", "96%"),
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
                role="status",
                aria_live="polite",
            ),
            rx.fragment(),
        ),
        spacing="4",
        align="stretch",
        width="100%",
        flex="1",
        padding_top=rx.cond(ChatState.messages.length() == 0, "0", "1.25rem"),
        padding_bottom=["0.25rem", "0.5rem"],
        role="log",
        aria_live="polite",
        aria_label="Prompt2Music conversation",
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
                min_height=["3.75rem", "4rem"],
                max_height="12rem",
                aria_label="Describe the music you imagine",
            ),
            rx.hstack(
                rx.text(
                    "Enter to send · Shift+Enter for a new line · prompts are not persisted",
                    color_scheme="gray",
                    size="1",
                    line_height="1.35",
                    flex="1",
                    min_width="0",
                ),
                rx.button(
                    "Send",
                    type="submit",
                    disabled=ChatState.processing,
                    size="2",
                    min_width="4.75rem",
                    aria_label="Structure music prompt",
                ),
                width="100%",
                gap="0.75rem",
                align="center",
            ),
            spacing="2",
            width="100%",
        ),
        on_submit=ChatState.submit_form,
        width="100%",
        background="var(--color-panel-solid)",
        border="1px solid var(--gray-5)",
        border_radius=["1rem 1rem 0 0", "1rem"],
        padding=["0.65rem 0.65rem max(0.65rem, env(safe-area-inset-bottom))", "0.75rem"],
        box_shadow="0 8px 30px rgba(0, 0, 0, 0.06)",
        position="sticky",
        bottom=["0", "1rem"],
        z_index="10",
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
        padding_x="1rem",
        padding_y=["1rem", "1.25rem"],
        text_align="center",
    )


def index() -> rx.Component:
    """Render the Prompt2Music chat interface."""
    return rx.box(
        rx.vstack(
            header(),
            rx.vstack(
                rx.cond(ChatState.messages.length() == 0, intro(), rx.fragment()),
                conversation(),
                composer(),
                width="100%",
                max_width="52rem",
                padding_x=["0.75rem", "1.25rem"],
                spacing="4",
                flex="1",
                align="stretch",
            ),
            footer(),
            min_height="100dvh",
            width="100%",
            align="center",
            spacing="0",
        ),
        background="var(--gray-1)",
        color="var(--gray-12)",
        min_height="100dvh",
    )


app = rx.App()
app.add_page(
    index,
    title=PAGE_TITLE,
    description=PAGE_DESCRIPTION,
    image="/favicon.svg",
    meta=PAGE_META,
)
