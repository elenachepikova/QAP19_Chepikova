from selenium.webdriver.common.by import By
import time

URL = 'https://www.wildberries.by/'

def test_css_1(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'div.main-page__banner.banner')
    assert element.is_displayed()

def test_css_2(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'span.simple-menu__currency')
    time.sleep(10)
    assert element.is_displayed()

def test_css_3(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'button[class*="burger"]')
    assert element.is_displayed()

def test_css_4(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'div#searchBlock')
    assert element.is_displayed()

def test_css_5(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[class*="nav-element__logo"]')
    assert element.is_displayed()

def test_css_6(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[data-wba-header-name="Cart"]')
    assert element.is_displayed()