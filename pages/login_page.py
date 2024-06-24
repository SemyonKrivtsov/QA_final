from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.secrets import USER_LOGIN, USER_PASSWORD


class LoginPage(Base):
    """Класс включающий действия по авторизации в системе"""

    url = 'https://store77.net/'

    # Locators
    user_name = '//div[@id="login_mod"]/form/div[1]/input'
    password = '//div[@id="login_mod"]/form/div[2]/input'
    button_login = '//div[@id="login_mod"]/form/div[3]/input'
    main_word = "//div[@id='reg_log_modal_exit']/div/div/div[2]/div/div[1]/span"
    start_login_button = "/html/body/div[3]/div/div/header/div[4]/div/div[3]/a[1]"
    cashback = '//*[@id="reg_log_modal_exit"]/div/div/div[2]/div/div[2]/div[2]/p'

    def __init__(self, driver):
        super().__init__(driver)
        self.cashback_amount = 0

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_cashback(self):
        return self.driver.find_element(By.XPATH, self.cashback)

    def get_start_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_login_button)))

    # Actions
    def input_user_name(self, user_name):
        for char in user_name:
            self.get_user_name().send_keys(char)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_start_login_button(self):
        self.get_start_login_button().click()
        print("Click start login button")

    # Methods
    def authorization(self):
        """Успешная авторизация в системе"""

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_start_login_button()
        self.input_user_name(USER_LOGIN)
        self.input_password(USER_PASSWORD)
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'Пользователь')
        self.cashback_amount = int(self.get_cashback().text)
