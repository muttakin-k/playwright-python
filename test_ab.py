def test_ab(page):
    page_header_assertion(page, "text=A/B Testing", "A/B")

def test_broken_images(page):
    page_header_assertion(page, "text=Broken Images", "Broken Images")

def page_header_assertion(page, locator_text, expected_header_text):
    locator = page.locator(locator_text)
    locator.click()
    page_header = page.locator("h3")
    header_text = page_header.text_content()
    assert expected_header_text in header_text