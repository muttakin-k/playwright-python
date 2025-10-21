from helper_functions import take_screenshot

def test_dynamic_content(page):
    dc_url = "https://the-internet.herokuapp.com/dynamic_content"
    page.goto(dc_url)

    take_screenshot(page, "dc_before_refresh")

    enable_static = "?with_content=static"
    page.goto(dc_url+enable_static)

    take_screenshot(page, "dc_after_refresh")