from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, logger):
        self.driver = driver
        self.log = logger

    testSignupText = (By.TAG_NAME, "h2")
    signupNameField = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    signupEmailField = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signupButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    loginEmailField = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    loginPasswordField = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    loginButton = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    warningText = (By.XPATH, "//p[text()='Email Address already exist!']")

    def get_text(self, index):
        elements = self.driver.find_elements(*LoginPage.testSignupText)
        return elements[index].text

    def enter_signup_name(self, name):
        self.log.info(f"Using value {name} for name")
        return self.driver.find_element(*LoginPage.signupNameField).send_keys(name)

    def enter_signup_email(self, email):
        self.log.info(f"Using value {email} for email")
        return self.driver.find_element(*LoginPage.signupEmailField).send_keys(email)

    def click_signup_button(self):
        return self.driver.find_element(*LoginPage.signupButton).click()

    def enter_login_email(self, email):
        self.log.info(f"Using value {email} for email")
        return self.driver.find_element(*LoginPage.loginEmailField).send_keys(email)

    def enter_login_password(self, password):
        self.log.info(f"Using value {password} for password")
        return self.driver.find_element(*LoginPage.loginPasswordField).send_keys(password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPage.loginButton).click()

    def signup(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup_button()

    def login(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login_button()

    def get_warning(self):
        return self.driver.find_element(*LoginPage.warningText).text
