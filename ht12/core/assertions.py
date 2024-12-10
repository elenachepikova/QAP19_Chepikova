from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ht12.core.actions import Actions


class Assertions(Actions):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def assert_element_is_visible(self, selector):
        self.wait.until(EC.visibility_of_element_located(selector))
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    def assert_element_is_displayed(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    def assert_element_is_selected(self, selector):
        element = self.get_element(selector)
        assert element.is_selected(), f"Element {selector} is not selected"

    def assert_page_title(self, title):
        assert self.driver.title == title
