import pytest
import allure
from pages.all_lots_page import AllLotsPage


class TestHeadFilters:

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Displaying of all lots on page Test')
    @allure.title('All lots are displayed')
    @allure.severity('major')
    def test_all_lots_is_displayed(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Check that all lots are displayed'):
            assert all_lots_page.all_lots_is_displayed(), 'All lots isnt displayed'

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Changing type of auction Test')
    @allure.title('Change type of auction')
    @allure.severity('major')
    def test_change_type_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click all lots button'):
            all_lots_page.click_all_lots_button()
        with allure.step('Select wish type of auction: "Даром"'):
            all_lots_page.select_wish_type_auction()
        with allure.step('Check that type of auction is "Даром"'):
            assert all_lots_page.request_type_auction() in all_lots_page.check_actual_type_auction(),\
                'Type of auction wasnt changed'

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Changing relevance of auction Test')
    @allure.title('Change relevance of auction')
    @allure.severity('major')
    def test_change_relevance_of_auction(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click relevant button'):
            all_lots_page.click_relevant_button()
        with allure.step('Select wish relevance of auction: "Дорогие"'):
            all_lots_page.select_wish_relevance_auction()
        with allure.step('Check that type of relevance is "Дорогие"'):
            assert all_lots_page.first_lot_on_page() >= all_lots_page.last_lot_on_page(),\
                'Relevance of auction wasnt changed'

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Changing type of lots view Test')
    @allure.title('Change type of view')
    @allure.severity('minor')
    def test_change_type_of_view(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click settings button'):
            all_lots_page.click_settings_button()
        with allure.step('Select type of view "Список"'):
            all_lots_page.select_type_of_view()
        with allure.step('Check that type of view is "Список"'):
            assert all_lots_page.type_of_view_request() in all_lots_page.check_actual_view(), \
                'Type of lots view wasnt changed'

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Changing size of image in list Test')
    @allure.title('Change list image size')
    @allure.severity('minor')
    def test_change_image_size_in_list(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click settings button'):
            all_lots_page.click_settings_button()
        with allure.step('Select type of view "Список"'):
            all_lots_page.select_type_of_view()
        with allure.step('Click settings button'):
            all_lots_page.click_settings_button()
        with allure.step('Select image size: "Маленькие"'):
            all_lots_page.select_image_size()
        with allure.step('Check that size of image is "Маленькие"'):
            assert 'size-s' in all_lots_page.check_actual_image_size(), 'Size of image in list wasnt changed'

    @allure.feature('All Lots Page')
    @allure.story('Head filters of lots')
    @allure.description('Changing number of lots per page Test')
    @allure.title('Change number of lots per page')
    @allure.severity('minor')
    def test_change_number_of_lots_per_page(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click settings button'):
            all_lots_page.click_settings_button()
        with allure.step('Select number of lots per page: "24"'):
            all_lots_page.select_number_lots_per_page()
        with allure.step('Check that there are "24" lots per page'):
            assert all_lots_page.number_of_lots_request() == all_lots_page.check_actual_number_of_lots(), \
                'Number of lots per page wasnt changed'  # mark


class TestFootFilters:

    @allure.feature('All Lots Page')
    @allure.story('Foot filters of lots')
    @allure.description('Test of next page button')
    @allure.title('Next page button')
    @allure.severity('major')
    def test_next_page_button(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Scroll page to bottom'):
            all_lots_page.scroll_page_to_bottom()
        with allure.step('Get current page number'):
            start_page = all_lots_page.current_page_number()
        with allure.step('Click next page button'):
            all_lots_page.click_next_page_button()
        with allure.step('Check that we are on the next page'):
            assert all_lots_page.current_page_number() == start_page + 1

    @allure.feature('All Lots Page')
    @allure.story('Foot filters of lots')
    @allure.description('Test of last page button')
    @allure.title('Last page button')
    @allure.severity('major')
    def test_last_page_button(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Scroll page to bottom'):
            all_lots_page.scroll_page_to_bottom()
        with allure.step('Get last page number'):
            last_page = all_lots_page.last_page_number()
        with allure.step('Click last page button'):
            all_lots_page.click_last_page_button()
        with allure.step('Check that we are on the last page'):
            assert all_lots_page.current_page_number() == last_page


class TestSideFilters:

    @allure.feature('All Lots Page')
    @allure.story('Side filters of lots')
    @allure.description('Testing the filter of all section')
    @allure.title('Filter of all section')
    @allure.severity('major')
    def test_filter_of_section(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Get name of clicked section'):
            clicked_section_name = all_lots_page.name_of_clicked_section()
        with allure.step('Click any section: "Электроника"'):
            all_lots_page.click_any_section()
        with allure.step('Check that current section is "Электроника"'):
            assert clicked_section_name == all_lots_page.actual_section_name()

    @allure.feature('All Lots Page')
    @allure.story('Side filters of lots')
    @allure.description('Testing the filter by checkbox set ')
    @allure.title('Filter by checkbox set')
    @allure.severity('major')
    def test_filter_by_checkbox_set(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Click our checkbox set[Новые, Новые, Новое]'):
            all_lots_page.click_checkbox_set()
        with allure.step('Get number of filtered lots'):
            filtered_lots = all_lots_page.number_filtered_lots()
        with allure.step('Click show result button'):
            all_lots_page.click_show_result_button()
        with allure.step('Compare number of filtered lots with current number of lots'):
            assert filtered_lots == all_lots_page.total_lots_showed()

    @allure.feature('All Lots Page')
    @allure.story('Side filters of lots')
    @allure.description('Testing the price filter')
    @allure.title('Price filter')
    @allure.severity('major')
    def test_price_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Enter price details'):
            all_lots_page.enter_price_details(100, 100)
        with allure.step('Click show result button'):
            all_lots_page.click_show_result_button()
        with allure.step('Compare price of first lot and last lot on page with enter price'):
            assert all_lots_page.first_lot_on_page() == '100,00' == all_lots_page.last_lot_on_page()

    @allure.feature('All Lots Page')
    @allure.story('Side filters of lots')
    @allure.description('Testing the seller rating filter')
    @allure.title('Seller rating filter')
    @allure.severity('major')
    def test_seller_rating_filter(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Select five star rating'):
            all_lots_page.select_five_star_rating()
        with allure.step('Get requested rating in percent'):
            rating_percent_request = all_lots_page.rating_request()
        with allure.step('Click show result button'):
            all_lots_page.click_show_result_button()
        with allure.step('Click any lot on page'):
            all_lots_page.click_any_lot()
        with allure.step('Check that seller rating in percent is equals five star'):
            assert rating_percent_request <= all_lots_page.actual_seller_rating()

    @allure.feature('All Lots Page')
    @allure.story('Side filters of lots')
    @allure.description('Choose lots location Test')
    @allure.title('Choose lots location')
    @allure.severity('major')
    def test_choose_lots_location(self, driver):
        all_lots_page = AllLotsPage(driver)
        with allure.step('Open All lots page'):
            all_lots_page.open_all_lots_page()
        with allure.step('Choose the location of lots: "Гродно"'):
            all_lots_page.click_button_chosen_location()
        with allure.step('Click show result button'):
            all_lots_page.click_show_result_button()
        with allure.step('Get name of chosen location'):
            name_of_request_location = all_lots_page.location_request()
        with allure.step('Click any lot on page'):
            all_lots_page.click_any_lot()
        with allure.step('Check that location of lots is "Гродно"'):
            assert name_of_request_location in all_lots_page.actual_lot_location()
