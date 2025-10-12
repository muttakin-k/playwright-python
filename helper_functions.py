import os, csv

def take_screenshot(page, module):
    sc_path = os.path.join("screenshots", module+".png")
    page.screenshot(path=sc_path, full_page=True)

def write_data_to_csv(filename, data):
    with open(filename, "w", newline="\n") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def handle_dialog(dialog):
    pass