def test_add_remove_button(page):
    locator = page.locator("text=Add/Remove Elements")
    locator.click()

    page.wait_for_timeout(20)

    page_header = page.locator("h3")
    assert "Add/Remove" in page_header.inner_html()