from selenium import webdriver
from selenium.webdriver.firefox.service import Service

import geckodriver_autoinstaller

import pytest


@pytest.fixture(params=["chrome", "firefox"]) # to run tests both in chrome and firefox
def driver(request):

    # browser = request.config.getoption("--browser") # to run tests separately  in chrome and firefox using --browser in command line
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == 'chrome':
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        geckodriver_autoinstaller.install()
        service = Service("/snap/bin/firefox.geckodriver")
        my_driver = webdriver.Firefox( service=service)        
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit() #my_driver.close() closes only current tab


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
