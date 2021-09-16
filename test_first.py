from webbrowser import Chrome


class TestOpen:
    def test_open_browser(self):
        with Chrome() as browser:
            browser.get("https://qastand.valhalla.pw/")
            print(f'{browser.current_url} is open')

