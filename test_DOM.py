from conftest import take_screenshot, write_data_to_csv

def test_challenging_dom(page):
    locator = page.locator("text=Challenging DOM")
    locator.click()

    page_header = page.locator("h3")
    assert "Challenging" in page_header.inner_html()

    buttons = page.locator(".button")
    blue_button = buttons.nth(0)
    red_button = buttons.nth(1)
    green_button = buttons.nth(2)

    blue_button.click()
    take_screenshot(page, "blue_button_clicked")

    red_button.click()
    take_screenshot(page, "red_button_clicked")

    green_button.click()
    take_screenshot(page, "green_button_clicked")

def test_table_vals(page):
    locator = page.locator("text=Challenging DOM")
    locator.click()

    table = page.locator("table")
    rows = table.locator("tbody")
    row_count = rows.count()

    data = []
    filename = "table_data.csv"

    for i in range(row_count):
        cells = rows.nth(i).locator("td")
        coll_count = cells.count()

        row_data = [cells.nth(j).inner_html() for j in range(coll_count)]

        print(f"Row {i+1}:{row_data}")
        data.append(row_data)

    write_data_to_csv(filename, data)
