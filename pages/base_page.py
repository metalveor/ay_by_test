from selenium.webdriver.chrome.webdriver import WebDriver  # for select annotation
from selenium.webdriver.common.by import By
import settings
from time import sleep

by_email = (By.CSS_SELECTOR, 'a[class="i-nav-tabs__link"]')
email_field = (By.CSS_SELECTOR, 'input[type="email"]')
password_field = (By.CSS_SELECTOR, 'input[type="password"]')
enter_button = (By.CSS_SELECTOR, 'button[form="loginForm"]')
add_favor_button = (By.CSS_SELECTOR, 'div[class="b-lot-title__sub-aside"]')
login_button = (By.CSS_SELECTOR, 'li[class="top-panel__userbar__li"]')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def click_login_button(self):
        self.find_element(login_button).click()

    def enter_login_details(self, email, password):
        self.find_element(by_email).click()
        self.find_element(email_field).send_keys(email)
        self.find_element(password_field).send_keys(password)
        self.find_element(enter_button).click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def authorization(self):
        self.enter_login_details(email=settings.email, password=settings.password)
        sleep(1)  # page loading
