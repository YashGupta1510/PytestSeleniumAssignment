import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

from Utils.DataReader import URL

@pytest.fixture(scope='module')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        chrome_options = Options()
        if headless == "true":
            print("came to headless")
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(chrome_options)
        else:
            driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(20)

    assert driver.title == "Automation Exercise"

    logger = logging.getLogger(__name__)
    file_handler_exists = any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)
    if not file_handler_exists:
        file_handler = logging.FileHandler("logFILE.log", encoding='utf-8')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s -%(filename)s - %(funcName)20s()]- %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info("------NEW RUN------")

    # Causing error - AttributeError: cls not available in module-scoped context - when set module scope for cli run
    # request.cls.logger = logger
    # request.cls.driver = driver
    # changed yield to yield driver, logger

    yield driver, logger

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser name: chrome, opera, edge, firefox"
    )
    parser.addoption(
        "--headless", action="store", default="false", help="Set flag true to run in Headless Mode"
    )
