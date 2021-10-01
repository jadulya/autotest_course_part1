from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from functions import login, element_is_present, wait_until_clickable, wait_until_visible, \
    wait_until_text_is, wait_until_alert, wait_until_url_to_be, wait_until_title_is, wait_iframe_switch_to


def test_new_window_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/new_window_button")
        browser.maximize_window()
        login(browser)
        windows = browser.window_handles
        assert len(windows) == 1
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        assert len(windows) == 2
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
        wait_until_alert(browser).accept()
        windows = browser.window_handles
        assert len(windows) == 1


def test_three_buttons_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/three_buttons")
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[onclick = "confirm_func()"]')).click()
        wait_until_alert(browser).dismiss()
        assert element_is_present(browser, By.ID, 'confirm_text'), "Не запускаем"


def test_iframe_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/iframe_page")
        browser.maximize_window()
        login(browser)
        wait_iframe_switch_to(browser, (By.ID, 'my_iframe'))
        assert element_is_present(browser, By.ID, 'photo')
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
        wait_until_alert(browser).accept()
        browser.switch_to.default_content()


def test_drag_and_drop_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/drag_and_drop_page")
        browser.maximize_window()
        login(browser)
        koala = wait_until_clickable(browser, (By.ID, "draggable"))
        rectangle = wait_until_visible(browser, (By.ID, 'droppable'))
        ActionChains(browser).drag_and_drop(koala, rectangle).perform()
        assert rectangle.text == "Успех!"
