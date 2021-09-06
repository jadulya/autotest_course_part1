from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, element_is_present


def test_inputs_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/inputs")
        browser.maximize_window()
        login(browser)
        button = browser.find_element(By.NAME, "test")
        button.send_keys("Hi")
        browser.find_element(By.CSS_SELECTOR, "form > button").click()
        success_text = browser.find_element(By.CSS_SELECTOR, ".notification.is-success").text

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Вы нашли не то поле ввода"
        assert success_text == "Верно"


def test_my_pet_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        browser.maximize_window()
        login(browser)
        browser.find_element(By.NAME, "pet").send_keys("Йорк")
        browser.find_element(By.NAME, "name").send_keys("Филя")
        browser.find_element(By.NAME, "age").send_keys("4")
        browser.find_element(By.NAME, "sex").send_keys("мужской")
        browser.find_element(By.CSS_SELECTOR, ".button").click()
        success_text = browser.find_element(By.CSS_SELECTOR, ".notification.is-success").text

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отсутствует"
        assert success_text == "Успех."


def test_my_pet_page_negative():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        browser.maximize_window()
        login(browser)
        browser.find_element(By.NAME, "pet").send_keys("Йорк")
        browser.find_element(By.CSS_SELECTOR, ".button").click()
        danger_text = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger").text

        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), \
            "Уведомление об успехе отобразилось"
        assert danger_text == "Заполнены не все поля."


def test_menu_list():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw")
        browser.maximize_window()
        browser.find_element(By.ID, "login").click()
        login(browser)

        default_list = ["Поля ввода и кнопки", "Мой питомец", "О себе", "Загрузка файла", "Ожидание",
                        "Медленная загрузка", "Модальные окна", "Новая вкладка", "iframe", "Drag-and-drop"]

        menu_list = browser.find_elements(By.TAG_NAME, "li")
        menu_list_text = []
        for item in menu_list:
            menu_list_text.append(item.text)

        assert menu_list_text == default_list
