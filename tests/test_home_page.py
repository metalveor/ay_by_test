import pytest
import allure
from pages.home_page import HomePage
import settings


class TestLogIn:

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('Testing of login button')
    @allure.title('login button')
    @allure.severity('critical')
    def test_login_button(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click login button'):
            home_page.click_login_button()
        with allure.step('Check that login frame is displayed'):
            assert home_page.login_frame_is_displayed(), 'Login button didnt work'

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('Test of successful passed LogIn. Check that user name is displayed on home page Header')
    @allure.title('LogIn passed successful')
    @allure.severity('critical')
    def test_login_passed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click login button'):
            home_page.click_login_button()
        with allure.step(f'Enter email = {settings.email} and password = {settings.password}'):
            home_page.enter_login_details(email=settings.email, password=settings.password)
        with allure.step('Click enter button'):
            home_page.click_enter_button()
        with allure.step('Check that login passed successful'):
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
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click login button'):
            home_page.click_login_button()
        with allure.step(f"Enter email = {creds['login']} and password = {creds['passwd']}"):
            home_page.enter_login_details(email=creds['login'], password=creds['passwd'])
        with allure.step('Click enter button'):
            home_page.click_enter_button()
        with allure.step('Check that login failed and alert message is displayed'):
            assert home_page.login_failed(), 'Login passed'

    @allure.feature('Home Page')
    @allure.story('Authorization')
    @allure.description('LogOut Test')
    @allure.title('LogOut')
    @allure.severity('critical')
    def test_logout(self, driver, authorization):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Clock logout button'):
            home_page.logout(driver)
        with allure.step('Check that logout passed successful'):
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
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click on search field'):
            home_page.click_search_field()
        with allure.step(f'Enter searching lot {sub}'):
            home_page.enter_search_details(sub)
        with allure.step('Click find button'):
            home_page.click_find_button()
        with allure.step(f'Check that lot {sub} is "найдено"'):
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
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click on search field'):
            home_page.click_search_field()
        with allure.step(f"Enter searching lot {e_sub['request']}"):
            home_page.enter_search_details(e_sub['request'])
        with allure.step('Click find button'):
            home_page.click_find_button()
        with allure.step(f"Check that {e_sub['request']} war recognition and {e_sub['answer']} was find"):
            assert e_sub['answer'] in home_page.search_result(), 'text couldnt be recognition'

    @allure.feature('Home Page')
    @allure.story('Side filters of lots')
    @allure.description('Changing section Test')
    @allure.title('Change section')
    @allure.severity('major')
    def test_change_section(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Change section'):
            home_page.change_section(driver)
        with allure.step('Check that section was change'):
            assert home_page.change_section_request() == home_page.change_section_result(), 'Section not changed'

    @allure.feature('Home Page')
    @allure.story('Content')
    @allure.description('Testing that we can go to any lot page')
    @allure.title('Go to any lot page')
    @allure.severity('critical')
    def test_go_to_any_lot_page(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Get name of clicked lot'):
            clicked_lot_name = home_page.name_of_clicked_lot()
        with allure.step('Click any lot'):
            home_page.click_any_lot()
        with allure.step('Check that clicked lot page was open'):
            assert clicked_lot_name == home_page.actual_lot_name(), 'Page didnt open'

    @allure.feature('Home Page')
    @allure.story('Add to favorites')
    @allure.description('Test of adding lot to favorites')
    @allure.title('Add to favorites')
    @allure.severity('major')
    def test_add_to_favorites(self, driver, authorization):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click any lot'):
            home_page.click_any_lot()
        with allure.step('Click add to favorites button'):
            home_page.add_lot_to_favor()
        with allure.step('Check that lot in favorites'):
            assert 'в избранном' in home_page.check_lot_added_in_favor(driver), 'Not in favorites'

    @allure.feature('Home Page')
    @allure.story('Head filters of lots')
    @allure.description('Choosing featured lots Test')
    @allure.title('Choose featured lots')
    @allure.severity('major')
    def test_choose_featured_lots(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Get section name of featured lots'):
            request_featured_lots = home_page.featured_lots_request()
        with allure.step('Choose featured lots: "Популярные"'):
            home_page.choose_featured_lots()
        with allure.step('Check that current lots is "Популярные"'):
            assert request_featured_lots == home_page.featured_lots_result(),\
                'Featured lots not selected'

    @allure.feature('Home Page')
    @allure.story('Head filters of lots')
    @allure.description('Resetting featured lots Test')
    @allure.title('Reset featured lots')
    @allure.severity('major')
    def test_reset_featured_lots(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Choose featured lots: "Популярные"'):
            home_page.choose_featured_lots()
        with allure.step('Click reset button'):
            home_page.reset_featured_lots()
        with allure.step('Check that all lots are displayed'):
            assert home_page.all_lots_is_displayed(), 'All lots isnt displayed '

    @allure.feature('Home Page')
    @allure.story('Content')
    @allure.description('Testing that total number of lots on Home page meets the requirements')  # mark
    @allure.title('Total number of lots on Home page')
    @allure.severity('minor')
    def test_total_number_of_lots(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Check that on Home page total number of lots are 15'):
            assert home_page.check_total_number_of_lots() == 15, 'Total number doest meet the requirement'


class TestHeader:

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Test that main logo is displayed on home page')
    @allure.title('Main logo is displayed')
    @allure.severity('trivial')
    def test_main_logo_is_displayed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Check that main logo is displayed'):
            assert home_page.logo_is_displayed(), 'Logo isnt displayed'

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Test that my location is displayed on home page')
    @allure.title('Mu location is displayed')
    @allure.severity('trivial')
    def test_my_location_is_displayed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Check that my location is displayed'):
            assert home_page.my_location_is_displayed(), 'My location isnt displayed'

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Changing of my location Test')
    @allure.title('Change of my location')
    @allure.severity('major')
    def test_change_of_location(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click location button'):
            home_page.click_location_button()
        with allure.step('Select wish location: "Гродно"'):
            home_page.select_wish_location()
        with allure.step('Check that current location is "Гродно"'):
            assert home_page.actual_location() in home_page.request_location(), 'Location wasnt changed '  # mark

    @allure.feature('Home Page')
    @allure.story('Header')
    @allure.description('Testing of create lot button')
    @allure.title('Create lot button')
    @allure.severity('critical')
    def test_create_lot_button(self, driver, authorization):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Click crate lot button'):
            home_page.click_create_lot_button()
        with allure.step('Check that sell page was open'):
            assert 'Создание лота' == home_page.title_of_creating_lot_page(), 'Create lot button didnt work'


class TestFooter:

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by news are displayed')
    @allure.title('Ay.by news are displayed')
    @allure.severity('trivial')
    def test_news_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Scroll page to bottom'):
            home_page.scroll_page_to_bottom()
        with allure.step('Check that Ay.by news are displayed'):
            assert home_page.news_ay_by_is_displayed(), 'Ay.by news did not displayed'

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by forum are displayed')
    @allure.title('Ay.by forum is displayed')
    @allure.severity('minor')
    def test_forum_ay_by_is_displayed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Scroll page to bottom'):
            home_page.scroll_page_to_bottom()
        with allure.step('Check that Ay.by forum are displayed'):
            assert home_page.forum_ay_by_is_displayed(), 'Ay.by forum did not displayed'

    @allure.feature('Home Page')
    @allure.story('Footer')
    @allure.description('Test that Ay.by info are displayed')
    @allure.title('Ay.by info is displayed')
    @allure.severity('trivial')
    def test_ay_by_info_is_displayed(self, driver):
        home_page = HomePage(driver)
        with allure.step('Open Home page'):
            home_page.open_home_page()
        with allure.step('Scroll page to bottom'):
            home_page.scroll_page_to_bottom()
        with allure.step('Check that that Ay.by info are displayed'):
            assert home_page.ay_by_info_is_displayed(), 'Ay.by info did not displayed'
