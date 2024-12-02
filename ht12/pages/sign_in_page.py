import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht12.core.actions import Actions
from ht12.core.assertions import Assertions
from ht12.data.test_data import DOMAIN, TEST_EMAIL, TEST_PASSWORD


class SignInPage(Actions):
    EMAIL_FIELD = (By.ID, 'user_email_address')
    PASSWORD_FIELD = (By.ID, 'user_password')
    SIGN_IN_WITH_EMAIL_BUTTON = (By.ID, 'login-submit')
    STAY_SIGNED_IN_CHECKBOX = (By.ID, 'user_remember_me')
    PASSWORD_TROUBLE_LINK = (By.CLASS_NAME, 'password-link')
    CONTINUE_WITH_GOOGLE = (By.CLASS_NAME, 'google-oauth-button')
    MAGIC_LINK_EMAIL_FIELD = (By.ID, 'magic-link-email-field')
    MAGIC_LINK_BUTTON = (By.ID, 'magic-link-submit-button')
    SIGN_UP_LINK = (By.CSS_SELECTOR, '.lava.raw-link')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-danger')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}users/sign_in'
        self.email = TEST_EMAIL
        self.password = TEST_PASSWORD
        self.assertions = Assertions(self.driver)

    @allure.step('Assert "Sign In" page is opened')
    def assert_page_is_displayed(self):
        assert self.driver.current_url == self.page, f"Url should be {self.page}, but is {self.driver.current_url}"
        assert self.driver.title == 'BookBub - Sign in'

    @allure.step('Fill in "Email" field')
    def enter_user_email(self):
        self.add_text(self.email, self.EMAIL_FIELD)

    @allure.step('Fill in "Password" field')
    def enter_password(self):
        self.add_text(self.password, self.PASSWORD_FIELD)

    @allure.step('Click on "Sign in with email" button')
    def sign_in_with_email(self):
        self.click_on(self.SIGN_IN_WITH_EMAIL_BUTTON)

    @allure.step('Assert error message is displayed on "Sign In" page')
    def assert_error_is_displayed(self):
        error_message = self.get_element(self.ERROR_MESSAGE)
        assert error_message.text == 'The email address or password you entered is incorrect.'

    @allure.step('Assert presence of "Sign In" page elements')
    def assert_elements_are_present(self):
        self.assertions.assert_element_is_visible(self.EMAIL_FIELD)
        self.assertions.assert_element_is_visible(self.PASSWORD_FIELD)
        self.assertions.assert_element_is_selected(self.STAY_SIGNED_IN_CHECKBOX)
        self.assertions.assert_element_is_visible(self.PASSWORD_TROUBLE_LINK)
        self.assertions.assert_element_is_visible(self.SIGN_IN_WITH_EMAIL_BUTTON)
        self.assertions.assert_element_is_visible(self.CONTINUE_WITH_GOOGLE)
        self.assertions.assert_element_is_visible(self.MAGIC_LINK_EMAIL_FIELD)
        self.assertions.assert_element_is_visible(self.MAGIC_LINK_BUTTON)
        self.assertions.assert_element_is_visible(self.SIGN_UP_LINK)
