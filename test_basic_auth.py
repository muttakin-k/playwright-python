def test_basic_auth(page):
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    content = page.locator("p").text_content()
    print("Page content:", content)
    assert "Congratulations" in content