def test_dynamic_controls(page):
    locator = page.locator("text=Dynamic Controls")
    locator.click()

    # First testing the add/remove button and asserting the correct result
    page.locator("text=Remove").click()
    message = page.locator("#message")
    assert message == "It's gone!"

    page.locator("text=Add").click()
    message = page.locator("#message")
    assert message == "It's back!"