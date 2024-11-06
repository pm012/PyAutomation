from selenium import webdriver
from selenium.webdriver.firefox.service import Service

import os
import geckodriver_autoinstaller
import logging
import pytest
import datetime

def get_current_date_time()->str:    
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

logging_configured = False
logger = logging.getLogger(__name__)

def pytest_configure(config):
    global logging_configured  # Access the global flag
    if not logging_configured:
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logging only once
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/debug_{get_current_date_time()}.log"),
                logging.StreamHandler()  # Log to both file and console
            ]
        )

        for handler in logging.getLogger().handlers:
            if isinstance(handler, logging.StreamHandler):
                handler.setLevel(logging.INFO)
        
        # Set root logger level to INFO to ensure logs are shown in console
        logging.getLogger().setLevel(logging.INFO)
        logger.info("Logging is configured")

        logging_configured = True  # Set the flag to prevent re-configuring
    else:
        logger.info("Logging already configured")
    


#@pytest.fixture(params=["chrome", "firefox"]) # to run tests both in chrome and firefox
@pytest.fixture
def driver(request):
    
    browser = request.config.getoption("--browser") # to run tests separately  in chrome and firefox using --browser in command line
    # browser = request.param # uncomment fixture with parameter to use all browsers defined in parametrized fixture
    print(f"Creating {browser} driver")
    if browser == 'chrome':
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        geckodriver_autoinstaller.install()
        service = Service("/snap/bin/firefox.geckodriver")
        my_driver = webdriver.Firefox( service=service)        
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    # my_driver.implicitly_wait(5) # to wait implicitly for 5 seconds in test
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit() #my_driver.close() closes only current tab


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
