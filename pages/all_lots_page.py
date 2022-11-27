from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


all_lots_page_url = 'http://ay.by/topic.phtml?f=1'

all_lots_button = (By.CSS_SELECTOR, 'span[data-aimnav-id="#list-types-content"]')
for_free_button = (By.CSS_SELECTOR, 'a[data-value="3"]')
main_title = (By.CSS_SELECTOR, 'h1[class="section-title"]')
relevant_button = (By.CSS_SELECTOR, 'span[data-aimnav-id="#list-sorter-content"]')
expensive_button = (By.CSS_SELECTOR, 'a[data-value="cost_desc"]')
first_lot = (By.XPATH, '//*[@id="lots-table"]/li[1]/div/div/div/div/p[1]//strong')
last_lot = (By.XPATH, '//*[@id="lots-table"]/li[96]/div/div/div/div/p[1]//strong')
settings_button = (By.CSS_SELECTOR, 'div[class="top-filters__split"]')
list_view_button = (By.CSS_SELECTOR, 'a[data-value="list"]')
grid_view_button = (By.CSS_SELECTOR, 'a[data-value="grid"]')
sorted_list = (By.CSS_SELECTOR, 'ul[id="lots-table"]')
little_button = (By.CSS_SELECTOR, 'a[data-value="1"]')
lots_amount_button = (By.CSS_SELECTOR, 'a[data-value="24"]')
all_lots_on_page = (By.CSS_SELECTOR, 'div[class="item-type-card__inner"]')
next_page_button = (By.CSS_SELECTOR, 'strong[class="pg-next-title"]')
current_page_button = (By.CSS_SELECTOR, 'a[class="g-pagination__list__item g-pagination__list__item_active"]')
last_page_button = (By.CSS_SELECTOR, 'li[class="g-pagination__list__li pg-link pg-last"]')
all_sections = (By.CSS_SELECTOR, 'a[class="filters__simplist__item"]')
show_button = (By.CSS_SELECTOR, 'a[class="dp-showresults__content dp-base_clt"]')
relisted_button = (By.CSS_SELECTOR, 'label[for="createdlots_1"]')
type_button = (By.CSS_SELECTOR, 'label[for="tab_1"]')
condition_button = (By.CSS_SELECTOR, 'label[for="condition_id_1"]')
price_byn_from = (By.CSS_SELECTOR, 'input[id="inp1_cost_byr"]')
price_byn_to = (By.CSS_SELECTOR, 'input[id="inp2_cost_byr"]')

class AllLotsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_all_lots_page(self):
        self.open_page(all_lots_page_url)

    def all_lots_is_displayed(self):
        return self.find_element(all_lots_button).is_displayed()

    def change_type_auction(self):
        self.find_element(all_lots_button).click()
        self.find_element(for_free_button).click()

    def change_type_auction_request(self):
        return self.find_element(for_free_button).text.lower()

    def check_changed_type_auction(self):
        return self.find_element(main_title).text.lower()

    def change_relevance_auction(self):
        self.find_element(relevant_button).click()
        self.find_element(expensive_button).click()

    def most_relevant_result(self):
        return self.find_element(first_lot).text

    def less_relevant_result(self):
        return self.find_element(last_lot).text

    def change_list_view(self):
        self.find_element(settings_button).click()
        self.find_element(list_view_button).click()

    def type_of_list_request(self):
        if self.find_element(list_view_button).get_attribute("innerText") == 'Список':
            return 'type-list'
        else:
            return 'type-grid'

    def check_selected_view(self):
        return self.find_element(sorted_list).get_attribute("class")

    def change_list_image_size(self):
        self.change_list_view()
        self.find_element(settings_button).click()
        self.find_elements(little_button)[1].click()

    def check_selected_image_size(self):
        return self.find_element(sorted_list).get_attribute("class")

    def change_amount_lots_per_page(self):
        self.find_element(settings_button).click()
        self.find_element(lots_amount_button).click()

    def amount_of_lots_request(self):
        return int(self.find_element(lots_amount_button).get_attribute("innerText"))

    def check_amount_of_lots(self):
        return len(self.find_elements(all_lots_on_page))-6

    def click_next_page_button(self):
        self.find_element(next_page_button).click()

    # def check_next_page_opened(self):
    #     print(self.driver.current_url)

    def current_page_number(self):
        return int(self.find_element(current_page_button).text)

    def click_last_page_button(self):
        self.find_element(last_page_button).click()

    def last_page_number(self):
        return int(self.find_element(last_page_button).text)

    def click_any_section(self):
        self.find_elements(all_sections)[-1].click()

    def actual_section_name(self):
        return self.find_element(main_title).text

    def name_of_clicked_section(self):
        return self.find_elements(all_sections)[-1].text

    def check_box_set(self):
        self.find_element(relisted_button).click()
        self.find_element(type_button).click()
        self.find_element(condition_button).click()

    def click_show_result_button(self):
        self.find_element(show_button).click()

    def count_filtered_lots(self):
        return int(''.join(x for x in self.find_element(show_button).text if x.isdigit()))

    def total_lots_showed(self):
        return int(''.join(x for x in self.find_element(all_lots_button).text if x.isdigit()))  # mark

    def enter_price_details(self, price_from, price_to):
        self.find_element(price_byn_from).send_keys(price_from)
        self.find_element(price_byn_to).send_keys(price_to)
        assert True
