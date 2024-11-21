import time
from selenium.webdriver.common.by import By

URL = 'https://www.wildberries.by/'

def test_xpath_1(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@class="main-page__banner banner"]')
    assert element.is_displayed()

def test_xpath_2(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@class="simple-menu__currency"]')
    time.sleep(10)
    assert element.is_displayed()

def test_xpath_3(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//button[contains(@class,"burger")]')
    assert element.is_displayed()

def test_xpath_4(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@id="searchBlock"]')
    assert element.is_displayed()

def test_xpath_5(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[contains(@class,"nav-element__logo")]')
    assert element.is_displayed()

def test_xpath_6(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[text()="            Корзина        "]')
    assert element.is_displayed()