from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInformationPage(Base):
    next_to_payment = '//*[@id="b_step2"]/div/button'
    payment_button = '//*[@id="b_step3"]/div/button'
    name_field = '//*[@id="b_step2"]/div/div[1]/div/div/div/div/div[1]/input'
    phone_field = '//*[@id="b_step2"]/div/div[1]/div/div/div/div/div[2]/input'
    email_field = '//*[@id="b_step2"]/div/div[1]/div/div/div/div/div[3]/input'

    def __init__(self, driver):
        super().__init__(driver)

    # Getters
    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_next_to_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_to_payment)))

    def get_payment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_button)))

    # Actions
    def click_next_to_button(self):
        self.get_next_to_payment().click()
        print("Click next to payment button")

    def click_payment_button(self):
        self.get_payment_button().click()
        print("Click payment button")

    # Methods
    def input_inforamtion(self, name, phone, email):
        self.get_current_url()

        self.get_name_field().clear()
        self.get_name_field().send_keys(name)

        self.get_email_field().clear()
        self.get_email_field().send_keys(email)

        self.get_phone_field().clear()
        for digit in phone:
            self.get_phone_field().send_keys(digit)

        self.click_next_to_button()
        self.click_payment_button()
