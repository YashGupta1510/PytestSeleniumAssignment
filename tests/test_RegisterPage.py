from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage


class TestRegisterPage(BasePage):
    def test_register(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        login_page = LoginPage(self.driver)
        assert login_page.get_text() == "New User Signup!"
        login_page.signup(name="test", email="test#yash@test.com")
        assert self.driver.title == "Automation Exercise - Signup"
        register_page = RegisterPage(self.driver)
        register_page.fill_form(gender="Mr", password="121212", day="15", month="10", year="2001", fname="yash",
                                lname="gupta", company="nagarro", address1="test address", address2="test address2",
                                country="India", state="UttarPradesh", city="Lucknow", zipcode="226001",
                                mobile="7881132091")
        assert register_page.text_to_assert() == "ACCOUNT CREATED!"
        register_page.logout()
        assert home_page.logged_in_as() == " Logged in as test"
        home_page.delete_acc()
        assert register_page.text_to_assert() == "ACCOUNT DELETED!"
