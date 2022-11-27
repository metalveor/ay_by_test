from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('user-data-dir=F:/Lessons/ay_by_test/tests/test_dir')
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


# @pytest.fixture(scope='function')
# def authorization(driver: WebDriver):
#     if driver.find_element(By.CSS_SELECTOR, 'from selenium.webdriver.common.by import By').is_displayed():
#         pass
    # else:
    #     BasePage.open_page()