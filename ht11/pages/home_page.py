import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions
from ht11.data.test_data import DOMAIN, TITLE


class HomePage(Actions):
    BANNER = (By.ID, 'bb-section-512921E4-B305-83EC-0A36-1A624B3CBBFA')
    FEATURED_SECTION = (By.ID, 'bb-section-512921E5-B3EE-81BE-E747-F1A82516138D')
    RECENT_REVIEWS = (By.ID, 'bb-section-512921E6-02B3-DB71-72CB-05545E668750')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = DOMAIN
        self.title = TITLE
        self.assertions = Assertions(self.driver)

    @allure.step('Open Home page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "Home page" is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_url(self.page)
        self.assertions.assert_page_title(self.title)
        self.assert_sections_are_present()

    @allure.step('Assert "HOME" page elements are present')
    def assert_sections_are_present(self):
        self.assertions.assert_element_is_visible(self.BANNER), 'BANNER not displayed'
        self.assertions.assert_element_is_visible(self.FEATURED_SECTION), 'FEATURED_SECTION not displayed'
        self.assertions.assert_element_is_visible(self.RECENT_REVIEWS), 'RECENT_REVIEWS not displayed'
