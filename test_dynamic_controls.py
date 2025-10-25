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
    page.get_by_role("button", name="Add").click()
    message = page.locator("#message")
    assert message.inner_text() == "It's back!"