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
condition_detail_field = (By.CSS_SELECTOR, 'input[id="condition_comment"]')
denomination_field = (By.CSS_SELECTOR, 'input[id="v1"]')
year_in_field = (By.CSS_SELECTOR, 'input[id="si1"]')
year_till_field = (By.CSS_SELECTOR, 'input[id="si2"]')
size_field = (By.CSS_SELECTOR, 'input[id="v2"]')
type_of_auction = (By.CSS_SELECTOR, 'a[id="type_link_buy"]')
count_field = (By.CSS_SELECTOR, 'input[name="count"]')
max_price = (By.CSS_SELECTOR, 'input[id="auc_pricecost"]')
duration_select = (By.CSS_SELECTOR, 'select[id="auc_time"]')
city_select = (By.CSS_SELECTOR, 'select[id="auc_city"]')
delivery = (By.CSS_SELECTOR, 'input[id="auc_delpay_2"]')
payment = (By.CSS_SELECTOR, 'input[id="auc_delpay_6"]')
delivery_cost = (By.CSS_SELECTOR, 'input[id="auc_delpay_txt_6"]')
payment_delivery = (By.CSS_SELECTOR, 'input[id="auc_whopay_0"]')
details_pay_del_field = (By.CSS_SELECTOR, 'textarea[id="auc_delpaytxt"]')
lot_description = (By.CSS_SELECTOR, 'iframe[id="textareaWidgIframe"]')
my_lot = (By.CSS_SELECTOR, 'div[class="item-type-card__inner"]')
my_profile_button = (By.CSS_SELECTOR, 'span[class="top-panel__userbar__user__name"]')
my_lot_in_profile = (By.CSS_SELECTOR, 'div[class="ph-cov-i ph-cov-ni"]')


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

    def attach_file(self, lot_img):
        self.find_elements(attach_button)[1].send_keys(os.path.join(os.path.dirname(__file__), lot_img))
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

    def enter_condition_details(self, details):
        self.find_element(condition_detail_field).send_keys(details)

    def enter_denomination(self, denomination):
        self.find_element(denomination_field).send_keys(denomination)

    def enter_year_in(self, year_in):
        self.find_element(year_in_field).send_keys(year_in)

    def enter_year_till(self, year_till):
        self.find_element(year_till_field).send_keys(year_till)

    def enter_size_details(self, size):
        self.find_element(size_field).send_keys(size)

    def choose_type_of_auction(self):
        self.find_element(type_of_auction).click()

    def enter_number_details(self, num):
        self.find_element(count_field).send_keys(num)

    def enter_max_price(self, price):
        self.find_element(max_price).send_keys(price)

    def select_duration_of_trading(self, days):
        Select(self.find_element(duration_select)).select_by_value(days)

    def select_location(self, city):
        Select(self.find_element(city_select)).select_by_visible_text(city)

    def choose_delivery_details(self):
        self.find_element(delivery).click()

    def choose_payment_details(self):
        self.find_element(payment).click()

    def enter_delivery_cost_details(self, cost):
        self.find_element(delivery_cost).send_keys(cost)

    def choose_payment_delivery_details(self):
        self.find_element(payment_delivery).click()

    def enter_details_field(self, details):
        self.find_element(details_pay_del_field).send_keys(details)

    def enter_description_field(self, description):
        self.find_element(lot_description).send_keys(description)

    def check_my_lot_in_searching(self, lot_name):
        self.open_page(home_page_url)
        self.click_search_field()
        self.enter_search_details(lot_name)
        self.click_find_button()
        return self.find_element(my_lot).is_displayed()

    def check_my_lot_in_profile(self):
        self.open_page(home_page_url)
        self.find_element(my_profile_button).click()
        return self.find_element(my_lot_in_profile).is_displayed()



