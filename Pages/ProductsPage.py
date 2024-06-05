from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class ProductsPage(BasePage):
    def __init__(self, driver, logger):
        self.driver = driver
        self.log = logger

    searchField = (By.ID, "search_product")
    searchButton = (By.ID, "submit_search")
    results = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    addedModal = (By.ID, "cartModal")
    viewCartButton = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")
    logInSignInTab = (By.CSS_SELECTOR, "a[href='/login']")
    searchedProductsText = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/h2")
    verifyCartProductName = (By.XPATH, "//*[@id='cart_info_table']/tbody/tr/td[2]/h4/a")

    def search(self, product):
        self.driver.find_element(*ProductsPage.searchField).send_keys(product)
        self.driver.find_element(*ProductsPage.searchButton).click()

    def add_to_cart(self):
        self.scroll_and_click(self.driver, ProductsPage.results)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProductsPage.addedModal))
        self.log.info("Clicking on View Cart")
        self.driver.find_element(*ProductsPage.viewCartButton).click()

    def get_cart_product(self):
        return self.driver.find_element(*ProductsPage.verifyCartProductName).text

    def move_to_login(self):
        self.driver.find_element(*ProductsPage.logInSignInTab).click()

    def get_searched_products_text(self):
        return self.driver.find_element(*ProductsPage.searchedProductsText).text

