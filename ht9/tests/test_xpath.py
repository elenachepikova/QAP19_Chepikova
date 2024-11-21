import time
from selenium.webdriver.common.by import By
import allure

URL = 'https://www.wildberries.by/'

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH01_Banner_is_present")
def test_xpath_1(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@class="main-page__banner banner"]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH02_Currency_icon_is_present")
def test_xpath_2(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@class="simple-menu__currency"]')
    time.sleep(10)
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH03_Navigation_menu_is_present")
def test_xpath_3(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//button[contains(@class,"burger")]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH04_Search_field_is_present")
def test_xpath_4(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@id="searchBlock"]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH05_Site_logo_is_present")
def test_xpath_5(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[contains(@class,"nav-element__logo")]')
    assert element.is_displayed()

@allure.suite("L20_Locators")
@allure.sub_suite("XPATH")
@allure.title("XPATH06_Cart_is_present")
def test_xpath_6(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[text()="            Корзина        "]')
    assert element.is_displayed()