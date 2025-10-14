
def test_context_menu(page):
    locator = page.locator("text=Context Menu")
    locator.click()

    hotspot_locator = page.locator("#hot-spot")
    hotspot_locator.click(button="right")

    # this section is not working, the dialog message is not printing
    # Will come back to this
    page.once("dialog", lambda dialog: print(dialog.message()) or dialog.accept())

