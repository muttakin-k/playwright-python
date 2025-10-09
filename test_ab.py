def test_ab(page):
    locator = page.locator("text=A/B Testing")
    locator.click()
    page_header = page.locator("h3")
    header_text = page_header.text_content()
    assert "A/B" in header_text

def test_broken_images(page):
    locator = page.locator("text=Broken Images")
    locator.click()
    page_header = page.locator("h3")
    header_text = page_header.text_content()
    assert "Broken Images" in header_text