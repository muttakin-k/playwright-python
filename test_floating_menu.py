from helper_functions import take_screenshot_context

def test_floating_menu(page):
    page.goto("https://the-internet.herokuapp.com/floating_menu")

    # Scrolling down to 1000 px and take a screenshot
    page.mouse.wheel(0, 1000)
    page.wait_for_timeout(1000)
    take_screenshot_context(page, "floating_menu_down_1000px")

    # Scrolling to the bottom of the page and taking a screenshot
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)
    take_screenshot_context(page, "floating_menu_page_bottom")

    # Scrolling up to 1000 px and take a screenshot
    page.mouse.wheel(0, -1000)
    page.wait_for_timeout(1000)
    take_screenshot_context(page, "floating_menu_up_1000px")