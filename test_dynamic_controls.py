def test_dynamic_controls(page):
    locator = page.locator("text=Dynamic Controls")
    locator.click()

    # First testing the add/remove button and asserting the correct result
    page.get_by_role("button", name="Remove").click()
    message = page.locator("#message")
    assert message.inner_text() == "It's gone!"

    page.get_by_role("button", name="Add").click()
    #page.locator("text=Add").click()
    message = page.locator("#message")
    assert message.inner_text() == "It's back!"