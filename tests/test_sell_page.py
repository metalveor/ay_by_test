import pytest
import allure
from pages.sell_page import SellPage


class TestCreateNewLot:

    lot_name = 'Тестовый рубль-заяц'

    @allure.feature('Sell Page')
    @allure.story('Create new lot')
    @allure.description('Test of successful passed lot creation. Check that lot placed at auction')
    @allure.title(f'Creation of lot <{lot_name}> passed successful')
    @allure.severity('critical')
    def test_lot_creation_passed(self, driver, authorization):
        sell_page = SellPage(driver)
        with allure.step('Open Sell page'):
            sell_page.open_sell_page()
        with allure.step('Enter new lot name'):
            sell_page.enter_name_details(self.lot_name)
        with allure.step('Choose "выбрать раздел вручную" section'):
            sell_page.choose_section()
        with allure.step('Choose main section: "Коллекционирование"'):
            sell_page.choose_main_section()
        with allure.step('Choose second section: "Банкноты. Ценные бумаги"'):
            sell_page.choose_second_section()
        with allure.step('Choose the continent: "Европа"'):
            sell_page.choose_continent()
        with allure.step('Choose the country: "Беларусь"'):
            sell_page.choose_country()
        with allure.step('Choose the year: "Выпуск 1992"'):
            sell_page.choose_year()
        with allure.step('Select lot condition: "Poor (PR)"'):
            sell_page.select_condition()
        with allure.step('Enter lot condition details'):
            sell_page.enter_condition_details('TMS Testing')
        with allure.step('Enter denomination of banknotes'):
            sell_page.enter_denomination('Рубль')
        with allure.step('Enter the year circulation in'):
            sell_page.enter_year_in('1992')
        with allure.step('Enter the year circulation till'):
            sell_page.enter_year_till('2001')
        with allure.step('Enter banknotes size'):
            sell_page.enter_size_details('105×53')
        with allure.step('Attach the image of banknotes'):
            sell_page.attach_file('my_lot.jpg')
        with allure.step('Choose the type of auction: "Хочу купить"'):
            sell_page.choose_type_of_auction()
        with allure.step('Enter the number of banknotes'):
            sell_page.enter_number_details('10')
        with allure.step('Enter maximal banknotes price'):
            sell_page.enter_max_price('1')
        with allure.step('Select the duration of trading'):
            sell_page.select_duration_of_trading("30")
        with allure.step('Select the lot location'):
            sell_page.select_location('Минск')
        with allure.step('Choose delivery details: "Отправка почтой"'):
            sell_page.choose_delivery_details()
        with allure.step('Choose payment details: "Полная предоплата до отправки лота по почте "'):
            sell_page.choose_payment_details()
        with allure.step('Enter delivery cost'):
            sell_page.enter_delivery_cost_details('100')
        with allure.step('Choose payment delivery details: "Продавец"'):
            sell_page.choose_payment_delivery_details()
        with allure.step('Enter other details'):
            sell_page.enter_details_field('TMS Testing')
        with allure.step('Enter description'):
            sell_page.enter_description_field('TMS Testing of lot creation ')
        with allure.step('Click submit button'):
            sell_page.click_submit_button()
        with allure.step('Check in profile that my lot created'):
            assert sell_page.check_my_lot_in_profile(), f'New lot <{self.lot_name}> didnt create'
        with allure.step('Check that my lot created by searching'):
            assert sell_page.check_my_lot_in_searching(self.lot_name),\
                f'New lot <{self.lot_name}> didnt find in global searching'

    @allure.feature('Sell Page')
    @allure.story('Create new lot')
    @allure.description('Test of failed lot creation. Check that alert message is displayed')
    @allure.title('Creation of lot failed')
    @allure.severity('major')
    def test_lot_creation_failed(self, driver, authorization):
        sell_page = SellPage(driver)
        with allure.step('Open Sell page'):
            sell_page.open_sell_page()
        with allure.step('Scroll page to bottom'):
            sell_page.scroll_page_to_bottom()
        with allure.step('Click submit button'):
            sell_page.click_submit_button()
        with allure.step('Check that alert message is displayed'):
            assert sell_page.alert_message_is_displayed(), 'Alert message didnt displayed'


class TestFields:

    @allure.feature('Sell Page')
    @allure.story('Testing of fields')
    @allure.description('Description frame resizing Test')
    @allure.title('Description frame resizing')
    @allure.severity('minor')
    def test_change_description_frame_size(self, driver, authorization):
        sell_page = SellPage(driver)
        with allure.step('Open Sell page'):
            sell_page.open_sell_page()
        with allure.step('Scroll page to bottom'):
            sell_page.scroll_page_to_bottom()
        with allure.step('Get size before drag'):
            size_before = sell_page.check_size()
        with allure.step('Click and drag button of form size '):
            sell_page.click_drag_button(driver)
        with allure.step('Get size after drag'):
            size_after = sell_page.check_size()
        with allure.step(f'Compare size before dragged {size_before} and size ather dragged {size_after}'):
            assert size_before < size_after, 'Resizing of description frame failed'

    @allure.feature('Sell Page')
    @allure.story('Testing of fields')
    @allure.description('Test of attaching file')
    @allure.title('Attach File')
    @allure.severity('major')
    def test_attach_file(self, driver, authorization):
        sell_page = SellPage(driver)
        with allure.step('Open Sell page'):
            sell_page.open_sell_page()
        with allure.step('Attach the image of lot'):
            sell_page.attach_file('my_lot.jpg')
        with allure.step('Check that attached image is displayed'):
            assert sell_page.attach_file_is_displayed(), 'File attachment failed'
