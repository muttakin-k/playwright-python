from helper_functions import take_screenshot

def test_dynamic_content(page):
    locator = page.locator("text=Dynamic Content")
    locator.click()

    dc_url = "https://the-internet.herokuapp.com/dynamic_content"
    #page.goto(dc_url)

    take_screenshot(page, "dc_before_refresh")

    enable_static = "?with_content=static"
    page.goto(dc_url+enable_static)

    # this is a dummy line

    take_screenshot(page, "dc_after_refresh")