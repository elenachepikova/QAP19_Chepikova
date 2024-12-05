import allure
from selenium.webdriver.firefox.webdriver import WebDriver

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions
from ht11.data.test_data import DOMAIN, TITLE


class ShopPage(Actions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}shop'
        self.title = f'SHOP | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open SHOP page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "SHOP" page is opened')
    def assert_page_is_displayed(self):
        assert self.driver.current_url == self.page, f"Url should be {self.page}, but is {self.driver.current_url}"
        assert self.driver.title == self.title
