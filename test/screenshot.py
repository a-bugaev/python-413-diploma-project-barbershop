"""
take screenshot from each template on each bootstrap breakpoint
"""

import os
import re
import selenium.webdriver as driver
import selenium.common.exceptions as selenium_exceptions
from selenium.webdriver.common.by import By

def get_saving_path():
    """
    get absolute path to screenshots dir in project root
    """
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    project_root = os.path.dirname(this_dir)
    return project_root + "/screenshots"


SCREENSHOTS_PATH = get_saving_path()
FIREFOX_OPTIONS = driver.firefox.options.Options()
FIREFOX_OPTIONS.add_argument("--headless")
VIEWPORT_WIDTHS = [1400, 1200, 992, 768, 576]
URLS = [
    "http://localhost:9000/",
    "http://localhost:9000/orders",
    "http://localhost:9000/orders/1",
    "http://localhost:9000/thanks",
]
DRIVER = driver.Firefox(options=FIREFOX_OPTIONS)

def main():
    """
    Takes VIEWPORT_WIDTHS x URLS screenshots
    """
    for url in URLS:
        for width in VIEWPORT_WIDTHS:
            DRIVER.get(url)
            DRIVER.set_window_size(width, 1080)

            btn = DRIVER.find_element(By.ID, "djHideToolBarButton")
            DRIVER.execute_script("arguments[0].classList.add('djdt-hidden')", btn)

            toolbar = DRIVER.find_element(By.ID, "djDebugToolbar")
            DRIVER.execute_script("arguments[0].classList.add('djdt-hidden')", toolbar)

            last_part = re.sub(r"^(.*)/([^$]*)$", r"\2", url)
            if re.search(r"^\d+$", last_part):
                raw_path = re.sub(r"^.*/(([^/]*)/([^$]*))$", r"\1", url).replace("/","_")
            else:
                raw_path = last_part

            if len(raw_path) == 0:
                template_name = "landing"
            else:
                template_name = raw_path

            filename = template_name+"-"+str(width)+".png"

            DRIVER.save_full_page_screenshot(f"{SCREENSHOTS_PATH}/{filename}")
            print(f"Saved screenshot: \n{SCREENSHOTS_PATH}/{filename}")


if __name__ == "__main__":
    try:
        main()
    except selenium_exceptions.WebDriverException as e:
        print(str(e))
