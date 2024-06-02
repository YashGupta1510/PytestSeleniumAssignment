import pytest
from selenium import webdriver

URL = "https://automationexercise.com/"


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
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

    request.cls.driver = driver

    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser name: chrome, opera, edge, firefox"
    )
