import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utils.DataReader import wrong_email, name, email, password


class TestLoginPage:

    @pytest.mark.run(order=3)
    def test_login(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(driver, logger)
        assert login_page.get_text(0) == "Login to your account"
        login_page.login(email, password)
        assert home_page.logged_in_as() == "Logged in as test"

    @pytest.mark.run(order=1)
    def test_failed_signup(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(driver, logger)
        assert login_page.get_text(2) == "New User Signup!"
        login_page.signup(name, wrong_email)
        assert login_page.get_warning() == "Email Address already exist!"
