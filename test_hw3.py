from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, element_is_present, wait_until_clickable, wait_until_visible,\
    wait_until_all_elements_visible


def test_inputs_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/inputs")
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "test")).send_keys("Hi")
        wait_until_clickable(browser, (By.CSS_SELECTOR, "form > button")).click()

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Вы нашли не то поле ввода"
        success_text = wait_until_visible(browser, (By.CSS_SELECTOR, ".notification.is-success")).text
        assert success_text == "Верно"


def test_my_pet_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/my_pet')
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, 'pet')).send_keys("Йорк")
        wait_until_clickable(browser, (By.NAME, 'name')).send_keys("Филя")
        wait_until_clickable(browser, (By.NAME, 'age')).send_keys("4")
        wait_until_clickable(browser, (By.NAME, 'sex')).send_keys("мужской")
        wait_until_clickable(browser, (By.CSS_SELECTOR, '.button')).click()

        assert element_is_present(browser, By.CSS_SELECTOR, '.notification.is-success'), \
            "Уведомление об успехе отсутствует"
        success_text = wait_until_visible(browser, (By.CSS_SELECTOR, '.notification.is-success')).text
        assert success_text == "Успех."


def test_my_pet_page_negative():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/my_pet')
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, 'pet')).send_keys("Йорк")
        wait_until_clickable(browser, (By.CSS_SELECTOR, '.button')).click()

        assert not element_is_present(browser, By.CSS_SELECTOR, '.notification.is-success'), \
            "Уведомление об успехе отобразилось"
        assert element_is_present(browser, By.CSS_SELECTOR, '.notification.is-danger')
        danger_text = wait_until_visible(browser, (By.CSS_SELECTOR, '.notification.is-danger')).text
        assert danger_text == "Заполнены не все поля."


def test_menu_list():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw')
        browser.maximize_window()
        wait_until_clickable(browser, (By.ID, 'login')).click()
        login(browser)

        DEFAULT_LIST = ["Поля ввода и кнопки", "Мой питомец", "О себе", "Загрузка файла", "Ожидание",
                        "Медленная загрузка", "Модальные окна", "Новая вкладка", "iframe", "Drag-and-drop"]

        menu_list = wait_until_all_elements_visible(browser, (By.TAG_NAME, 'li'))
        menu_list_text = []
        for item in menu_list:
            menu_list_text.append(item.text)

        assert menu_list_text == DEFAULT_LIST, "Строки меню не соответсвуют ожиданию"

