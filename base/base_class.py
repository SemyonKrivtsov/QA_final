import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result

    def get_screenshot(self):
        """Method Screenshot"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + ".png"
        self.driver.save_screenshot(rf'..\screen\{name_screenshot}')

