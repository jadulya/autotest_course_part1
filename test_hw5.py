from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, element_is_present, wait_until_clickable, wait_until_visible, \
    wait_until_text_is, wait_until_alert, wait_until_url_to_be, wait_until_title_is


def test_wait_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/wait")
        browser.maximize_window()
        login(browser)
        wait_until_text_is(browser, (By.ID, 'demo'), "100")
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
        alert_text = wait_until_alert(browser).text

        assert alert_text == "Успех!"


def test_slow_load_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/slow_load')
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.CLASS_NAME, 'input')).send_keys("Hi")
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()

        assert element_is_present(browser, By.CSS_SELECTOR, '.notification.is-success'), \
            "Уведомление об успехе отсутствует"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, '.notification.is-success'), \
            "Уведомление об успехе не пропало"


def test_navigation():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/profile')
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[href = "/my_pet"]')).click()
        wait_until_url_to_be(browser, 'https://qastand.valhalla.pw/my_pet')
        browser.refresh()
        assert wait_until_title_is(browser, "Course Test Stand")

