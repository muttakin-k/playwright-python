def test_authentication(page):
    page.goto("https://the-internet.herokuapp.com/login")

    username = page.locator("#username")
    passowrd = page.locator("#password")
    submit_btn = page.locator("button[type='submit']")

    valid_user = "tomsmith"
    valid_pass = "SuperSecretPassword!"

    invalid_user = "t"
    invalid_pass = "SSecretPassword!"

    login_error = page.locator("#flash")

    # testing with invalid user-pass combination
    username.fill(invalid_user)
    passowrd.fill(invalid_pass)
    submit_btn.click()

    # Asserting the error msg
    assert login_error.inner_text() == "Your username is invalid!"

