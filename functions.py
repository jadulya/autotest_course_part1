from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def element_is_present(browser, by, value):
    try:
        wait_until_visible(browser, (by, value))
        return True
    except TimeoutException:
        return False


def wait_until_clickable(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_element_located(locator))


def wait_until_all_elements_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_all_elements_located(locator))


def login(browser):
    wait_until_clickable(browser, (By.NAME, "email")).send_keys("qa_test@test.ru")
    wait_until_clickable(browser, (By.NAME, "password")).send_keys("!QAZ2wsx")
    wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
