def test_drag_drop(page):
    locator = page.locator("text=Drag and Drop")
    locator.click()

    source = page.locator("#column-a")
    dest = page.locator("#column-b")

    source.drag_to(dest)

    header_a = page.locator("#column-a header").inner_text()
    header_b = page.locator("#column-b header").inner_text()

    print("\n")

    print(f"After drag: A={header_a}, B={header_b}")
    assert header_a == "B" and header_b == "A"

    source = page.locator("#column-b")
    dest = page.locator("#column-a")

    source.drag_to(dest)

    header_a = page.locator("#column-a header").inner_text()
    header_b = page.locator("#column-b header").inner_text()

    print("\n")

    print(f"After drag: A={header_a}, B={header_b}")
    assert header_a == "A" and header_b == "B"