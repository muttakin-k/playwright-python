def test_checkboxes(page):
    locator = page.locator("text=Checkboxes")
    locator.click()

    # Locating all the checkboxes
    cb = page.locator("input[type='checkbox']")

    # There are only 2 checkboxes in this page
    cb_1 = cb.nth(0)
    cb_2 = cb.nth(1)

    # cb_1 is unchecked and cb_2 is checked at each refresh, so initially asserting that
    assert not cb_1.is_checked()
    assert cb_2.is_checked()

    cb_1.check()
    cb_2.uncheck()

    # Asserting after the changes
    assert cb_1.is_checked()
    assert not cb_2.is_checked()

    