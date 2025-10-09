def test_add_remove_button(page):
    locator = page.locator("text=Add/Remove Elements")
    locator.click()

    page.wait_for_timeout(20)

    page_header = page.locator("h3")
    assert "Add/Remove" in page_header.inner_html()

    add_button = page.locator("text=Add Element")
    # clicking the add button 5 times
    for _ in range(5):
        add_button.click()

    # Finding all the delete buttons
    delete_buttons = page.locator("button.added-manually")
    count = delete_buttons.count()
    assert count == 5
