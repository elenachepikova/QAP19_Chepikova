import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ht11.core.actions import Actions
from ht11.core.assertions import Assertions


class Cart(Actions):
    TITLE = (By.CSS_SELECTOR, '.mb-0.bb-font-h5')
    CLOSE_ICON = (By.XPATH, '//*[@aria-label="Close Sidebar"]')
    MESSAGE = (By.CSS_SELECTOR, '.text-center.mt-5>.bb-font-h5')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button.btn.mt-4')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)
        self.assertions = Assertions(self.driver)
        self.message = self.get_element(self.MESSAGE)

    @allure.step('Assert Cart sidebar is opened in empty state')
    def assert_empty_cart_is_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        self.assertions.assert_element_is_visible(self.TITLE)
        self.assertions.assert_element_is_visible(self.CLOSE_ICON)
        self.assertions.assert_element_is_visible(self.MESSAGE)
        assert self.message.text == 'Your Cart is Empty'
        self.assertions.assert_element_is_visible(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step('Assert Cart sidebar is not displayed')
    def assert_cart_is_not_displayed(self):
        assert not self.assertions.assert_element_is_visible(self.TITLE), "Cart sidebar is still visible!"
