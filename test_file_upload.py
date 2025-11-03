def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    choose_file_button = page.locator("input#file-upload")
    #choose_file_button.click()

    file_path = "C:/Users/user/Downloads/"
    file_name = "images.jpeg"
    choose_file_button.set_input_files(file_path+file_name)

    page.locator("input#file-submit").click()

    uploaded_file_location = page.locator("div#uploaded-files")
    assert uploaded_file_location.inner_text() == file_name
