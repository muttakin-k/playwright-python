def test_checkboxes(page):
    locator = page.locator("text=Checkboxes")
    locator.click()

    cb = page.locator("input[type='checkbox']")

    cb_1 = cb.nth(0)
    cb_2 = cb.nth(1)

    assert not cb_1.is_checked()
    assert cb_2.is_checked()

    cb_1.check()
    cb_2.uncheck()

    assert cb_1.is_checked()
    assert not cb_2.is_checked()

    