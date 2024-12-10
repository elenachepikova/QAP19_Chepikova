import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions
from ht11.data.test_data import DOMAIN, TITLE


class ContactPage(Actions):
    CONTACT_US_BANNER = (By.ID, 'bb-section-51292A57-9603-A922-BC8E-363F9F372AE4')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}contact'
        self.title = f'CONTACT | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open CONTACT page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "CONTACT" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_url(self.page)
        self.assertions.assert_page_title(self.title)
        self.assertions.assert_element_is_visible(self.CONTACT_US_BANNER)
