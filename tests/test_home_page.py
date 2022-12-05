import pytest
import allure
from pages.home_page import HomePage
import settings


class TestLogIn:

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('Test of successful passed LogIn. Check that user name is displayed on home page Header')
    @allure.title('LogIn passed successful')
    @allure.severity('critical')
    def test_login_passed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.enter_login_details(email=settings.email, password=settings.password)
        home_page.click_enter_button()
        assert home_page.login_passed(), 'Login failed'

    CREDENTIALS = [
        {'login': 'qap2021@mail.ru', 'passwd': 'VuYay7'},
        {'login': 'qap2022@mail.ru', 'passwd': 'VuYay8'},
    ]

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('Test of failed LogIn. Check that alert message is displayed')
    @allure.title('LogIn failed')
    @allure.severity('critical')
    @pytest.mark.parametrize('creds', CREDENTIALS)
    def test_login_failed(self, driver, creds):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.enter_login_details(email=creds['login'], password=creds['passwd'])
        home_page.click_enter_button()
        assert home_page.login_failed(), 'Login passed'

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('LogOut Test')
    @allure.title('LogOut')
    @allure.severity('critical')
    def test_logout(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.logout(driver)
        assert home_page.logout_passed(), 'Logout failed'


class TestContent:
    SUBJECT = ['queen', '1984', '~', '0']

    @allure.feature('Home Page')
    @allure.story('Search field')
    @allure.description('Test of searching field')
    @allure.title('Search field')
    @allure.severity('critical')
    @pytest.mark.parametrize('sub', SUBJECT)
    def test_search_field(self, driver, sub):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_search_field()
        home_page.enter_search_details(sub)
        home_page.click_find_button()
        assert 'найдено' in home_page.search_result(), 'Not found'

    ERROR_SUBJECT = [
        {'answer': 'топор', 'request': 'njgjh'},
        {'answer': 'машина', 'request': 'vfibyf'},
        {'answer': 'монета', 'request': 'vjytnf'}
    ]

    @allure.feature('Home Page')
    @allure.story('Search field')
    @allure.description('Testing of recognition of error input  in searching field')
    @allure.title('Recognition of error input')
    @allure.severity('major')
    @pytest.mark.parametrize('e_sub', ERROR_SUBJECT)
    def test_recognition_of_error_input(self, driver, e_sub):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_search_field()
        home_page.enter_search_details(e_sub['request'])
        home_page.click_find_button()
        assert e_sub['answer'] in home_page.search_result()

    @allure.feature('Home Page')
    @allure.story('Side filters of lots')
    @allure.description('Changing section Test')
    @allure.title('Change section')
    @allure.severity('major')
    def test_change_section(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.change_section(driver)
        assert home_page.change_section_request() == home_page.change_section_result(), 'Section not changed'

    @allure.feature('Home Page')
    @allure.story('Content')
    @allure.description('Testing that we can go to any lot page')
    @allure.title('Go to any lot page')
    @allure.severity('critical')
    def test_go_to_any_lot_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        clicked_lot_name = home_page.name_of_clicked_lot()
        home_page.click_any_lot()
        assert clicked_lot_name == home_page.actual_lot_name(), 'Page didnt open'

    @allure.feature('Home Page')
    @allure.story('Content')
    @allure.description('Test of add lot to favorites')
    @allure.title('Add to favorites')
    @allure.severity('major')
    def test_add_to_favorites(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_any_lot()
        home_page.add_lot_to_favor()
        assert 'в избранном' in home_page.check_lot_added_in_favor(), 'Not in favorites'

    @allure.feature('Home Page')
    @allure.story('Head filters of lots')
    @allure.description('Choosing featured lots Test')
    @allure.title('Choose featured lots')
    @allure.severity('major')
    def test_choose_featured_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        request_featured_lots = home_page.featured_lots_request()
        home_page.choose_featured_lots()
        assert request_featured_lots == home_page.featured_lots_result(),\
            'Featured lots not selected'

    @allure.feature('Home Page')
    @allure.story('Head filters of lots')
    @allure.description('Resetting featured lots Test')
    @allure.title('Reset featured lots')
    @allure.severity('major')
    def test_reset_featured_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.choose_featured_lots()
        home_page.reset_featured_lots()
        assert home_page.all_lots_is_displayed(), 'All lots isnt displayed '

    @allure.feature('Home Page')
    @allure.story('Content')
    @allure.description('Testing that total number of lots on Home page meets the requirements')  # mark
    @allure.title('Total number of lots')
    @allure.severity('minor')
    def test_total_number_of_lots(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.check_total_number_of_lots() == 15, 'Total number doest meet the requirement'


class TestHeader:

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Test that main logo is displayed on home page')
    @allure.title('Main logo is displayed')
    @allure.severity('trivial')
    def test_main_logo_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.logo_is_displayed(), 'Logo isnt displayed'

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Test that my location is displayed on home page')
    @allure.title('Mu location is displayed')
    @allure.severity('trivial')
    def test_my_location_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.my_location_is_displayed(), 'My location isnt displayed'

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Changing of my location Test')
    @allure.title('Change of my location')
    @allure.severity('major')
    def test_change_of_location(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_location_button()
        home_page.select_wish_location()
        assert home_page.actual_location() in home_page.request_location(), 'Location wasnt changed '  # mark

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Testing of create lot button')
    @allure.title('Create lot button')
    @allure.severity('critical')
    def test_create_lot_button(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_create_lot_button()
        assert 'Создание лота' == home_page.title_of_creating_lot_page()


class TestFooter:

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by news are displayed')
    @allure.title('Ay.by news are displayed')
    @allure.severity('trivial')
    def test_news_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.news_ay_by_is_displayed()

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by forum are displayed')
    @allure.title('Ay.by forum is displayed')
    @allure.severity('minor')
    def test_forum_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.forum_ay_by_is_displayed()

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by info are displayed')
    @allure.title('Ay.by info is displayed')
    @allure.severity('trivial')
    def test_ay_by_info_is_displayed(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll_page_to_bottom()
        assert home_page.ay_by_info_is_displayed()
