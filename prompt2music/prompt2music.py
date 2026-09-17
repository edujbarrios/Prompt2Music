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


def brand() -> rx.Component:
    """Render the compact Prompt2Music brand mark."""
    return rx.hstack(
        rx.center(
            rx.icon("audio-lines", size=17),
            width="2rem",
            height="2rem",
            border_radius="0.65rem",
            background="var(--gray-12)",
            color="var(--gray-1)",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.heading("Prompt2Music", size="4", weight="medium", line_height="1"),
            rx.text(
                "Music prompt structurer",
                size="1",
                color_scheme="gray",
                display=["none", "block"],
                line_height="1.1",
            ),
            spacing="1",
            align="start",
        ),
        spacing="2",
        align="center",
    )


def header() -> rx.Component:
    """Render the compact project header."""
    return rx.box(
        rx.hstack(
            rx.link(
                brand(),
                href="/",
                color="inherit",
                text_decoration="none",
                aria_label="Prompt2Music home",
            ),
            rx.spacer(),
            rx.button(
                rx.icon("plus", size=14),
                rx.text("New chat", display=["none", "block"]),
                variant="ghost",
                color_scheme="gray",
                size="1",
                on_click=ChatState.clear_conversation,
                disabled=ChatState.processing,
                aria_label="Clear conversation and start a new chat",
            ),
            rx.link(
                rx.hstack(
                    rx.icon("github", size=15),
                    rx.text("GitHub", display=["none", "block"]),
                    spacing="1",
                    align="center",
                ),
                href=PROJECT_REPOSITORY,
                is_external=True,
                color_scheme="gray",
                text_decoration="none",
                padding="0.35rem 0.5rem",
                border_radius="0.55rem",
                aria_label="Open Prompt2Music on GitHub",
                _hover={"background": "var(--gray-3)"},
            ),
            width="100%",
            max_width="58rem",
            padding_x=["0.8rem", "1.25rem"],
            padding_y=["0.65rem", "0.8rem"],
            gap=["0.25rem", "0.5rem"],
            align="center",
            margin_x="auto",
        ),
        width="100%",
        border_bottom="1px solid rgba(0, 0, 0, 0.06)",
        background="rgba(250, 250, 250, 0.86)",
        backdrop_filter="blur(18px) saturate(1.2)",
        position="sticky",
        top="0",
        z_index="20",
    )


def intro() -> rx.Component:
    """Render the empty-state product introduction and example prompts."""
    return rx.vstack(
        rx.hstack(
            rx.badge("Open source", variant="soft", color_scheme="gray", radius="full"),
            rx.badge("No coding required", variant="soft", color_scheme="gray", radius="full"),
            spacing="2",
            justify="center",
            flex_wrap="wrap",
        ),
        rx.heading(
            "Turn a musical idea into a structured prompt.",
            size="8",
            text_align="center",
            font_size=["2.2rem", "3rem", "3.8rem"],
            line_height=["1.08", "1.04"],
            letter_spacing="-0.035em",
            max_width="48rem",
            weight="medium",
        ),
        rx.text(
            "Describe the track you imagine in plain language. Prompt2Music turns it into a "
            "clear, structured music prompt using the open-source engine by Eduardo J. Barrios.",
            color_scheme="gray",
            size="3",
            text_align="center",
            max_width="40rem",
            line_height="1.65",
        ),
        rx.vstack(
            rx.text(
                "Try an example",
                color_scheme="gray",
                size="1",
                weight="medium",
                letter_spacing="0.04em",
                text_transform="uppercase",
            ),
            rx.flex(
                *[
                    rx.button(
                        rx.icon("sparkles", size=14),
                        example,
                        variant="soft",
                        color_scheme="gray",
                        size="1",
                        on_click=ChatState.use_example(example),
                        white_space="normal",
                        height="auto",
                        min_height="2.8rem",
                        width=["100%", "auto"],
                        text_align="left",
                        justify_content="flex-start",
                        cursor="pointer",
                        padding="0.65rem 0.8rem",
                        border="1px solid var(--gray-4)",
                        background="rgba(255, 255, 255, 0.72)",
                        style={
                            "transition": "transform 140ms ease, box-shadow 140ms ease, border-color 140ms ease",
                            "_hover": {
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 8px 22px rgba(0, 0, 0, 0.07)",
                                "border_color": "var(--gray-6)",
                            },
                        },
                    )
                    for example in EXAMPLE_PROMPTS
                ],
                gap="0.65rem",
                flex_direction=["column", "row"],
                align_items="stretch",
                justify_content=["stretch", "center"],
                flex_wrap="wrap",
                width="100%",
                max_width="50rem",
            ),
            spacing="2",
            align="center",
            width="100%",
            padding_top="0.75rem",
        ),
        spacing="4",
        align="center",
        width="100%",
        padding_top=["3.5rem", "8vh", "11vh"],
        padding_bottom=["1.5rem", "2.5rem"],
    )


def message_bubble(message: dict[str, str]) -> rx.Component:
    """Render one user or assistant message."""
    is_user = message["role"] == "user"

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.center(
                    rx.icon(rx.cond(is_user, "user", "audio-lines"), size=12),
                    width="1.45rem",
                    height="1.45rem",
                    border_radius="0.45rem",
                    background=rx.cond(is_user, "var(--gray-5)", "var(--gray-12)"),
                    color=rx.cond(is_user, "var(--gray-12)", "var(--gray-1)"),
                    flex_shrink="0",
                ),
                rx.text(
                    rx.cond(is_user, "You", "Prompt2Music"),
                    color_scheme="gray",
                    size="1",
                    weight="medium",
                    letter_spacing="0.03em",
                ),
                spacing="2",
                align="center",
            ),
            rx.text(
                message["content"],
                white_space="pre-wrap",
                overflow_wrap="anywhere",
                font_family=rx.cond(is_user, "inherit", "monospace"),
                size="3",
                line_height="1.65",
                width="100%",
            ),
            rx.cond(
                message["role"] == "assistant",
                rx.button(
                    rx.icon("copy", size=14),
                    "Copy",
                    variant="ghost",
                    color_scheme="gray",
                    size="1",
                    on_click=[
                        rx.set_clipboard(message["content"]),
                        rx.toast.success("Structured prompt copied"),
                    ],
                    align_self="flex-end",
                    aria_label="Copy structured prompt",
                ),
                rx.fragment(),
            ),
            spacing="3",
            align="stretch",
            width="100%",
        ),
        background=rx.cond(is_user, "rgba(238, 238, 238, 0.82)", "rgba(255, 255, 255, 0.9)"),
        border="1px solid var(--gray-5)",
        border_radius=["1rem", "1.15rem"],
        padding=["0.9rem", "1.05rem 1.15rem"],
        box_shadow=rx.cond(is_user, "none", "0 8px 28px rgba(0, 0, 0, 0.045)"),
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
                padding="0.3rem 0.2rem",
                role="status",
                aria_live="polite",
            ),
            rx.fragment(),
        ),
        spacing="4",
        align="stretch",
        width="100%",
        flex="1",
        padding_top=rx.cond(ChatState.messages.length() == 0, "0", "1.5rem"),
        padding_bottom=["0.4rem", "0.75rem"],
        role="log",
        aria_live="polite",
        aria_label="Prompt2Music conversation",
    )


def composer() -> rx.Component:
    """Render the keyboard-friendly message composer."""
    input_is_empty = ChatState.input_text == ""

    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.icon("music", size=14, color="var(--gray-9)"),
                rx.text("Describe your track", size="1", weight="medium", color_scheme="gray"),
                spacing="2",
                align="center",
                width="100%",
            ),
            rx.text_area(
                name="prompt",
                value=ChatState.input_text,
                on_change=ChatState.set_input_text,
                placeholder="Genre, mood, vocals, instruments, BPM, language…",
                disabled=ChatState.processing,
                enter_key_submit=~ChatState.processing,
                max_length=2000,
                rows="2",
                auto_height=True,
                resize="none",
                size="3",
                width="100%",
                min_height=["4rem", "4.4rem"],
                max_height="12rem",
                aria_label="Describe the music you imagine",
                background="var(--gray-2)",
            ),
            rx.hstack(
                rx.box(
                    rx.text(
                        "Not persisted · no external AI API",
                        color_scheme="gray",
                        size="1",
                        line_height="1.35",
                        display=["block", "block", "none"],
                    ),
                    rx.text(
                        "Enter to send · Shift+Enter for a new line · prompts are not persisted",
                        color_scheme="gray",
                        size="1",
                        line_height="1.35",
                        display=["none", "none", "block"],
                    ),
                    flex="1",
                    min_width="0",
                ),
                rx.button(
                    rx.cond(
                        ChatState.processing,
                        rx.fragment(),
                        rx.icon("arrow-up", size=15),
                    ),
                    "Send",
                    type="submit",
                    disabled=ChatState.processing | input_is_empty,
                    loading=ChatState.processing,
                    size="2",
                    min_width="5.3rem",
                    radius="full",
                    high_contrast=True,
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
        background="rgba(255, 255, 255, 0.93)",
        backdrop_filter="blur(14px)",
        border="1px solid var(--gray-5)",
        border_radius=["1rem 1rem 0 0", "1.15rem"],
        padding=["0.7rem 0.7rem max(0.7rem, env(safe-area-inset-bottom))", "0.85rem"],
        box_shadow="0 16px 46px rgba(0, 0, 0, 0.09)",
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
        padding_y=["1.1rem", "1.5rem"],
        text_align="center",
        opacity="0.82",
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
                max_width="54rem",
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
        background=(
            "radial-gradient(circle at 50% 8%, rgba(255,255,255,0.98) 0%, "
            "rgba(247,247,247,0.94) 34%, var(--gray-1) 68%)"
        ),
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
