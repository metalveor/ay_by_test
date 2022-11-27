import pytest
from pages.home_page import HomePage
import settings
from time import sleep


class TestLogIn:

    def test_login_passed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.enter_login_details(email=settings.email, password=settings.password)
        assert home_page.login_passed(), 'Login failed'

    CREDENTIALS = [
        {'login': 'qap2021@mail.ru', 'passwd': 'VuYay7'},
        {'login': 'qap2022@mail.ru', 'passwd': 'VuYay8'},
    ]

    @pytest.mark.parametrize('creds', CREDENTIALS)
    def test_login_failed(self, driver, creds):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.enter_login_details(email=creds['login'], password=creds['passwd'])
        assert home_page.login_failed(), 'Login passed'

    def test_logout(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.login()
        home_page.logout(driver)
        assert home_page.logout_passed(), 'Logout failed'


class TestContent:
    SUBJECT = ['queen', '1984', '~', '0']

    @pytest.mark.parametrize('sub', SUBJECT)
    def test_search_field(self, driver, sub):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_search_field()
        home_page.enter_search_details(sub)
        home_page.click_find_button()
        assert 'найдено' in home_page.search_answer_txt(), 'Not found'

    ERROR_SUBJECT = [
        {'need': 'топор', 'have': 'njgjh'},
        {'need': 'машина', 'have': 'vfibyf'},
        {'need': 'монета', 'have': 'vjytnf'}
    ]

    @pytest.mark.parametrize('e_sub', ERROR_SUBJECT)
    def test_recognition_of_error_input(self, driver, e_sub):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_search_field()
        home_page.enter_search_details(e_sub['have'])
        home_page.click_find_button()
        assert e_sub['need'] in home_page.search_answer_txt()

    def test_change_section(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.change_section(driver)
        assert home_page.change_section_request_txt() == home_page.change_section_result_txt(), 'Section not changed'

    def test_go_to_any_lot_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        clicked_lot_name = home_page.name_of_clicked_lot()
        home_page.click_any_lot()
        assert clicked_lot_name == home_page.actual_lot_name(), 'Page didnt open'

    def test_add_favorites(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.login()
        sleep(1)  # page loading
        home_page.add_product_to_favor()
        sleep(1)  # page loading
        assert 'в избранном' in home_page.add_to_favor_txt(), 'Not in favorites'

    def test_select_recommended_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        request_recommended_lots = home_page.recommended_lots_request()
        home_page.select_recommended_lots()
        assert request_recommended_lots == home_page.recommended_lots_result(),\
            'Recommended lots not selected'

    def test_reset_recommended_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.reset_recommended_lots()
        assert home_page.all_lots_is_displayed(), 'All lots isnt displayed '

    def test_total_number_of_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.check_total_number_of_lots() == 15, 'Total number doest meet the requirement'


class TestHeader:

    def test_main_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.logo_is_displayed(), 'Logo isnt displayed'

    def test_my_location(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.my_location_is_displayed(), 'My location isnt displayed'

    def test_change_of_location(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.change_of_location()
        assert home_page.changed_location() in home_page.request_location(), 'Location wasnt changed '  # mark

    def test_create_lot_button(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.login()
        sleep(1)  # page loading
        home_page.click_create_lot_button()
        assert 'Создание лота' == home_page.title_of_creating_lot_page()


class TestFooter:

    def test_news_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.news_ay_by_is_displayed()

    def test_forum_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.forum_ay_by_is_displayed()

    def test_ay_by_info_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.ay_by_info_is_displayed()
