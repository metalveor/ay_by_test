from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import settings

# login_button = (By.CSS_SELECTOR, 'li[class="top-panel__userbar__li"]')
# by_email = (By.CSS_SELECTOR, 'a[class="i-nav-tabs__link"]')
# email_field = (By.CSS_SELECTOR, 'input[type="email"]')
# password_field = (By.CSS_SELECTOR, 'input[type="password"]')
# enter_button = (By.CSS_SELECTOR, 'button[form="loginForm"]')
# add_favor_button = (By.CSS_SELECTOR, 'div[class="b-lot-title__sub-aside"]')


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('user-data-dir=test_dir')
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()

#
# @pytest.fixture(scope='function')
# def login(driver):
#     driver.find_element(login_button).click()
#     driver.find_element(by_email).click()
#     driver.find_element(email_field).send_keys(settings.email)
#     driver.find_element(password_field).send_keys(settings.password)
#     driver.find_element(enter_button).click()
