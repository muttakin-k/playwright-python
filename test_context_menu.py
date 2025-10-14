#from conftest import take_screenshot
#from helper_functions import handle_dialog

def handle_dialog(dialog):
    print(f"Alert message: {dialog.message()}")
    dialog.accept()

def test_context_menu(page):
    locator = page.locator("text=Context Menu")
    locator.click()

    hotspot_locator = page.locator("#hot-spot")
    hotspot_locator.click(button="right")

    #take_screenshot(page, "context_menu_alert")
    page.once("dialog", lambda dialog: print(dialog.message()) or dialog.accept())

