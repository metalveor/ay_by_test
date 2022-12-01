from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import settings
from time import sleep

home_page_url = 'http://ay.by/'

login_button = (By.CSS_SELECTOR, 'li[class="top-panel__userbar__li"]')
user_name_field = (By.CSS_SELECTOR, 'span[class="top-panel__userbar__user__name"]')
user_name_field_elements = (By.CSS_SELECTOR, 'span[class="top-panel__userbar__ppnav__name"]')
login_alert = (By.CSS_SELECTOR, 'div[class="i-input-group__popover i-input-group__popover_login i-input-group__popover_visible"]')


search_answer = (By.CSS_SELECTOR, 'h1[class="section-title section-title_small"]')
sections = (By.CSS_SELECTOR, 'li[class="main-nav__list__li main-nav__list__li_wnav"]')
change_section_request = (By.CSS_SELECTOR, 'a[href="http://coins.ay.by/belarus-posle-1991/"]')
change_section_result = (By.CSS_SELECTOR, 'span[class="breadcrumbs__list__item"]')
all_lots_on_page = (By.CSS_SELECTOR, 'div[class="item-type-card__inner"]')
add_to_favor_button = (By.CSS_SELECTOR, 'div[class="b-lot-title__sub-aside"]')
product_header = (By.CSS_SELECTOR, 'h1[class="b-lot-title__title"]')
my_location = (By.CSS_SELECTOR, 'li[class="top-panel__hnav__li top-panel__hnav__withdrop"]')
wish_location = (By.CSS_SELECTOR, 'a[href="http://ay.by/personal/city.phtml?cid=5&cid_only=0&next=http%3A%2F%2Fay.by%2F"]')
main_logo = (By.CSS_SELECTOR, 'div[class="top-panel__logo"]')
recommended_lots_request = (By.CSS_SELECTOR, 'a[href="http://ay.by/popular/"]')
recommended_lots_result = (By.CSS_SELECTOR, 'a[href="http://ay.by/topic.phtml?topic=popular"]')
clear_button = (By.CSS_SELECTOR, 'li[class="filters__sqcheckers__li"]')
all_lots_button = (By.CSS_SELECTOR, 'span[data-aimnav-id="#list-types-content"]')
news_ay_by = (By.CSS_SELECTOR, 'div[class="news-headlines__col-1"]')
forum_ay_by = (By.CSS_SELECTOR, 'div[class="news-headlines__col-2"]')
ay_by_info = (By.CSS_SELECTOR, 'div[class="footer-compact__inner footer-compact__inner_bottom"]')
names_of_lots = (By.CSS_SELECTOR, 'p[class="item-type-card__title"]')
actual_lot_name = (By.CSS_SELECTOR, 'h1[class="b-lot-title__title"]')
create_lot_button = (By.CSS_SELECTOR, 'li[class="top-panel__userbar__li top-panel__userbar__addlot"]')
title_of_create = (By.CSS_SELECTOR, 'h1[id="page_title"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.open_page(home_page_url)

    def login_passed(self):
        return self.find_element(user_name_field).is_displayed()

    def login_failed(self):
        return self.find_element(login_alert).is_displayed()

    def logout(self, driver):
        ActionChains(driver).move_to_element(self.find_element(user_name_field)).click(
            self.find_elements(user_name_field_elements)[5]).perform()

    def logout_passed(self):
        return self.find_element(login_button).is_displayed()

    def search_answer_txt(self):
        return self.find_element(search_answer).text.lower()

    def change_section(self, driver):
        ActionChains(driver).move_to_element((self.find_elements(sections))[0]).click(
            self.find_element(change_section_request)).perform()

    def change_section_request_txt(self):
        return self.find_element(change_section_request).get_attribute("innerText").lower()
        # return self.find_element(change_section_request).text.lower()  <- doesn't work?

    def change_section_result_txt(self):
        return self.find_element(change_section_result).text.lower()

    def add_product_to_favor(self):
        (self.find_elements(all_lots_on_page))[-1].click()
        self.find_element(add_to_favor_button).click()
        sleep(1)  # page loading

    def add_to_favor_txt(self):
        return self.find_element(add_to_favor_button).text.lower()

    def my_location_is_displayed(self):
        return self.find_element(my_location).is_displayed()

    def change_of_location(self):
        self.find_element(my_location).click()
        self.find_element(wish_location).click()

    def request_location(self):
        return self.find_element(wish_location).get_attribute("innerText")

    def changed_location(self):
        return self.find_element(my_location).text

    def logo_is_displayed(self):
        return self.find_element(main_logo).is_displayed()

    def select_recommended_lots(self):
        self.find_element(recommended_lots_request).click()

    def recommended_lots_request(self):
        return self.find_element(recommended_lots_request).text

    def recommended_lots_result(self):
        return self.find_element(recommended_lots_result).text

    def reset_recommended_lots(self):
        self.select_recommended_lots()
        self.find_element(clear_button).click()

    def all_lots_is_displayed(self):
        return self.find_element(all_lots_button).is_displayed()

    def news_ay_by_is_displayed(self):
        return self.find_element(news_ay_by).is_displayed()

    def forum_ay_by_is_displayed(self):
        return self.find_element(forum_ay_by).is_displayed()

    def ay_by_info_is_displayed(self):
        return self.find_element(ay_by_info).is_displayed()

    def check_total_number_of_lots(self):
        return len(self.find_elements(all_lots_on_page))

    def click_any_lot(self):
        self.find_elements(all_lots_on_page)[0].click()

    def name_of_clicked_lot(self):
        return self.find_elements(names_of_lots)[0].text

    def actual_lot_name(self):
        return self.find_element(actual_lot_name).text

    def click_create_lot_button(self):
        self.find_element(create_lot_button).click()

    def title_of_creating_lot_page(self):
        return self.find_element(title_of_create).text

