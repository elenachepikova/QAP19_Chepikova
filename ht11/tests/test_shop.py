import allure

from ht11.elements.header import NavigationPanel
from ht11.pages.home_page import HomePage
from ht11.pages.shop_page import ShopPage


@allure.suite("Tests for 'SHOP' page")
class TestShopPage:
    @allure.title("Verify 'SHOP' page is accessible via navigation panel")
    def test_open_shop_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on(panel.SHOP)
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
