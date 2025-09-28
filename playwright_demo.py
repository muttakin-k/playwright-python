from playwright.sync_api import sync_playwright

def test_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.example.com")
        print("Page Title is ----->"+page.title())
        page.click("text=More Information")
        page.screenshot(path="example.png")
        browser.close()

test_run()