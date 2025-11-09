def test_authentication(page):
    page.goto("https://the-internet.herokuapp.com/login")

    username = page.locator("#username")
    passowrd = page.locator("#password")
    submit_btn = page.locator("button[type='submit']")

    valid_user = "tomsmith"
    valid_pass = "SuperSecretPassword!"

    invalid_user = "t"
    invalid_pass = "SSecretPassword!"

    login_msg = page.locator("#flash")

    # testing with invalid user-pass combination
    username.fill(invalid_user)
    passowrd.fill(invalid_pass)
    submit_btn.click()

    # Asserting the error msg
    # It will be invalid username in this case
    assert "Your username is invalid!" in login_msg.inner_text() 

    # testing with invalid pass
    username.fill(valid_user)
    passowrd.fill(invalid_pass)
    submit_btn.click()

    # Asserting the error msg
    # It will be invalid password in this case
    assert "Your password is invalid!" in login_msg.inner_text()

    # Happy path login
    username.fill(valid_user)
    passowrd.fill(valid_pass)
    submit_btn.click()

    # Asserting the success msg
    assert "You logged into a secure area!" in login_msg.inner_text()
    #assert "Secure Area" in page.locator("h2.icon-lock").inner_text()

    # Logout testing
    logout_button = page.locator("a.button.secondary.radius")
    logout_button.click()

    # Asserting the success msg
    assert "You logged out of the secure area!" in login_msg.inner_text()





