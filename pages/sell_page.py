from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
import os

sell_page_url = 'http://ay.by/sell/'
home_page_url = 'http://ay.by/'

drag_button = (By.CSS_SELECTOR, 'a[id="framedrag"]')
drag_to = (By.CSS_SELECTOR, 'div[style="height: 57px"]')
attach_button = (By.CSS_SELECTOR, 'input[type="file"]')
file_img = (By.CSS_SELECTOR, 'img[class="fileup_img"]')
submit_button = (By.CSS_SELECTOR, 'span[id="submit_button"]')
alert_message = (By.CSS_SELECTOR, 'th[id="message-error-all-id"]')
lot_name_field = (By.CSS_SELECTOR, 'input[class="lotaddform-maintitle__ip up-border"]')
choose_section = (By.CSS_SELECTOR, 'a[onclick="return show_choose_cat();"]')
collect_section = (By.CSS_SELECTOR, 'a[rel="1101586"]')
second_section = (By.CSS_SELECTOR, 'a[rel="1101688"]')
continent_section = (By.CSS_SELECTOR, 'a[rel="1102278"]')
country_section = (By.CSS_SELECTOR, 'a[rel="1102283"]')
year_section = (By.CSS_SELECTOR, 'a[rel="1105815"]')
condition = (By.CSS_SELECTOR, 'select[rel="condition"]')

class SellPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_sell_page(self):
        self.open_page(sell_page_url)
        self.authorization()
        sleep(1)  # page loading
        self.open_page(sell_page_url)

    # def click_drag_button(self, driver):
    #     ActionChains(driver).drag_and_drop(drag_button, drag_to)

    def attach_file(self):
        self.find_elements(attach_button)[1].send_keys(os.path.join(os.path.dirname(__file__), 'my_lot.jpg'))
        sleep(1)  # img loading

    def attach_file_is_displayed(self):
        return self.find_element(file_img).is_displayed()

    def click_submit_button(self):
        self.find_element(submit_button).click()

    def alert_message_is_displayed(self):
        return self.find_element(alert_message)

    def enter_name_details(self, lot_name):
        self.find_element(lot_name_field).send_keys(lot_name)

    def choose_section(self):
        self.find_element(choose_section).click()

    def choose_main_section(self):
        self.find_element(collect_section).click()

    def choose_second_section(self):
        self.find_element(second_section).click()

    def choose_continent(self):
        self.find_element(continent_section).click()

    def choose_country(self):
        self.find_element(country_section).click()

    def choose_year(self):
        self.find_element(year_section).click()

    def select_condition(self):
        Select(self.find_element(condition)).select_by_index(8)



