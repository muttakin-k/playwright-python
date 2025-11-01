from playwright.sync_api import expect

def test_Entry_ad(page):
    locator = page.locator("text=Entry Ad")
    locator.click()

    # Initially the modal is visible
    modal = page.locator("#modal")
    modal.wait_for(state="visible")

    # Asserting if the modal as sample text from the actual
    expect(modal).to_contain_text("take an action")

    # Closing the modal
    modal.locator("text=Close").click()

    # At page refresh, the modal is not supposed to be visible anymore
    page.reload()
    modal = page.locator("#modal")
    expect(modal).to_be_hidden()

    # Re-enabling the modal
    page.locator("text=click here")

    # Now the modal should be visible again, so asserting that
    #page.reload()
    modal = page.locator("#modal")
    expect(modal).to_be_visible()


