from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    logInSignInTab = (By.CSS_SELECTOR, "a[href='/login']")

    def move_to_sign_in_page(self):
        self.log.info("Moving to SignIn Page.")
        return self.driver.find_element(*HomePage.logInSignInTab).click()
