import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        login_context = browser.new_context(
            http_credentials={"username":"admin",
                              "password":"admin"
                              }
        )
        yield login_context
        browser.close()

@pytest.fixture()
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()