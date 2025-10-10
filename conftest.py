import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def baseUrl():
    return "https://the-internet.herokuapp.com/"

@pytest.fixture(scope="session")
def browser_context_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        login_context = browser.new_context(
            http_credentials={"username":"admin",
                              "password":"admin"
                              }
        )
        yield login_context
        browser.close()

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        browser_context = browser.new_context()
        yield browser_context
        browser.close()


@pytest.fixture()
def login_page(browser_context_login):
    page = browser_context_login.new_page()
    yield page
    page.close()

@pytest.fixture()
def page(browser_context, baseUrl):
    page = browser_context.new_page()
    page.goto(baseUrl)
    yield page
    page.close()

def take_screenshot(page, module):
    sc_path = os.path.join("screenshots", module+".png")
    page.screenshot(path=sc_path, full_page=True)
    