from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class TestHomePage(BasePage):
    def test_move_to_sign_in_page(self):
        home_page = HomePage(self.driver)
        home_page.move_to_sign_in_page()
        assert self.driver.title == "Automation Exercise - Signup / Login"
