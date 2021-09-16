import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from functions import login, element_is_present, wait_until_clickable, wait_until_visible


def test_about_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/about")
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "name")).send_keys("Неля")
        wait_until_clickable(browser, (By.NAME, "surname")).send_keys("Аюпова")
        wait_until_clickable(browser, (By.ID, "age2")).click()
        wait_until_clickable(browser, (By.ID, "lang1")).click()
        wait_until_clickable(browser, (By.ID, "lang2")).click()
        level = wait_until_visible(browser, (By.NAME, "lvl"))
        select = Select(level)
        select.select_by_visible_text("Middle")  # вот тут тоже надо же ожидание?
        wait_until_clickable(browser, (By.NAME, "surname")).send_keys(Keys.ENTER)
        assert wait_until_visible(browser, (By.ID, "age1")).get_attribute("checked"), "Чек бокс не включен по умолчанию"
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отсутствует"
        success_text = wait_until_visible(browser, (By.CSS_SELECTOR, ".notification.is-success")).text
        assert success_text == "Успех."


def test_upload_file_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[type="file"]')).send_keys(os.path.join(os.getcwd(),
                                                                                      'resources', 'команда.jpg'))
        wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отсутствует"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе не пропало"
