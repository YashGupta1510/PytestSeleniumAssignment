import pytest
import logging

from selenium.webdriver import ActionChains


class BasePage:
    def scroll_and_click(self, driver, element):
        e = driver.find_element(*element)
        actions = ActionChains(driver)
        actions.move_to_element(e).perform()
        driver.execute_script("arguments[0].click();", e)
