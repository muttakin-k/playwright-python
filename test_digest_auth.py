def test_digest_auth(login_page):
    login_page.goto("https://the-internet.herokuapp.com/digest_auth")
    content = login_page.locator("p").text_content()
    print("Page content:", content)
    assert "Congratulations" in content

