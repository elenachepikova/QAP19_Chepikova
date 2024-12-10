import allure

from ht11.elements.header import NavigationPanel
from ht11.pages.contact_page import ContactPage
from ht11.pages.home_page import HomePage


@allure.suite("Tests for 'CONTACT' page")
class TestContactPage:
    @allure.title("Verify 'CONTACT' page is accessible via navigation panel")
    def test_open_contact_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on(panel.CONTACT)
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()
