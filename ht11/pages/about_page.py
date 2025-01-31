import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions
from ht11.data.test_data import DOMAIN, TITLE


class AboutPage(Actions):
    ABOUT_US_BANNER = (By.ID, 'bb-section-5129237E-F62C-D51F-8FF0-2BFF121EE5F7')
    CONTACT_US = (By.XPATH, '//button[contains(text(),"CONTACT US")]')
    SHOP_NOW = (By.CSS_SELECTOR, 'button.btn-secondary')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}about'
        self.title = f'ABOUT | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open About page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "About" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_url(self.page)
        self.assertions.assert_page_title(self.title)
        self.assertions.assert_element_is_visible(self.ABOUT_US_BANNER)

