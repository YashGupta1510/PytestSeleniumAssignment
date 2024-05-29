from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


class TestLoginPage(BasePage):
    def test_signup(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(self.driver)
        login_page.signup(name="test", email="test#yash@test.com")
        assert self.driver.title == "Automation Exercise - Signup"
