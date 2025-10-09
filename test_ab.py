def test_ab(page):
    #print("Page Title is ----->"+page.title())

    locator = page.locator("text=A/B Testing")
    locator.click()
    page_header = page.locator("h3")
    header_text = page_header.text_content()
    assert "A/B" in header_text
    print(header_text)