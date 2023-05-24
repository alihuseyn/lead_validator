import re

from selenium import webdriver

from .utils import warning


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")


def _append_url_protocol(url: str) -> str:
    return url if url.startswith("https://") or url.startswith("http://") else f"https://{url}"


def is_valid_shopify_website(driver: webdriver.Chrome, url: str) -> bool:
    try:
        driver.get(_append_url_protocol(url))
    except BaseException:
        warning("URL can be dead: ", url)
    else:
        try:
            result = driver.execute_script("return Shopify;")
        except BaseException:
            warning("It is not shopify website: ", url)
        else:
            if result is None:
                warning("It can be not a shopify website: ", url)
            else:
                if ("shop" not in result or result["shop"] is None):
                    warning("It seems not a shopify website: ", url)
                else:
                    return True

    return False


def is_valid_email(email: str) -> bool:
    return EMAIL_PATTERN.match(email) is not None
