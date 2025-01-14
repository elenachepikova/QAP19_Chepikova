from ht12.pages.home_page import HomePage
from ht12.pages.sign_in_page import SignInPage


class TestHomePage:

    def test_open_home_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_page_is_displayed()

    def test_click_on_sign_in_button(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_sign_in()
        sign_in_page = SignInPage(driver)
        sign_in_page.assert_page_is_displayed()
