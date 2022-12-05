from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import settings
from pages.base_page import BasePage

home_page_url = 'http://ay.by/'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def authorization(driver):
    login = BasePage(driver)
    login.open_page(home_page_url)
    login.click_login_button()
    login.enter_login_details(email=settings.email, password=settings.password)
    login.click_enter_button()
    login.implicitly_wait()
    login.login_passed()
