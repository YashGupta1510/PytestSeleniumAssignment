from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    logInSignInTab = (By.CSS_SELECTOR, "a[href='/login']")
    loggedInAs = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    deleteAcc = (By.CSS_SELECTOR, "a[href='/delete_account']")

    def move_to_sign_in_page(self):
        self.log.info("Moving to SignIn Page.")
        return self.driver.find_element(*HomePage.logInSignInTab).click()

    def logged_in_as(self):
        return self.driver.find_element(*HomePage.loggedInAs).text

    def delete_acc(self):
        self.log.info("Deleting account")
        self.driver.find_element(*HomePage.deleteAcc).click()
