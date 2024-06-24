import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    # Locators
    product_1 = "//*[@id='b_step1']/div/div[1]/div/div/div[1]/div/div[2]/div/a"
    product_2 = "//*[@id='b_step1']/div/div[2]/div/div/div[1]/div/div[2]/div/a"

    price1 = "//*[@id='b_step1']/div/div[1]/div/div/div[3]/div/div"
    price2 = "//*[@id='b_step1']/div/div[2]/div/div/div[3]/div/div"

    next_button = "//*[@id='b_step1']/div/button"

    total_price = "//*[@id='b_step2']/div/div[2]/div[1]/div[2]"

    select_first_section = "/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/a"
    delete_first_product = '//*[@id="b_step1"]/div/div[1]/div/div/div[4]/a'

    def __init__(self, driver):
        super().__init__(driver)

    # Getters
    def get_product1_name(self):
        return self.driver.find_element(By.XPATH, self.product_1)

    def get_product2_name(self):
        return self.driver.find_element(By.XPATH, self.product_2)

    def get_price1_name(self):
        return self.driver.find_element(By.XPATH, self.price1)

    def get_price2_name(self):
        return self.driver.find_element(By.XPATH, self.price2)

    def get_next_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def get_total_price(self):
        return self.driver.find_element(By.XPATH, self.total_price)

    def get_first_section(self):
        return self.driver.find_element(By.XPATH, self.select_first_section)

    def get_delete_first_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_first_product)))

    # Actions
    def click_next_button_button(self):
        self.get_next_button().click()
        print("Click next button")

    def click_first_section(self):
        time.sleep(2)
        self.driver.execute_script('window.scroll(0,0)')
        # time.sleep(5)
        self.get_first_section().click()
        print("Click first section")

    def click_delete_first_product(self):
        self.get_delete_first_product().click()
        print("Click delete first product")

    # Methods
    def check_products_and_next(self, product_name1, price1, cashback, product_name2=None, price2=None):
        self.get_current_url()

        assert product_name1 == self.get_product1_name().get_attribute("innerText")
        assert price1 == int(self.get_price1_name().get_attribute("innerText").replace(" ", "")[:-1])

        cur_price = int(self.get_price1_name().get_attribute("innerText").replace(" ", "")[:-1])
        if product_name2 is not None:
            assert product_name2 == self.get_product2_name().get_attribute("innerText")
            assert price2 == int(self.get_price2_name().get_attribute("innerText").replace(" ", "")[:-1])
            cur_price += int(self.get_price2_name().get_attribute("innerText").replace(" ", "")[:-1])

        assert cur_price - cashback == int(self.get_total_price().get_attribute("innerText").replace(" ", "")[:-1])
        self.click_next_button_button()

    def clear_cart(self):
        self.click_first_section()
        while True:
            try:
                self.click_delete_first_product()
                time.sleep(5)
            except:
                break

