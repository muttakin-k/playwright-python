import os

def test_file_download(page):
    page.goto("https://the-internet.herokuapp.com/download")

    intended_file_name = "bb.txt"
    file_locator = page.locator("text="+intended_file_name)
    file_locator.click()

    downloads_path = "C:/Users/user/Downloads/"
    assert os.path.basename(downloads_path+intended_file_name) == intended_file_name