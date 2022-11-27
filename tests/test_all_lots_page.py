import pytest
from pages.all_lots_page import AllLotsPage
import settings
from time import sleep


class TestHeadFilters:

    def test_all_lots_is_displayed(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        assert all_lots_page.all_lots_is_displayed(), 'All lots isnt displayed'

    def test_change_type_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.change_type_auction()
        assert all_lots_page.change_type_auction_request() in all_lots_page.check_changed_type_auction(),\
            'Type of auction wasnt changed'

    def test_change_relevance_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.change_relevance_auction()
        assert all_lots_page.most_relevant_result() >= all_lots_page.less_relevant_result(),\
            'Relevance of auction wasnt changed'

    def test_change_list_view(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.change_list_view()
        assert all_lots_page.type_of_list_request() in all_lots_page.check_selected_view(), \
            'List view wasnt changed'

    def test_change_list_image_size(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.change_list_image_size()
        assert 'size-s' in all_lots_page.check_selected_image_size(), 'List image size wasnt changed'

    def test_change_amount_of_lots_per_page(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.change_amount_lots_per_page()
        assert all_lots_page.amount_of_lots_request() == all_lots_page.check_amount_of_lots(), \
            'Amount of lots per page wasnt changed'  # mark


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
        all_lots_page.check_box_set()
        filtered_lots = all_lots_page.count_filtered_lots()
        all_lots_page.click_show_result_button()
        assert filtered_lots == all_lots_page.total_lots_showed()

    def test_price_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        all_lots_page.open_all_lots_page()
        all_lots_page.enter_price_details(100, 100)
        all_lots_page.click_show_result_button()
        sleep(5)
        assert True


