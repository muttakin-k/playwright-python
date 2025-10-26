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
    # At this time, the message is supposed to be there, so asserting
    message_locator = page.locator("#message")
    assert message_locator.count() == 1
    page.get_by_role("button", name="Add").click()
    message = page.locator("#message")
    assert message.inner_text() == "It's back!"

    # Second Phase of testing: Testing the textbox
    # The textbox should be disabled at first
    text_box = page.locator("input[type='text']")
    assert text_box.is_disabled()

    # Now clicking the button "Enable" and assert again
    page.get_by_role("button", name="Enable").click()
    page.wait_for_timeout(10000)
    text_box = page.locator("input[type='text']")
    assert text_box.is_enabled()

    disable_button = page.get_by_role("button", name="Disable")

    # Clicking the disable button and asserting
    disable_button.click()
    page.wait_for_timeout(10000)
    assert text_box.is_disabled()

