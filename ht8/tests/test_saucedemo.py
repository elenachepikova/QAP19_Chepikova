from selenium.webdriver.common.by import By
from pytest import mark

INIT_URL = 'https://www.saucedemo.com/'
TARGET_URL = 'https://www.saucedemo.com/inventory.html'

@mark.parametrize('driver', ['chrome','firefox'], indirect=True)
@mark.parametrize('username,password',[('standard_user','secret_sauce')])
def test_positive_scenario(driver,username,password):
    driver.get(INIT_URL)
    # Test preparation: Find elements by NAME
    username_field = driver.find_element(By.NAME, 'user-name')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.NAME, 'login-button')
    # Test steps
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    assert driver.current_url == TARGET_URL

@mark.parametrize('driver', ['chrome','firefox'], indirect=True)
@mark.parametrize('username,password,text',[('','secret_sauce',"Epic sadface: Username is required"),
                                       ('standard_user','',"Epic sadface: Password is required"),
                                       ('123','secret_sauce',"Epic sadface: Username and password do not match any user in this service"),
                                       ('standard_user','123',"Epic sadface: Username and password do not match any user in this service"),
                                       ('locked_out_user','secret_sauce',"Epic sadface: Sorry, this user has been locked out.")])
def test_negative_scenario(driver,username,password,text):
    driver.get(INIT_URL)
    # Test preparation: Find elements by XPATH
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    error_button = driver.find_element(By.XPATH, '//*[@id="login_button_container"]')
    # Test steps
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    assert driver.current_url == INIT_URL
    assert error_button.text == text