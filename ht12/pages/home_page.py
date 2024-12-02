import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht12.core.actions import Actions
from ht12.core.assertions import Assertions
from ht12.data.test_data import DOMAIN


class HomePage(Actions):
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'sign-in-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = DOMAIN
        self.assertions = Assertions(self.driver)

    @allure.step('Open "BookBub" Home page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "Home page" is opened')
    def assert_page_is_displayed(self):
        assert self.driver.current_url == self.page, f"Url should be {self.page}, but is {self.driver.current_url}"
        assert self.driver.title == 'BookBub: Get amazing deals on bestselling ebooks'

    @allure.step('Click on "Sign In" button on Home page')
    def click_sign_in(self):
        self.click_on(self.SIGN_IN_BUTTON)
