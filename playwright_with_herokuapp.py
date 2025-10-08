from playwright.sync_api import sync_playwright

def add_remove_test(baseUrl):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(baseUrl)

        locator = page.locator("text=Add/Remove Elements")
        locator.click()
        page.wait_for_timeout(20)

        page_header = page.locator("h3")
        assert "Add/Remove" in page_header.inner_html()

        print(page_header.inner_html())

        browser.close()


if __name__ == "__main__":
    baseurl = "https://the-internet.herokuapp.com/"
    #ab_test(baseUrl=baseurl)
    # adding clicking button
    # add_remove_test(baseUrl=baseurl)
    #test_internet_login()

