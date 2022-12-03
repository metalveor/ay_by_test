import pytest
import allure
from pages.all_lots_page import AllLotsPage


class TestHeadFilters:

    def test_all_lots_is_displayed(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        assert all_lots_page.all_lots_is_displayed(), 'All lots isnt displayed'

    def test_change_type_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_all_lots_button()
        all_lots_page.select_wish_type_auction()
        assert all_lots_page.request_type_auction() in all_lots_page.check_actual_type_auction(),\
            'Type of auction wasnt changed'

    def test_change_relevance_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_relevant_button()
        all_lots_page.select_wish_relevance_auction()
        assert all_lots_page.first_lot_on_page() >= all_lots_page.last_lot_on_page(),\
            'Relevance of auction wasnt changed'

    def test_change_list_view(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_settings_button()
        all_lots_page.select_type_of_view()
        assert all_lots_page.type_of_list_request() in all_lots_page.check_actual_view(), \
            'List view wasnt changed'

    def test_change_list_image_size(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_settings_button()
        all_lots_page.select_type_of_view()
        all_lots_page.click_settings_button()
        all_lots_page.select_list_image_size()
        assert 'size-s' in all_lots_page.check_actual_image_size(), 'List image size wasnt changed'

    def test_change_number_of_lots_per_page(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_settings_button()
        all_lots_page.select_number_lots_per_page()
        assert all_lots_page.number_of_lots_request() == all_lots_page.check_actual_number_of_lots(), \
            'Number of lots per page wasnt changed'  # mark


class TestFootFilters:

    def test_next_page_button(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.scroll_page_to_bottom()
        start_page = all_lots_page.current_page_number()
        all_lots_page.click_next_page_button()
        assert all_lots_page.current_page_number() == start_page + 1

    def test_last_page_button(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.scroll_page_to_bottom()
        last_page = all_lots_page.last_page_number()
        all_lots_page.click_last_page_button()
        assert all_lots_page.current_page_number() == last_page


class TestSideFilters:

    def test_all_section_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        clicked_section_name = all_lots_page.name_of_clicked_section()
        all_lots_page.click_any_section()
        assert clicked_section_name == all_lots_page.actual_section_name()

    def test_check_box_filter_set(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_checkbox_set()
        filtered_lots = all_lots_page.count_filtered_lots()
        all_lots_page.click_show_result_button()
        assert filtered_lots == all_lots_page.total_lots_showed()

    def test_price_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.enter_price_details('100,00', '100,00')
        all_lots_page.click_show_result_button()
        assert all_lots_page.first_lot_on_page() == all_lots_page.last_lot_on_page()
        assert all_lots_page.first_lot_on_page() == '100,00'
        assert all_lots_page.last_lot_on_page() == '100,00'

    def test_choose_lots_location(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.click_button_chosen_location()
        all_lots_page.click_show_result_button()
        name_of_request_location = all_lots_page.location_request()
        all_lots_page.click_any_lot()
        assert name_of_request_location in all_lots_page.actual_lot_location()

    def test_seller_rating_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.select_five_star_rating()
        rating_percent_request = all_lots_page.rating_request()
        all_lots_page.click_show_result_button()
        all_lots_page.click_any_lot()
        assert rating_percent_request <= all_lots_page.actual_seller_rating()
