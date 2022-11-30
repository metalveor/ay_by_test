import pytest
from pages.sell_page import SellPage
import settings
from time import sleep


class TestCreateLot:

    def test_lot_creation_passed(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.enter_name_details('Тестовый рубль-заяц')
        sell_page.choose_section()
        sell_page.choose_main_section()
        sell_page.choose_second_section()
        sell_page.choose_continent()
        sell_page.choose_country()
        sell_page.choose_year()
        sell_page.select_condition()
        sleep(10)

    def test_lot_creation_failed(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.click_submit_button()
        assert sell_page.alert_message_is_displayed()

    # def test_change_description_frame_size(self, driver):
    #     sell_page = SellPage(driver)
    #     sell_page.open_sell_page()
    #     sell_page.scroll_page_to_bottom()
    #     sell_page.click_drag_button(driver)

    def test_attach_file(self, driver):
        sell_page = SellPage(driver)
        sell_page.open_sell_page()
        sell_page.attach_file()
        assert sell_page.attach_file_is_displayed()
