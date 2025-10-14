def test_digest_auth(login_page):
    # Initial navigation and assertion to digest auth
    login_page.goto("https://the-internet.herokuapp.com/digest_auth")
    content = login_page.locator("p").text_content()
    print("Page content:", content)
    assert "Congratulations" in content

    # Digest auth offers statefullness, so testing that here
    login_page.go_back()
    # final navigation to digest auth and testing if we are still logged in
    login_page.goto("https://the-internet.herokuapp.com/digest_auth")
    print("Page content:", content)
    assert "proper credentials" in content
