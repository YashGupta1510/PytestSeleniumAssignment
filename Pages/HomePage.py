from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver, logger):
        self.driver = driver
        self.log = logger

    logInSignInTab = (By.CSS_SELECTOR, "a[href='/login']")
    cartTab = (By.CSS_SELECTOR, "a[href='/view_cart']")
    productsTab = (By.CSS_SELECTOR, "a[href='/products']")
    deleteAccTab = (By.CSS_SELECTOR, "a[href='/delete_account']")
    loggedInAs = (By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a")
    subscriptionText = (By.XPATH,"//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
    emailField = (By.ID, "susbscribe_email")
    emailButton = (By.ID, "subscribe")
    successSubscribeText = (By.ID, "success-subscribe")
    addToCartButton = (By.CSS_SELECTOR, "a[data-product-id='2']")
    addedModal = (By.ID, "cartModal")
    viewCartButton = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")
    cartPageInfo = (By.ID, "cart_info")
    proceedToCheckOut = (By.XPATH, "//*[@id='do_action']/div[1]/div/div/a")
    descriptionTextareaField = (By.TAG_NAME, "textarea")
    proceedToPaymentButton = (By.CSS_SELECTOR, "a[href='/payment']")

    nameOnCardField = (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
    cardNumberField = (By.CSS_SELECTOR, "input[data-qa='card-number']")
    cvcField = (By.CSS_SELECTOR, "input[data-qa='cvc']")
    monthField = (By.CSS_SELECTOR, "input[data-qa='expiry-month']")
    yearField = (By.CSS_SELECTOR, "input[data-qa='expiry-year']")
    paymentButton = (By.ID, "submit")
    orderSuccessMessage = (By.ID, "success_message")

    def move_to_sign_in_page(self):
        self.log.info("Moving to SignIn Page.")
        return self.scroll_and_click(self.driver, HomePage.logInSignInTab)

    def logged_in_as(self):
        return self.driver.find_element(*HomePage.loggedInAs).text

    def subscribe(self, email):
        self.log.info("On Home Page to Subscribe")
        element = self.driver.find_element(*HomePage.subscriptionText)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        assert element.text == "SUBSCRIPTION"
        self.enter_email_and_submit(email)

    def enter_email_and_submit(self, email):
        self.driver.find_element(*HomePage.emailField).send_keys(email)
        self.driver.find_element(*HomePage.emailButton).click()

    def success_subscribe_msg(self):
        element = self.driver.find_element(*HomePage.successSubscribeText)
        return element.text

    def add_to_cart(self):
        self.log.info("Clicking on Product")
        self.scroll_and_click(self.driver, HomePage.addToCartButton)

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(HomePage.addedModal))

        self.log.info("Clicking on View Cart")
        self.driver.find_element(*HomePage.viewCartButton).click()

        self.log.info("Clicking on Proceed to Checkout")
        self.scroll_and_click(self.driver, HomePage.proceedToCheckOut)

        self.log.info("Entering Description for order")
        self.driver.find_element(*HomePage.descriptionTextareaField).send_keys("TESTING the textarea"
                                                                               "and moving to confirm order")

        self.scroll_and_click(self.driver, HomePage.proceedToPaymentButton)

    def payment(self, name_on_card, number, cvc, month, year):
        self.log.info("Completing Payment form")
        self.log.info(f"Detail: nameOnCard is {name_on_card}, number is {number}, cvc is {cvc}, expiry month is {month}"
                      f", expiry year is {year}")
        self.driver.find_element(*HomePage.nameOnCardField).send_keys(name_on_card)
        self.driver.find_element(*HomePage.cardNumberField).send_keys(number)
        self.driver.find_element(*HomePage.cvcField).send_keys(cvc)
        self.driver.find_element(*HomePage.monthField).send_keys(month)
        self.driver.find_element(*HomePage.yearField).send_keys(year)
        self.scroll_and_click(self.driver, HomePage.paymentButton)

    def get_success_order_message(self):
        self.log.info("Order Complete Moving to SignIn Page.")
        self.driver.back()
        return self.driver.find_element(*HomePage.orderSuccessMessage).text

    def move_to_products_page(self):
        self.log.info("Moving to Products Page.")
        self.driver.find_element(*HomePage.productsTab).click()

    def move_to_cart_page(self):
        self.log.info("Moving to SignIn Page.")
        return self.driver.find_element(*HomePage.cartTab).click()

    def delete_acc(self):
        self.log.info("Deleting account")
        self.driver.find_element(*HomePage.deleteAccTab).click()

