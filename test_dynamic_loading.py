def dl1(p):
    p.get_by_role("link", name="Example 1", exact=False).click()
    h4_locator = p.locator("h4").nth(0)
    assert "Example 1:" in h4_locator.inner_html()

def dl2(p):
    p.get_by_role("link", name="Example 2", exact=False).click()
    h4_locator = p.locator("h4").nth(0)
    assert "Example 1:" not in h4_locator.inner_html()

def test_dynamic_loading(page):
    locator = page.locator("text=Dynamic Loading")
    locator.click()

    # Testing the first example: Dynamic Loading 1
    #dl1(page)

    # Testing the first example: Dynamic Loading 2
    dl2(page)