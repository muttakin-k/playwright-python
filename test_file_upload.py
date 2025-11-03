def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    # Locating input: choose file 
    choose_file_button = page.locator("input#file-upload")

    # Setting up file name and path in the local machine
    file_path = "C:/Users/user/Downloads/"
    file_name = "images.jpeg"
    choose_file_button.set_input_files(file_path+file_name)

    # Locating and clicking submit button
    page.locator("input#file-submit").click()

    # Changing page; locating the name div where the uploaded file name is seen
    uploaded_file_location = page.locator("div#uploaded-files")

    # Asserting that the uploaded filename div contains the filename that we have uploaded
    assert uploaded_file_location.inner_text() == file_name
