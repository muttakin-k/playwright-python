from conftest import take_screenshot

def test_challenging_dom(page):
    locator = page.locator("text=Challenging DOM")
    locator.click()

    page_header = page.locator("h3")
    assert "Challenging" in page_header.inner_html()

    blue_button = page.locator("button.button")
    red_button = page.locator("button.button.alert")
    green_button = page.locator("button.button.success")

    blue_button.click()
    take_screenshot(page, "blue_button_clicked")

    red_button.click()
    take_screenshot(page, "red_button_clicked")

    green_button.click()
    take_screenshot(page, "green_button_clicked")

