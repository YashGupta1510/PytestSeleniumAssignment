import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utils.DataReader import email, password, name_on_card, cardNumber, cvc, year, month


class TestHomePage:
    @pytest.mark.run(order=4)
    def test_subscription(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        assert driver.title == "Automation Exercise"
        home_page.subscribe(email)
        assert home_page.success_subscribe_msg() == "You have been successfully subscribed!"

    @pytest.mark.run(order=6)
    def test_checkout(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        home_page.move_to_sign_in_page()
        LoginPage(driver, logger).login(email, password)
        home_page.add_to_cart()
        assert driver.title == "Automation Exercise - Payment"
        home_page.payment(name_on_card, cardNumber, cvc, month, year)
        assert home_page.get_success_order_message() == "Your order has been placed successfully!"

    @pytest.mark.run(order=7)
    def test_delete_acc(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        home_page.delete_acc()
