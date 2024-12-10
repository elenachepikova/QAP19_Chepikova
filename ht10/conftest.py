import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    download_dir = os.path.abspath('/test/downloads')

    options = FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/pdf,text/plain")
    options.set_preference("pdfjs.disabled", True)

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                               options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
