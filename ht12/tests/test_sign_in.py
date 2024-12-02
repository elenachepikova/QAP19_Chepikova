from ht12.pages.explore_all_deals_page import ExploreAllDeals
from ht12.pages.home_page import HomePage
from ht12.pages.sign_in_page import SignInPage


class TestSignIn:

    def test_all_elements_are_present(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_sign_in()
        sign_in_page = SignInPage(driver)
        sign_in_page.assert_elements_are_present()

    def test_incorrect_credentials_error(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_sign_in()
        sign_in_page = SignInPage(driver)
        sign_in_page.sign_in_with_email()
        sign_in_page.assert_page_is_displayed()
        sign_in_page.assert_error_is_displayed()

    def test_successful_sign_in(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_sign_in()
        sign_in_page = SignInPage(driver)
        sign_in_page.enter_user_email()
        sign_in_page.enter_password()
        sign_in_page.sign_in_with_email()
        explore_all_deals = ExploreAllDeals(driver)
        explore_all_deals.assert_page_is_displayed()
