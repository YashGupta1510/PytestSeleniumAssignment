import pytest
from selenium import webdriver

URL = "https://automationexercise.com/"


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()
