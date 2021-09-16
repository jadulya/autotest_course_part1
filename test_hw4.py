import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from functions import login, element_is_present


def test_about_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/about")
        browser.maximize_window()
        login(browser)
        browser.find_element(By.NAME, "name").send_keys("Неля")
        browser.find_element(By.NAME, "surname").send_keys("Аюпова")
        browser.find_element(By.ID, "age2").click()
        browser.find_element(By.ID, "lang1").click()
        browser.find_element(By.ID, "lang2").click()
        level = browser.find_element(By.NAME, "lvl")
        select = Select(level)
        select.select_by_visible_text("Middle")
        browser.find_element(By.NAME, "surname").send_keys(Keys.ENTER)
        assert browser.find_element(By.ID, "age1").get_attribute("checked"), "Чек бокс не включен по умолчанию"
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отсутствует"
        success_text = browser.find_element(By.CSS_SELECTOR, ".notification.is-success").text
        assert success_text == "Успех."


def test_upload_file_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        browser.maximize_window()
        login(browser)
        upload_file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
        upload_file.send_keys(os.path.join(os.getcwd(), 'resources', 'команда.jpg'))
        browser.find_element(By.CLASS_NAME, 'button').click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отсутствует"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе не пропало"

