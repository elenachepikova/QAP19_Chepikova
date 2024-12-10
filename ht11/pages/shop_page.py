import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions
from ht11.data.test_data import DOMAIN, TITLE


class ShopPage(Actions):
    ALL_PRODUCTS_TITLE = (By.CSS_SELECTOR, 'h2.bb-font-h2')

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
        self.assertions.assert_page_url(self.page)
        self.assertions.assert_page_title(self.title)
        self.assertions.assert_element_is_visible(self.ALL_PRODUCTS_TITLE)
