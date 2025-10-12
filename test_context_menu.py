from conftest import take_screenshot

def test_context_menu(page):
    locator = page.locator("text=Context Menu")
    locator.click()

    hotspot_locator = page.locate("div#hot-spot")
    hotspot_locator.click(button="Right")

    take_screenshot(page, "context_menu_alert")