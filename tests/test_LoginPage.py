from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


class TestLoginPage(BasePage):
    def test_signup(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(self.driver)
        assert login_page.get_text(2) == "New User Signup!"
        login_page.signup(name="test", email="test#yash@test.com")
        assert self.driver.title == "Automation Exercise - Signup"

    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(self.driver)
        assert login_page.get_text(0) == "Login to your account"
        login_page.login("test#yash@test.com", "121212")
        assert home_page.logged_in_as() == " Logged in as test"

    def test_failed_signup(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(self.driver)
        assert login_page.get_text(2) == "New User Signup!"
        login_page.signup(name="test", email="test@test.com")
        assert login_page.get_warning() == "Email Address already exist!"
