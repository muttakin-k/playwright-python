from helper_functions import take_screenshot

def test_disappearing_items(page):
    locator = page.locator("text=Disappearing Elements")
    locator.click()

    take_screenshot(page, "Disappearing Elements")