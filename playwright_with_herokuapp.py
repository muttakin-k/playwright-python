from playwright.sync_api import sync_playwright

def ab_test(baseUrl):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(baseUrl)
        print("Page Title is ----->"+page.title())

        locator = page.locator("text=A/B Testing")
        locator.click()
        page_header = page.locator("h3")
        header_text = page_header.text_content()
        assert "A/B" in header_text
        print(header_text)
        #print("page header ----> " + page_header.inner_html())

        browser.close()

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

