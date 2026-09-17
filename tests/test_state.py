from prompt2music.state import ChatState


def test_chat_state_exposes_expected_vars_and_events() -> None:
    assert ChatState.input_text is not None
    assert ChatState.messages is not None
    assert ChatState.processing is not None
    assert ChatState.set_input_text is not None
    assert ChatState.submit_prompt is not None
    assert ChatState.clear_conversation is not None
