def test_dropdown(page):
    locator = page.locator("text=Dropdown")
    locator.click()

    # Locating all the checkboxes
    dd_locator = page.locator("#dropdown")

    # Select by value
    page.select_option("#dropdown", value = "1")

    # asserting if the value is 1
    assert dd_locator.input_value() == "1"

    # Select by label
    page.select_option("#dropdown", label = "Option 2")

    # asserting if the value is 2
    assert dd_locator.input_value() == "2"

    # Select by index
    page.select_option("#dropdown", index = 1)

    # asserting if the value is 1
    assert dd_locator.input_value() == "1"
