from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_until_clickable(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_element_located(locator))


def wait_until_all_elements_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_all_elements_located(locator))


def wait_until_text_is(browser, locator, text_, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.text_to_be_present_in_element(locator, text_))


def wait_until_alert(browser, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.alert_is_present())


def wait_until_url_to_be(browser, url, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.url_to_be(url))


def wait_until_title_is(browser, title, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.title_is(title))


def login(browser):
    wait_until_clickable(browser, (By.NAME, 'email')).send_keys("qa_test@test.ru")
    wait_until_clickable(browser, (By.NAME, 'password')).send_keys("!QAZ2wsx")
    wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()


def element_is_present(browser, by, value):
    try:
        wait_until_visible(browser, (by, value))
        return True
    except TimeoutException:
        return False

