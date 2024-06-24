import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 1")
    login = LoginPage(driver)
    login.authorization()
    cashback = login.cashback_amount

    mp = MainPage(driver)
    mp.click_exit_button()
    mp.click_mobile_page()
    mp.select_product_samsung()
    mp.click_cart_button()
    mp.click_to_order()

    product1 = mp.samsung_phone_name
    price1 = mp.samsung_price

    cp = CartPage(driver)
    cp.check_products_and_next(product1, price1, cashback)

    cip = ClientInformationPage(driver)
    cip.input_inforamtion("Вася Пупкин", "99935555555", "mail@mail.ru",)

    cp.clear_cart()
    driver.quit()


def test_buy_product_2(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 2")
    login = LoginPage(driver)
    login.authorization()
    cashback = login.cashback_amount

    mp = MainPage(driver)
    mp.click_exit_button()
    mp.click_mobile_page()
    mp.select_product_google()
    mp.click_cart_button()
    mp.click_to_order()

    product1 = mp.google_phone_name
    price1 = mp.google_price

    cp = CartPage(driver)
    cp.check_products_and_next(product1, price1, cashback)

    cip = ClientInformationPage(driver)
    cip.input_inforamtion("Иван Иванов", "9997755555", "mail@mail.ru", )

    cp.clear_cart()
    driver.quit()


def test_buy_two_products(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 3")
    login = LoginPage(driver)
    login.authorization()
    cashback = login.cashback_amount

    mp = MainPage(driver)
    mp.click_exit_button()
    mp.click_mobile_page()
    mp.select_product_google()
    mp.click_cart_button()
    mp.click_to_catalog()

    driver.back()
    time.sleep(2)
    mp.click_google_checkbox()

    mp.select_product_samsung()
    mp.click_cart_button()
    mp.click_to_order()

    product1 = mp.google_phone_name
    price1 = mp.google_price

    product2 = mp.samsung_phone_name
    price2 = mp.samsung_price

    cp = CartPage(driver)
    cp.check_products_and_next(product1, price1, cashback, product_name2=product2, price2=price2)

    cip = ClientInformationPage(driver)
    cip.input_inforamtion("Вася Пупкин", "99935555555", "mail@mail.ru", )

    cp.clear_cart()
    driver.quit()
