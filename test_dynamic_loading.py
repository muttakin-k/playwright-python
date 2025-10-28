def dl1(p):
    p.get_by_role("link", name="Example 1", exact=False).click()
    h4_locator = p.locator("h4")
    assert "Example 1:" in h4_locator

def dynamic_loading(page):
    locator = page.locator("text=Dynamic Loading")
    locator.click()

    # Testing the first example: Dynamic Loading 1
    dl1(page)