from playwright.sync_api import expect

def test_Entry_add(page):
    locator = page.locator("text=Entry Add")
    locator.click()

    modal = page.locator("#modal")
    modal.wait_for(state="visible")

    expect(modal).to_contain_text("take an action")

    