import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht12.core.actions import Actions
from ht12.core.assertions import Assertions
from ht12.data.test_data import DOMAIN


class ExploreAllDealsPage(Actions):
    HEADER_TEXT = (By.CSS_SELECTOR, '.header-text')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}ebook-deals?categories='
        self.title = 'Ebooks Deals Up to 95% Off for Any Genre and Any Ereader - BookBub'
        self.header = self.get_element(self.HEADER_TEXT)
        self.assertions = Assertions(self.driver)

    @allure.step('Assert "Explore All Deals" page is opened')
    def assert_page_is_displayed(self):
        assert self.driver.current_url == self.page, f"Url should be {self.page}, but is {self.driver.current_url}"
        self.assertions.assert_page_title(self.title)
        assert self.header.text == 'Explore All Deals'
