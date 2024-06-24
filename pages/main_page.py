import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    # Locators
    exit_button = "//div[@id='reg_log_modal_exit']"
    mobile_section = "//a[@class='kat_block block_link kat_smart_img']"
    samsung_checkbox = "//*[@id='filter_BREND']/div/div/div/div[1]/div/label/span[1]"
    google_checkbox = "//*[@id='filter_BREND']/div/div/div/div[3]/div/label/span[1]"
    select_top = "//div[@class='blocks_product_fix_w']"
    cart_button = "/html/body/div[3]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[4]/div[1]/a"
    price_product = "//p[@class='price_title_product']"
    product_name = "//h2[@class='title_card_product']"
    to_catalog_button = "//*[@id='modal_add_product']/div/div/div[3]/div/button"
    to_order_button = "//*[@id='modal_add_product']/div/div/div[3]/div/div/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.samsung_price = None
        self.samsung_phone_name = None
        self.google_price = None
        self.google_phone_name = None
        self.driver = driver

    # Getters
    def get_exit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exit_button)))

    def get_mobile_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_section)))

    def get_samsung_checkbox(self):
        return self.driver.find_element(By.XPATH, self.samsung_checkbox)

    def get_google_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.google_checkbox)))

    def get_top_mobile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_top)))

    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, self.cart_button)

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price_product)

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, self.product_name)

    def get_to_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_catalog_button)))

    def get_to_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_order_button)))

    # Actions
    def click_exit_button(self):
        self.get_exit_button().click()
        print("Click exit button")

    def click_mobile_page(self):
        self.get_mobile_page().click()
        print("Click mobile page button")

    def click_samsung_checkbox(self):
        print(self.get_samsung_checkbox().get_attribute("value"))
        self.get_samsung_checkbox().click()
        print("Click samsung checkbox button")

    def click_google_checkbox(self):
        self.get_google_checkbox().click()
        print("Click google checkbox button")

    def click_top_mobile(self):
        self.get_top_mobile().click()
        print("Click top mobile button")

    def click_cart_button(self):
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1400, 900)

        button = self.driver.find_element(By.XPATH, self.cart_button)
        button.click()
        print("Click cart button")

    def click_to_catalog(self):
        self.get_to_catalog_button().click()
        print("Click to catalog button")

    def click_to_order(self):
        self.get_to_order_button().click()
        print("Click to order button")

    # Methods
    def select_product_samsung(self):
        self.get_current_url()

        self.click_samsung_checkbox()
        time.sleep(3)
        self.click_top_mobile()
        self.samsung_price = int(self.get_price().get_attribute("innerText").replace(" ", "")[:-1])
        self.samsung_phone_name = self.get_product_name().get_attribute("innerText")

    def select_product_google(self):
        self.get_current_url()

        self.click_google_checkbox()
        time.sleep(3)
        self.click_top_mobile()
        self.google_price = int(self.get_price().get_attribute("innerText").replace(" ", "")[:-1])
        self.google_phone_name = self.get_product_name().get_attribute("innerText")
