from lead_validator.driver import get_chrome_driver
from lead_validator.file import reader, writer
from lead_validator.validator import is_valid_email, is_valid_shopify_website
from lead_validator.utils import success, danger, info


if __name__ == "__main__":
    valid_count = 0
    invalid_count = 0

    data = reader("websites.txt")
    with get_chrome_driver() as driver:
        for entry in data:
            if not is_valid_shopify_website(driver, entry["url"]):
                invalid_count += 1
                writer(entry)
                danger(entry["url"] + " url is invalid")
                danger("-----")
            elif not is_valid_email(entry["email"]):
                invalid_count += 1
                writer(entry)
                danger(entry["email"] + " email is invalid")
                danger("-----")
            else:
                valid_count += 1
                success(entry["url"] + " - " + entry["email"] + " is valid")
                success("-----")

    info("In total ", str(valid_count), " seems valid shopify websites")
    info("Invalid entries found: ", str(invalid_count), " check required")
