def test_dynamic_controls(page):
    locator = page.locator("text=Dynamic Controls")
    locator.click()

    # First testing the add/remove button and asserting the correct result
    # At initial stage there will be the remove button but no text in #message
    message_locator = page.locator("#message")
    assert message_locator.count() == 0

    # Clicking the remove button for the first time
    page.get_by_role("button", name="Remove").click()
    message = page.locator("#message")
    assert message.inner_text() == "It's gone!"

    # Clicking on the add button for the first time
    # At this time, the message is supposed to be there so asserting
    message_locator = page.locator("#message")
    assert message_locator.count() == 1
    page.get_by_role("button", ).click()
    message = page.locator("#message")
    assert message.inner_text() == "It's back!"

    # Second Phase of testing: Testing the textbox
    # The textbox should be disabled at first
    text_box = page.get_by_role("input", name="Enable")
    assert text_box.is_disabled()

    # Now clicking the button "Enable" and assert again
    page.get_by_role("button", text="Enable").click()
    disable_button = page.get_by_role("button", text="Disable")
    assert text_box.is_enabled()

    # Clicking the disable button and asserting
    disable_button.click()
    assert text_box.is_disabled()

