import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")
