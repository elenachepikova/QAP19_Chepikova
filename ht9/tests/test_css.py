from selenium.webdriver.common.by import By
import time
import allure

URL = 'https://www.wildberries.by/'

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("01_Banner_is_present")
def test_css_1(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'div.main-page__banner.banner')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("02_Currency_icon_is_present")
def test_css_2(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'span.simple-menu__currency')
    time.sleep(5)
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("03_Navigation_menu_is_present")
def test_css_3(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'button[class*="burger"]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("04_Search_field_is_present")
def test_css_4(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'div#searchBlock')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("05_Site_logo_is_present")
def test_css_5(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[class*="nav-element__logo"]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("CSS")
@allure.title("06_Cart_is_present")
def test_css_6(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[data-wba-header-name="Cart"]')
    time.sleep(5)
    assert element.is_displayed()