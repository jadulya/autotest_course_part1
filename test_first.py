from selenium import webdriver


class TestOpen:
    def test_open_browser(self):
        browser = webdriver.Chrome()
        browser.get('https://qastand.valhalla.pw/')
        print(f'{browser.current_url} is open')
        browser.quit()
