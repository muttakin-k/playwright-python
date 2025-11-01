from playwright.sync_api import expect

def test_Entry_ad(page):
    locator = page.locator("text=Entry Ad")
    locator.click()

    modal = page.locator("#modal")
    modal.wait_for(state="visible")

    expect(modal).to_contain_text("take an action")

    modal.locator("text=Close").click()

    page.reload()

    modal = page.locator("#modal")
    expect(modal).to_be_hidden()

    #modal.wait_for(state="close")

