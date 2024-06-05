import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage
from Utils.DataReader import product, password, email


class TestProductsPage:

    @pytest.mark.run(order=5)
    def test_search_and_verify_cart(self, setup):
        driver, logger = setup
        home_page = HomePage(driver, logger)
        home_page.move_to_products_page()
        assert driver.title == "Automation Exercise - All Products"
        products_page = ProductsPage(driver, logger)
        products_page.search(product)
        assert products_page.get_searched_products_text() == "SEARCHED PRODUCTS"
        products_page.add_to_cart()
        assert products_page.get_cart_product() == "Men Tshirt"
        products_page.move_to_login()
        login_page = LoginPage(driver, logger)
        login_page.login(email, password)
        home_page.move_to_cart_page()
        assert products_page.get_cart_product() == "Men Tshirt"
