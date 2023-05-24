from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@contextmanager
def get_chrome_driver():
    options = Options()
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(10)

    try:
        yield driver
    finally:
        driver.close()
