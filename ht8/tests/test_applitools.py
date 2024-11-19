from selenium.webdriver.common.by import By
from pytest import mark

# Test data
INIT_URL = 'https://demo.applitools.com/index.html'
TARGET_URL = 'https://demo.applitools.com/app.html'

# Test will be executed twice: using Chrome & Firefox browsers, indirect=True allows to send parameters to the fixture
@mark.parametrize('driver', ['chrome','firefox'], indirect=True)
@mark.parametrize('username,password',[('admin','admin')])
def test_login_with_valid_credentials(driver,username,password):
    # Open the link
    driver.get(INIT_URL)
    # Find all the necessary elements on the page and assign variables
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'log-in')
    # Fill in username and password fields and click on 'Sign in' button
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    # Verify user is successfully logged in
    assert driver.current_url == TARGET_URL
    assert driver.title == 'ACME demo app'