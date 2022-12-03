import pytest
import allure
from pages.sell_page import SellPage
import settings
from time import sleep


class TestCreateNewLot:

    lot_name = 'Тестовый рубль-заяц'

    def test_lot_creation_passed(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.enter_name_details(self.lot_name)
        sell_page.choose_section()
        sell_page.choose_main_section()
        sell_page.choose_second_section()
        sell_page.choose_continent()
        sell_page.choose_country()
        sell_page.choose_year()
        sell_page.select_condition()
        sell_page.enter_condition_details('TMS Testing')
        sell_page.enter_denomination('Рубль')
        sell_page.enter_year_in('1992')
        sell_page.enter_year_till('2001')
        sell_page.enter_size_details('105×53')
        sell_page.attach_file('my_lot.jpg')
        sell_page.choose_type_of_auction()
        sell_page.enter_number_details('10')
        sell_page.enter_max_price('1')
        sell_page.select_duration_of_trading("30")
        sell_page.select_location('Минск')
        sell_page.choose_delivery_details()
        sell_page.choose_payment_details()
        sell_page.enter_delivery_cost_details('100')
        sell_page.choose_payment_delivery_details()
        sell_page.enter_details_field('TMS Testing')
        sell_page.enter_description_field('TMS Testing of lot creation ')
        sell_page.click_submit_button()
        assert sell_page.check_my_lot_in_searching(self.lot_name)
        assert sell_page.check_my_lot_in_profile()

    def test_lot_creation_failed(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.click_submit_button()
        assert sell_page.alert_message_is_displayed()


class TestFields:

    def test_change_description_frame_size(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.scroll_page_to_bottom()
        size_before = sell_page.check_size()
        sell_page.click_drag_button(driver)
        size_after = sell_page.check_size()
        assert size_before < size_after

    def test_attach_file(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.attach_file('my_lot.jpg')
        assert sell_page.attach_file_is_displayed()
