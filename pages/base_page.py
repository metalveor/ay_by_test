from selenium.webdriver.chrome.webdriver import WebDriver  # for select annotation
from selenium.webdriver.common.by import By

by_email = (By.CSS_SELECTOR, 'a[class="i-nav-tabs__link"]')
email_field = (By.CSS_SELECTOR, 'input[type="email"]')
password_field = (By.CSS_SELECTOR, 'input[type="password"]')
enter_button = (By.CSS_SELECTOR, 'button[form="loginForm"]')
login_button = (By.CSS_SELECTOR, 'li[class="top-panel__userbar__li"]')
user_name_field = (By.CSS_SELECTOR, 'span[class="top-panel__userbar__user__name"]')
search_field = (By.CSS_SELECTOR, 'input[id="top-s"]')
find_button = (By.CSS_SELECTOR, 'button[class="top-panel__search__btn"]')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def open_page(self, page_url):
        self.driver.get(page_url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_login_button(self):
        self.find_element(login_button).click()

    def enter_login_details(self, email, password):
        self.find_element(by_email).click()
        self.find_element(email_field).send_keys(email)
        self.find_element(password_field).send_keys(password)

    def click_enter_button(self):
        self.find_element(enter_button).click()

    def login_passed(self):
        return self.find_element(user_name_field).is_displayed()

    def click_search_field(self):
        self.find_element(search_field).click()

    def enter_search_details(self, subject_of_search):
        self.find_element(search_field).send_keys(subject_of_search)

    def click_find_button(self):
        self.find_element(find_button).click()
